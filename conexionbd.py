from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'cursophp.com.ar'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fullstack'
app.config['MYSQL_DB'] = 'cvgimenez'
mysql = MySQL(app)


		

@app.route('/nuevo', methods=['POST'])	
@cross_origin()	
def nuevo():
		if request.method == 'POST':
			request_data = request.get_json()
			nombre = request_data['nombre']
			email =request_data['email']
			mensaje=request_data['mensaje']
			cur = mysql.connection.cursor()
			cur.execute('INSERT INTO mensajes (nombre,email,mensaje) VALUES (%s, %s, %s)', (nombre,email,mensaje) )			
			mysql.connection.commit()
			return "Guardado OK"
					
			
if __name__	== '__main__':
			app.run(port=4000, debug=True)
			
