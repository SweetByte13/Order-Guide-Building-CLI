from models.__init__ import CURSOR, CONN

class Item:

    all = {}
    
    def __init__(self, name, par_id, catagory_id):
        self.name = name
        self.par_id = par_id
        self.catagory_id = catagory_id
        self.proveyer_items = []
        self.catagory = None
        self.par = None
        
    def __repr__(self):
        return f"Item {self.id}: {self.name}, {self.par_id}, {self.catagory_id}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not valid, Item must have a name')
        
    @property
    def par_id(self):
        return self._par_id
    
    @par_id.setter
    def par_id(self, new_par_id):
        if isinstance (new_par_id, int):
            self._par_id = new_par_id
        else:
            raise TypeError(f'{new_par_id} is not a valid par ID, Items must have a par ID')
        
    @property
    def catagory_id(self):
        return self._catagory_id
    
    @catagory_id.setter
    def catagory_id(self, new_catagory_id):
        if isinstance (new_catagory_id, int):
            self._catagory_id = new_catagory_id
        else:
            raise TypeError(f'{new_catagory_id} is not a valid catagory ID, Items must have a catagory ID')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            par_id INTEGER,
            catagory_id INTEGER,
            FOREIGN KEY (par_id) REFERENCES par(id),
            FOREIGN KEY (catagory_id) REFERENCES catagory(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, par_id, catagory_id):
        item = cls(str(name), int(par_id), int(catagory_id))
        item.save()
        return item
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS items
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.name = str(row[1])
            item.par_id = int(row[2])
            item.catagory_id = int(row [3])
        else:
            item = cls(str(row[1]), int(row[2]), int(row[3]))
            item.id = row[0]
            cls.all[item.id] = item
        return item
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM items
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM items
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM items
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO items(name, par_id, catagory_id)
            VALUES (?,?,?)
        """    
        CURSOR.execute(sql, (self.name, self.par_id, self.catagory_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE items
            SET name=?, par_id=?, catagory_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.name, self.par_id, self.catagory_id, self.id))
        CONN.commit()
        
    def delete(self):
        sql_P_delete = """
            DELETE FROM proveyer_item
            WHERE item_id = ?
        """
        sql = """
            DELETE FROM items
            WHERE id=?
        """
        CURSOR.execute(sql_P_delete, (self.id,))
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
        
    def load_related_catagories(self):
        from models.catagory import Catagory
        sql = """
            SELECT * 
            FROM catagories
            WHERE id=?
        """
        row = CURSOR.execute(sql, (self.catagory_id,)).fetchone()
        self.catagory=Catagory.instance_from_db(row)
        
    def load_related_par(self):
        from models.par import Par
        sql = """
            SELECT * 
            FROM pars
            WHERE id=?
        """
        row = CURSOR.execute(sql, (self.par_id,)).fetchone()
        self.par=Par.instance_from_db(row)
       
    def load_related_proveyer_items(self):
        from models.proveyer_item import Proveyer_Item
        sql = """
            SELECT * 
            FROM proveyer_item
            WHERE item_id=?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        self.proveyer_items=[Proveyer_Item.instance_from_db(row) for row in rows]
        
    @classmethod   
    def print_item(cls, item):
        from helpers import format_spacing_for_print
        print(f'|{format_spacing_for_print(item.name)}|{format_spacing_for_print(item.par.stock)}|{format_spacing_for_print(item.par.par_amount)}|')