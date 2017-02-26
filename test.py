import xml.etree.ElementTree as ET
import re
import datetime
import pymysql

db = pymysql.connect(host="mydb-secinsight.cxtml2hqpnfr.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                     user="secinsight",         # your username
                     passwd="miGushatz1",  # your password
                     db="mydb_secinsight")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
#cur = db.cursor()

tree = ET.parse('D:\\Users\\Eyali\\Documents\\Work\\SecInsight\\GitHub\\secinsight\\nvdcve-2.0-2016.xml')

def find_in_tree(tree, id):
    found = tree.find(id)
    if found == 'id':
        print "No %s in file" % entry
        found = []
    return found

