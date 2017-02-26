#!/usr/bin/python
import pymysql

db = pymysql.connect(host="mydb-secinsight.cxtml2hqpnfr.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                     user="secinsight",         # your username
                     passwd="miGushatz1",  # your password
                     db="mydb_secinsight")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM cve")

wordsdict = {}

i = 0
# print all the first cell of all the rows
for row in cur.fetchall():
    # split the text
    words = row[2].split()
    print ("row " + str(i))
    i=i+1
    # for each word in the line:
    for word in words:
        if wordsdict.has_key(word.lower()):
            wordsdict[word.lower()] = (wordsdict[word.lower()]+1)
        else:
            wordsdict[word.lower()] = 1
        # print("==> " + word + " " + str(wordsdict[word.lower()]))

for word in wordsdict.items():
    print(word[0])
    try:
        cur.execute("INSERT INTO word_dict values ('" + word[0].replace("'", "") + "',"+str(word[1])+")")
    except:
        print ("error for word " + word[0])
        pass

db.close()