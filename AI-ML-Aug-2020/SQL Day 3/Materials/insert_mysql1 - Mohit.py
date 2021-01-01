import connect1
import traceback
def mysqlops(q1, data):
	try :
		db_cnx = connect1.mysql_connector()
		mycursor = db_cnx.cursor()
		mycursor.executemany(q1, data)
		db_cnx.commit()
		print ("Done")
	except Exception as e :
		print (e)
		print (traceback.print_tb(e.__traceback__))
		
	finally :
		mycursor.close()
		db_cnx.close()

		
if __name__ == "__main__":
	
	data = [(1,"31-12-2020"),(2,"31-12-2020"),(3,"31-12-2020"),(5,"31-12-2020")]
	
	q1 = "insert into attendance2 (roll_number, date1) values(%s, %s)"
	print (q1)
	mysqlops(q1, data)