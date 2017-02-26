import csv
import pymysql

db = pymysql.connect(host="mydb-secinsight.cxtml2hqpnfr.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                     user="secinsight",         # your username
                     passwd="miGushatz1",  # your password
                     db="mydb_secinsight")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Get last treat_key for sequence
query_threat_key =  ("select max(threat_weakness_key) from threat_weakness")
print(query_threat_key)
threat_weakness_key = cur.execute(query_threat_key)
print(threat_weakness_key)



with open('D:\\Users\\Eyali\\Documents\\Work\\SecInsight\\GitHub\\secinsight\\CWE_weakness.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        threat_weakness_key = threat_weakness_key.numerator+1
        print(threat_weakness_key)
        threat_weakness_name=row['Name']
        threat_weakness_name = threat_weakness_name.replace("'", "''''")
        threat_desc = row['Description']
        threat_desc = threat_desc.replace("'", "''''")

        query =  ("INSERT INTO threat_weakness(threat_weakness_key,threat_weakness_id,threat_weakness_name,threat_weakness_desc) VALUES (")
        query += "'" + threat_weakness_key.__str__() + "', "
        query += "'" + row['CWE-ID'] + "', "
        query += "'" + threat_weakness_name + "', "
        query += "'" + threat_desc + "')"

        #query += """'""" + threat_desc + """')"""""
        print (query)
        cur.execute(query)
        db.commit()
cur.close()
db.close()


#for row in csv_data:
#    query = cur.execute("INSERT INTO threat_weakness(threat_weakness_key,threat_weakness_name,threat_weakness_id,threat_weakness_desc)VALUES('1',%s, %s, %s)", row)
#close the connection to the database.
#db.commit()
#print ('Done')