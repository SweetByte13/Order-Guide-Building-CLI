from models.__init__ import CURSOR, CONN

class Par:

    all = {}
    
    def __init__(self, name, par_amount, stock):
        self.name = name
        self.stock = stock
        self.par_amount = par_amount
        self.items = []
        self.department_pars = []

        
    def __repr__(self):
        return f"Par {self.id}: {self.name}, {self.par_amount}, {self.stock}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not valid, Par must have a name')
        
    @property
    def par_amount(self):
        return self._par_amount
    
    @par_amount.setter
    def par_amount(self, new_par_amount):
        if isinstance (new_par_amount, int):
            self._par_amount = new_par_amount
        else:
            raise TypeError(f'{new_par_amount} is not a valid, Par must have a par amount')    

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, new_stock):
        if isinstance (new_stock, int):
            self._stock = new_stock
        else:
            raise TypeError(f'{new_stock} is not valid, Par must have a stock amount')

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pars (
            id INTEGER PRIMARY KEY,
            name TEXT,
            par_amount INTEGER,
            stock INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, stock, par_amount):
        par = cls(str(name), int(par_amount), int(stock))
        par.save()
        return par
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pars
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        par = cls.all.get(row[0])
        if par:
            par.name=str(row[1])
            par.par_amount=int(row[2])
            par.stock=int(row[3])
            
        else:
            par = cls(str(row[1]), int(row[2]), int(row[3]))
            par.id = row[0]
            cls.all[par.id] = par
        return par
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM pars
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pars
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM pars
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO pars (name, par_amount, stock)
            VALUES (?,?,?)
        """    
        CURSOR.execute(sql, (self.name, self.par_amount, self.stock))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE pars
            SET name=?, stock=?, par_amount=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.name, self.stock, self.par_amount, self.id))
        CONN.commit()
        
    def delete(self):
        sql_PD_delete = """
            DELETE FROM par_departments
            WHERE id=?
        """
        sql_I_delete = """
            DELETE FROM items
            WHERE id=?
        """
        sql = """
            DELETE FROM pars
            WHERE id=?
        """
        CURSOR.execute(sql_PD_delete, (self.id,))
        CURSOR.execute(sql_I_delete, (self.id,))
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       
    def load_related_items(self):
        from models.item import Item
        sql = """
            SELECT * 
            FROM items
            WHERE par_id=?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        self.items=[Item.instance_from_db(row) for row in rows]