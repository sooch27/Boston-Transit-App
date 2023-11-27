import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( record_num, id, longitude, latitude, current_status, current_stop_sequence, occupancy_status, direction_id, updated_at) values (%s, %s,%s, %s, %s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['label'], mbtaDict['longitude'])
        mycursor.execute(sql, val)

    mydb.commit()