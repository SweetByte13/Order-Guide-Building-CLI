from models.__init__ import CURSOR, CONN

class Proveyer_Catagory:
    all = {}
    
    def __init__(self,proveyer_id, catagory_id):
        self.proveyer_id = proveyer_id
        self.catagory_id = catagory_id
        self.proveyer = None
        self.catagory = None
        
    def __repr__(self):
        return f"Proveyer-Catagory {self.id}:{self.proveyer_id}, {self.catagory_id}"
    
    @property
    def proveyer_id(self):
        return self._proveyer_id
    
    @proveyer_id.setter
    def proveyer_id(self, new_proveyer_id):
        if isinstance (new_proveyer_id, int):
            self._proveyer_id = new_proveyer_id
        else:
            raise TypeError(f'{new_proveyer_id} is not a valid ID, must have a proveyer ID')
        
    @property
    def catagory_id(self):
        return self._catagory_id
    
    @catagory_id.setter
    def catagory_id(self, new_catagory_id):
        if isinstance (new_catagory_id, int):
            self._catagory_id = new_catagory_id
        else:
            raise TypeError(f'{new_catagory_id} is not a valid ID, must have a catagory ID')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS proveyer_catagories (
            id INTEGER PRIMARY KEY,
            proveyer_id INTEGER,
            catagory_id INTEGER,
            FOREIGN KEY (proveyer_id) REFERENCES proveyer(id),
            FOREIGN KEY (catagory_id) REFERENCES catagory(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, proveyer_id, catagory_id):
        proveyer_catagory = cls(int(proveyer_id), int(catagory_id))
        proveyer_catagory.save()
        return proveyer_catagory
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS proveyer_catagories
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        proveyer_catagory = cls.all.get(row[0])
        if proveyer_catagory:
            proveyer_catagory.proveyer_id = row[1]
            proveyer_catagory.catagory_id = row[2]
            
        else:
            proveyer_catagory = cls(int(row[1]), int(row[2]))
            proveyer_catagory.id = row[0]
            cls.all[proveyer_catagory.id] = proveyer_catagory
        return proveyer_catagory
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM proveyer_catagories
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
   
    def save(self):
        sql = """
            INSERT INTO proveyer_catagories(proveyer_id, catagory_id)
            VALUES (?,?)
        """    
        CURSOR.execute(sql, (self.proveyer_id, self.catagory_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE proveyer_catagories
            SET proveyer_id=?, catagory_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM proveyer_catagories
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       