from models.__init__ import CURSOR, CONN

class Department:
    all = {}
    
    def __init__(self, name):
        self.name = name
        self.department_pars = []
    
    def __repr__(self):
        return f"Department {self.id}: {self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not valid.')
 
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name):
        department = cls(str(name))
        department.save()
        return department
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = str(row[1])    
        else:
            department = cls(str(row[1]))
            department.id = row[0]
            cls.all[department.id] = department
        return department
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM departments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM departments
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO departments(name)
            VALUES (?)
        """    
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE departments
            SET name=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
        
    def delete(self):
        sql_DP_delete = """
            DELETE FROM par_departments
            WHERE id=?
        """
        sql = """
            DELETE FROM departments
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CURSOR.execute(sql_DP_delete, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       