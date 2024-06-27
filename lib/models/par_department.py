from models.__init__ import CURSOR, CONN

class Par_Department:
    all = {}
    
    def __init__(self, par_id, department_id):
        self.par_id = par_id
        self.department_id = department_id
        self.par = None
        self.department = None
        
    def __repr__(self):
        return f"Par-Department {self.id}:{self.par_id}, {self.department_id}"

    @property
    def par_id(self):
        return self._par_id
    
    @par_id.setter
    def par_id(self, new_par_id):
        if isinstance (new_par_id, int):
            self._par_id = new_par_id
        else:
            raise TypeError(f'{new_par_id} is not a valid par ID, Par-Department must have a par ID')
        
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, new_department_id):
        if isinstance (new_department_id, int):
            self._department_id = new_department_id
        else:
            raise TypeError(f'{new_department_id} is not a valid department ID,  Par-Department must have a department ID')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS par_departments (
            id INTEGER PRIMARY KEY,
            par_id INTEGER,
            department_id INTEGER,
            FOREIGN KEY (par_id) REFERENCES par(id),
            FOREIGN KEY (department_id) REFERENCES department(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, par_id, department_id):
        par_department = cls(int(par_id), int(department_id))
        par_department.save()
        return par_department
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS par_departments
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        par_department = cls.all.get(row[0])
        if par_department:
            par_department.par_id = int(row[1])
            par_department.department_id = int(row[2])
            
        else:
            par_department = cls(int(row[1]), int(row[2]))
            par_department.id = row[0]
            cls.all[par_department.id] = par_department
        return par_department
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM par_departments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM par_departments
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO par_departments(par_id, department_id)
            VALUES (?,?)
        """    
        CURSOR.execute(sql, (self.par_id, self.department_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE par_department
            SET par_id=?, department_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM par_department
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       