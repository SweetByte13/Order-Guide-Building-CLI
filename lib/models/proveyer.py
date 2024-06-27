from models.__init__ import CURSOR, CONN


class Proveyer:
    all = {}
    
    def __init__(self, name, cut_off_time, order_min):
        self.name = name
        self.cut_off_time = cut_off_time
        self.order_min = order_min
        self.proveyer_catagories = []
        self.proveyer_items = []
        
    def __repr__(self):
        return f"Proveyer {self.id}: {self.name}, {self.cut_off_time}, {self.order_min}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not valid, Proveyers must have a name.')
        
    @property
    def cut_off_time(self):
        return self._cut_off_time
    
    @cut_off_time.setter
    def cut_off_time(self, new_cut_off_time):
        if isinstance (new_cut_off_time, int):
            self._cut_off_time = new_cut_off_time
        else:
            raise TypeError(f'{new_cut_off_time} is not valid, Proveyers must have a cut off time.')
        
    @property
    def order_min(self):
        return self._order_min
    
    @order_min.setter
    def order_min(self, new_order_min):
        if isinstance (new_order_min, int):
            self._order_min = new_order_min
        else:
            raise TypeError(f'{new_order_min} is not valid, Proveyers must have a order minimum.')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS proveyers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cut_off_time INTEGER,
            order_min INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, cut_off_time, order_min):
        proveyer = cls(str(name), int(cut_off_time), int(order_min))
        proveyer.save()
        return proveyer
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS proveyers
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    @classmethod
    def instance_from_db(cls, row):
        proveyer = cls.all.get(row[0])
        if proveyer:
            proveyer.name = str(row[1])
            proveyer.cut_off_time = int(row[2])
            proveyer.order_min = int(row[3])
        else:
            proveyer = cls(str(row[1]), int(row[2]), int(row[3]))
            proveyer.id = row[0]
            cls.all[proveyer.id] = proveyer
        return proveyer
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM proveyers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM proveyers
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM proveyers
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO proveyers(name, cut_off_time, order_min)
            VALUES (?,?,?)
        """    
        CURSOR.execute(sql, (self.name, self.cut_off_time, self.order_min))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE proveyers
            SET name=?, cut_off_time=?, order_min=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.name, self.cut_off_time, self.order_min, self.id))
        CONN.commit()
        
    def delete(self):
        sql_PI_delete = """
            DELETE FROM proveyer_item
            WHERE proveyer_id = ?
        """
        sql_PC_delete = """
            DELETE FROM proveyer_catagories
            WHERE proveyer_id = ?
        """
        sql_P_delete = """
            DELETE FROM proveyers
            WHERE id=?
        """
        CURSOR.execute(sql_PI_delete, (self.id,))
        CURSOR.execute(sql_PC_delete, (self.id,))
        CURSOR.execute(sql_P_delete, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
        
    def load_related_proveyer_items(self):
        from models.proveyer_item import Proveyer_Item
        sql = """
            SELECT * 
            FROM proveyer_item
            WHERE proveyer_id=?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        self.proveyer_items=[Proveyer_Item.instance_from_db(row) for row in rows]
            
    def print_proveyer(self):
        from helpers import format_spacing_for_print
        print(f'|{format_spacing_for_print(self.name)}|{format_spacing_for_print(self.cut_off_time)}|{format_spacing_for_print(self.order_min)}|')
            
            
            