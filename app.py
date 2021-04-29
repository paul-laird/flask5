from flask import Flask
from flask import request
import pypyodbc
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
with open('.pw') as f:
  password=f.read()
connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
  'Server=pauldb.dbsprojects.ie;'
  'Database=student;'
  'encrypt=yes;'
  'TrustServerCertificate=yes;'
  'UID=sa;'
  'PWD='+password,autocommit = True)

@app.route("/add") #Add Student
def add():
  name = request.args.get('name')
  email = request.args.get('email')
  cur = connection.cursor() #create a connection to the SQL instance
  cursor.execute("{call uspInsertStudent(name, email)}")
  return '{"Result":"Success"}'

@app.route("/") #Default - Show Data
def hello(): # Name of the method
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM students''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['Name']=row[0].replace('\n',' ')
    Result['Email']=row[1]
    Result['ID']=row[2]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
