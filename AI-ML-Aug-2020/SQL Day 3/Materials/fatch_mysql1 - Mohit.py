import connect1
def mysqlops(q1):
	try :
		db_cnx = connect1.mysql_connector()
		mycursor = db_cnx.cursor()
		mycursor.execute(q1)
		print ("doing...")
		rows = mycursor.fetchall()
		print (rows)
		for each in rows:
			print (each)
		print ("Done")
	except Exception as e :
		print (e)
		
	finally :
		mycursor.close()
		db_cnx.close()

		
if __name__ == "__main__":
	table = input("Enter the table name ")
	d1 = input("Enter the date ")
	d1 = repr(d1)
	q1 = f"select * from {table} where date1 = {d1}"
	print (q1)
	mysqlops(q1)