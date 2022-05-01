#from ..core import DB
#from database.migrations import DB
from sys import path
import os

migrations_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'migrations')))
core_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))

path.append(migrations_dir)
path.append(core_dir)

#print(core_dir)
#print(migrations_dir)
import create_table_20220501
#from py_server.database.migrations import create_table_20220501
#from database import DB
from core import DB
print(create_table_20220501.up_query)
print(DB)
#def run():
#    DB.execute(create_table_20220501.up_query)

#def down():

