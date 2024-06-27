#!/usr/bin/env python3
from models.__init__ import CONN, CURSOR
from models.proveyer import Proveyer
from models.proveyer_item import Proveyer_Item
from models.par import Par
from models.item import Item
from models.par_department import Par_Department
from models.department import Department
from models.proveyer_catagory import Proveyer_Catagory
from models.catagory import Catagory

def seed_database():
    Proveyer.drop_table()
    Proveyer_Item.drop_table()
    Par.drop_table()
    Par_Department.drop_table()
    Department.drop_table()
    Item.drop_table()
    Proveyer_Catagory.drop_table()
    Catagory.drop_table()
    
    Proveyer.create_table()
    Proveyer_Item.create_table()
    Par.create_table()
    Par_Department.create_table()
    Department.create_table()
    Item.create_table()
    Proveyer_Catagory.create_table()
    Catagory.create_table()

    Proveyer.create('Baldor', 1900, 150)
    Proveyer.create("Dairyland", 1630, 200)
    Proveyer.create("LaFrieda", 2100, 180)
    Proveyer.create("Congressional", 2100, 150)
    Proveyer.create("Sysco", 1600, 100)
    
    Proveyer_Item.create("Tomatoes",4, 1, 10, 4)
    Proveyer_Item.create("Apples",3,  1, 23, 50)
    Proveyer_Item.create("Butter",5,  2,34, 24)
    Proveyer_Item.create("Lard",2, 3, 25, 1)
    Proveyer_Item.create("Honey",1, 5, 18, 1)
    Proveyer_Item.create("Salmon",6, 4, 32, 2)
    
    Catagory.create("Produce")
    Catagory.create("Dairy")
    Catagory.create("Meat")
    Catagory.create("Dry Goods")
    Catagory.create("Fish")
    
    Proveyer_Catagory.create(1, 1)  
    Proveyer_Catagory.create(2, 1)
    Proveyer_Catagory.create(2, 2)
    Proveyer_Catagory.create(3, 3)
    Proveyer_Catagory.create(4,5)
    Proveyer_Catagory.create(6,4)
    Proveyer_Catagory.create(1,4)
     
    Par.create("Tomatoes", 12, 8)
    Par.create("Apples", 45, 8)
    Par.create("Butter", 8, 10)
    Par.create("Lard", 2, 1)
    Par.create("Honey", 1, 1)
    Par.create("Salmon", 3, 1)
    
    Par_Department.create(1, 1)
    Par_Department.create(2, 1)
    Par_Department.create(3, 2)
    Par_Department.create(4, 3)
    Par_Department.create(1, 2)
    Par_Department.create(6, 1)

    Department.create("Kitchen")
    Department.create("Bar")
    Department.create("Pastry")
    Department.create("Kitchen")
    
    Item.create("Honey", 5, 4)
    Item.create("Lard", 4, 3)
    Item.create("Apples", 2, 1)
    Item.create("Tomatoes", 1, 1)
    Item.create("Butter", 3, 2)
    Item.create("Salmon", 6, 5)
    
seed_database()
print("Seeded database")