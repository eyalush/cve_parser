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

xmlprefix = '{http://scap.nist.gov/schema/feed/vulnerability/2.0}'

# Get last treat_key for sequence
query_threat_key =  ("select max(threat_key) from threat")
print(query_threat_key)
threat_key = cur.execute(query_threat_key)
print(threat_key)
if (query_threat_key is ''):
    threat_key =0
threat_source_id = 1

for entry in tree.iter(xmlprefix + 'entry'):
    threat_id = entry.get('id')
    cwe = ''
    threat_published_dt = datetime.datetime.now()
    threat_modified_dt = datetime.datetime.now()
    threat_desc = ''
    for entryitem in entry.iter():
        if (str.find(entryitem.tag, 'vulnerable-configuration')>0):
            threat_key = threat_key + 1
            print('\t', threat_key, entryitem.attrib)
            print('\t', threat_source_id, entryitem.attrib)
            print ('\t', entryitem.tag, entryitem.attrib)
        if (str.find(entryitem.tag, 'vulnerable-software-list') > 0):
            print ('\t', entryitem.tag, entryitem.attrib)
        if (str.find(entryitem.tag, 'cve-id') > 0):
            threat_id = entryitem.text
        if (str.find(entryitem.tag, 'published-datetime') > 0):
            threat_published_dt = datetime.datetime.strptime(re.sub(r"[+-][0-9][0-9]:[0-9][0-9]", "", entryitem.text), '%Y-%m-%dT%H:%M:%S.%f')
        if (str.find(entryitem.tag, 'last-modified-datetime') > 0):
            threat_modified_dt = datetime.datetime.strptime(re.sub(r"[+-][0-9][0-9]:[0-9][0-9]", "", entryitem.text), '%Y-%m-%dT%H:%M:%S.%f')
        if (str.find(entryitem.tag, 'cvss') > 0):
            print ('\t', entryitem.tag, entryitem.attrib)
        if (str.find(entryitem.tag, 'cwe') > 0):
            threat_weakness_id = entryitem.get('id')
            print ('\t', threat_weakness_id, entryitem.attrib)
        if (str.find(entryitem.tag, 'references') > 0):
            print ('\t', entryitem.tag, entryitem.attrib)
        if (str.find(entryitem.tag, 'summary') > 0):
            threat_desc = entryitem.text
            threat_desc= threat_desc.replace( "'", "''''")
            print(threat_desc)

    query = ("insert into threat (threat_key, threat_source_id, threat_id, threat_published_dt, threat_modified_dt, threat_weakness_id, threat_desc, threat_created_dt, threat_updated_dt) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(threat_key.numerator,threat_source_id,threat_id, threat_published_dt.isoformat(), threat_modified_dt.isoformat(), threat_weakness_id,threat_desc, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
    print (query)
    cur.execute(query)
    db.commit()
cur.close()
db.close()