import mysql.connector

def mysql_connector():
	my_conf = {
				"host" : "192.168.220.141",
				'port' : "3306",
				'user' : "YATE",
				'password': 'Testing123#',
				'database': "mohit",
			  }
	cnx = mysql.connector.connect(**my_conf)
	return cnx