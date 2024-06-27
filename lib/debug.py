#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.proveyer import Proveyer
from models.proveyer_item import Proveyer_Item

p1=Proveyer(id=1,name='Baldor', catagory='Produce', cut_off_time=1900, order_min=150)
p2=Proveyer(id=2, name='Dairyland', catagory='Dairy', cut_off_time=1630, order_min=200)
p3=Proveyer(id=3,name='LaFrieda', catagory='Meat', cut_off_time=2100, order_min=180)
p4=Proveyer(id=4,name='Congressional', catagory='Fish', cut_off_time=2100, order_min=150)

# pi1=Proveyer_Item(proveyer_id=1, price=12, case_size=6)
# pi2=Proveyer_Item(proveyer_id=2, price=23, case_size=4)
# pi3=Proveyer_Item(proveyer_id=3, price=24, case_size=1)
# pi4=Proveyer_Item(proveyer_id=1, price=18, case_size=2)
# pi5=Proveyer_Item(proveyer_id=4, price=15, case_size=1)

ipdb.set_trace()
