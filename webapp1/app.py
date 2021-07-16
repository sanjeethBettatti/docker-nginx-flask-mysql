import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()
  cursor.execute("select @@version")
  res = cursor.fetchall()
  cursor.close()

  return "Database version: "+str(res[0][0])+" from app1"

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
