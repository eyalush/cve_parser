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
cur = db.cursor()

tree = ET.parse('D:\\Users\\Eyali\\Documents\\Work\\SecInsight\\GitHub\\secinsight\\nvdcve-2.0-2016.xml')

root = tree.getroot()

#for child in root:
 #   print(child.tag, child.attrib)

for entry in root.findtext('id'):
    product = entry.get('product')
    print(product)



        #  query = ("insert into threat (threat_key, threat_source_id, threat_id, threat_published_dt, threat_modified_dt, threat_weakness_id, threat_desc, threat_created_dt, threat_updated_dt) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(threat_key.numerator,threat_source_id,threat_id, threat_published_dt.isoformat(), threat_modified_dt.isoformat(), threat_weakness_id,threat_desc, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
#    print (query)
#    cur.execute(query)
  #  db.commit()
cur.close()
db.close()