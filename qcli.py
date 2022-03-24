import mysql.connector

Q_S2L = "SELECT v_stations.sid, v_lines.lname FROM v_stations JOIN v_sline JOIN v_lines "\
        " ON (v_stations.sid = v_sline.sid AND v_sline.lid = v_lines.lid)" \
        " WHERE  v_stations.sname = %s"

Q_L2S = "SELECT v_lines.lid, v_stations.sname FROM v_stations JOIN v_sline JOIN v_lines "\
        " ON (v_stations.sid = v_sline.sid AND v_sline.lid = v_lines.lid) "\
        " WHERE  v_lines.lname = %s ORDER BY v_sline.pos"


def query_s2l(cursor, sname):
    cursor.execute(Q_S2L, (sname,))
    r_dict = {}
    for r in cursor:
        if r[0] not in r_dict:
            r_dict[r[0]] = []
        r_dict[r[0]].append(r[1])
    return r_dict

def query_l2s(cursor, lname):
    cursor.execute(Q_L2S, (lname,))
    r_dict = {}
    for r in cursor:
        if r[0] not in r_dict:
            r_dict[r[0]] = []
        r_dict[r[0]].append(r[1])
    return r_dict




connection = None
cursor = None
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='vaticletest_db',
                                         user='vaticletest_user',
                                         password='password')

    cursor = connection.cursor(prepared=True)

    print(">", end=""); inline = input()
    while inline:    
        # inline = "line:Circle" # "station:" # 
        # inline = "station:Victoria"
        
        qline = inline.split(':')

        if qline[0] == "station":
            res = query_s2l(cursor, qline[1])
            for rid in res:
                print("%s: %s:\n\t%s"% (rid, qline[1], "\n\t".join(res[rid])) )
        elif qline[0] == "line":
            res = query_l2s(cursor, qline[1])
            for rid in res:
                print("%s: %s:\n\t%s"% (rid, qline[1], "\n\t".join(res[rid])) )
        else:
            print("Bad query. [station|line]:<name>")
        print(">", end=""); inline = input()

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection is not None and connection.is_connected():
        if cursor is not None:
            cursor.close()
        connection.close()
        print("MySQL connection is closed")

