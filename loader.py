#!/usr/bin/python
import mysql.connector
import json
connection = None
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='vaticletest_db',
                                         user='vaticletest_user',
                                         password='password')

    # Parameterized query

    with open("train-network.json") as f:
        all_data = json.load(f)

    # print([k for k in all_data])

    if True:
        q = "INSERT INTO v_stations (sid, sname, lati, longi) VALUES (%s, %s, %s, %s ) "
        cursor = connection.cursor(prepared=True)
        for sdata in all_data['stations']:
            # print(sdata)
            cursor.execute(q, (sdata['id'], sdata['name'], sdata['latitude'], sdata['longitude']))
            print
        connection.commit()
    if True:
        i = 0
        q1 = "INSERT INTO v_lines (lid, lname) VALUES (%s, %s) "
        q2 = "INSERT INTO v_sline (lid, pos, sid) VALUES (%s, %s, %s) "
        cursor = connection.cursor(prepared=True)
        for ldata in all_data['lines']:
            i+=1
            cursor.execute(q1, (i, ldata['name']))
            pos = 0
            for station in ldata['stations']:
                pos += 1
                cursor.execute(q2, (i, pos, station))
        connection.commit()


    print("Success!")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

