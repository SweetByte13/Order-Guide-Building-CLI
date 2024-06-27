from models.__init__ import CURSOR, CONN
from models.proveyer import Proveyer
from models.item import Item

class Proveyer_Item:
    all = {}
    
    def __init__(self, name, item_id, proveyer_id, price, case_size):
        self.name = name
        self.item_id = item_id
        self.proveyer_id = proveyer_id
        self.price = price
        self.case_size = case_size
        self.item = None
        self.proveyer = None
        
    def __repr__(self):
        return f"Proveyer Item {self.id}: {self.name}, {self.item_id}, {self.proveyer_id}, {self.price}, {self.case_size}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if  isinstance (name, str):
            self._name = name
        else:
            raise TypeError(f'{name} is not valid, Proveyer_Item must have a name.')
    
    @property
    def item_id(self):
        return self._item_id
    
    @item_id.setter
    def item_id(self, new_item_id):
        if  isinstance (new_item_id, int):
            self._item_id = new_item_id
        else:
            raise TypeError(f'{new_item_id} is not a valid item ID, Proveyer_Item must have a item ID.')
            
    @property
    def proveyer_id(self):
        return self._proveyer_id
    
    @proveyer_id.setter
    def proveyer_id(self, proveyer_id):
        if  isinstance (proveyer_id, int) and Proveyer.find_by_id(proveyer_id):
            self._proveyer_id = proveyer_id
        else:
            raise TypeError(f'{proveyer_id} is not a valid proveyer ID, Proveyer_Item must have a proveyer ID.')
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if  isinstance (new_price, int):
            self._price= new_price
        else:
            raise TypeError(f'{new_price} is not valid, Proveyer_Item must have a price.')
        
    @property
    def case_size(self):
        return self._case_size
    
    @case_size.setter
    def case_size(self, new_case_size):
        if  isinstance (new_case_size, int):
            self._case_size= new_case_size
        else:
            raise TypeError(f'{new_case_size} is not valid, Proveyer_Item must have a case size.')
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS proveyer_item (
            id INTEGER PRIMARY KEY,
            name TEXT,
            item_id INTEGER,
            proveyer_id INTEGER,
            price INTEGER,
            case_size INTEGER,
            FOREIGN KEY (item_id) REFERENCES item(id),
            FOREIGN KEY (proveyer_id) REFERENCES proveyer(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
            
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS proveyer_item;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO proveyer_item (name, item_id, proveyer_id, price, case_size)
                VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.item_id, self.proveyer_id, self.price, self.case_size))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE proveyer_item
            SET name = ?, item_id = ?, proveyer_id = ?, price = ?, case_size = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.item_id, self.proveyer_id, self.price,
                             self.case_size, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM proveyer_item
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, item_id, proveyer_id, price, case_size):
        proveyer_item = cls(str(name), int(item_id), int(proveyer_id), int(price), int(case_size))
        proveyer_item.save()
        return proveyer_item

    @classmethod
    def instance_from_db(cls, row):
        proveyer_item = cls.all.get(row[0])
        if proveyer_item:
            proveyer_item.id=int(row[0])
            proveyer_item.name=str(row[1])
            proveyer_item.item_id = int(row[2])
            proveyer_item.proveyer_id = int(row[3])
            proveyer_item.price = int(row[4])
            proveyer_item.case_size = int(row[5])
        else:
            proveyer_item = cls(str(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))
            proveyer_item.id = row[0]
            cls.all[proveyer_item.id] = proveyer_item
        return proveyer_item

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM proveyer_item
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM proveyer_item
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_proveyer_id(cls, proveyer_id):
        sql = """
            SELECT *
            FROM proveyer_item
            WHERE proveyer_id is ?
        """
        row = CURSOR.execute(sql, (proveyer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_item_id(cls, item_id):
        sql = """
            SELECT *
            FROM proveyer_item
            WHERE item_id is ?
        """
        row = CURSOR.execute(sql, (item_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def load_related_proveyer(self):
        sql = """
            SELECT * 
            FROM proveyers
            WHERE id=?
        """
        row = CURSOR.execute(sql, (self.proveyer_id,)).fetchone()
        self.proveyer=Proveyer.instance_from_db(row)
        
    def load_related_item(self):
        sql = """
            SELECT * 
            FROM items
            WHERE id=?
        """
        row = CURSOR.execute(sql, (self.item_id,)).fetchone()
        self.item=Item.instance_from_db(row)