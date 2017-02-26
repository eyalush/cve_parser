import xml.etree.ElementTree as ET
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
for entry in tree.iter(xmlprefix + 'entry'):
    cveid = entry.get('id')
    print cveid
    for entryitem in entry.iter():
        if (str.find(entryitem.tag, 'vulnerable-configuration')>0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'vulnerable-software-list') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'cve-id') > 0):
            print '\t', entryitem.tag, entryitem.text
        if (str.find(entryitem.tag, 'published-datetime') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'last-modified-datetime') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'cvss') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'cwe') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'references') > 0):
            print '\t', entryitem.tag, entryitem.attrib
        if (str.find(entryitem.tag, 'summary') > 0):
            print '\t', entryitem.tag, entryitem.attrib
#for entry in root.findall('entry'):
#    for note in entry.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}Notes').findall('{http://www.icasi.org/CVRF/schema/vuln/1.1}Note'):
#        print note.text
#    print entry.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}Title').text