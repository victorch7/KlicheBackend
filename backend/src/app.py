from flask import Flask, request, redirect, json, jsonify, render_template
import os
from flask_mysqldb import MySQL #Se importa la libreria para trabajar con mysql
#from database.db_config import MYSQL #Se importa la configuracion para trabajar con la BD

#Nombre aplicacion
app = Flask(__name__)

#Confiuracion de bd
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'klichedb'
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"
#app.config['MYSQL_URI'] = 'mysql://root@localhost:3306/klichedb'
con = MySQL(app)

#Metodos para crud productos (por el momento)
@app.route('/createProducto', methods=['POST'])
def crearProducto():
    pass

@app.route('/lisProducts', methods=['GET'])
def listarProductos():
    pass

@app.route('/listProduct/<id>', methods=['GET']) #Retorna un solo producto
def listarProducto(id):
    pass

@app.route('/editProduct/<id>', methods=['PUT'])
def editarProducto(id):
    pass

@app.route('/deleteProduct/<id>', methods=['DELETE'])
def eliminarProducto(id):
    pass

#Ruta de prueba
@app.route('/')
def prueba():
    return "Hola"

#Ruta de prueba BD
@app.route('/index')
def indexbd():
    with app.app_context():
        cur = con.connection.cursor()
        cur.execute("SELECT * FROM productos")
        results = cur.fetchall()
        cur.close()
        return render_template('index.html', data=results)

# @app.teardown_request
# def close_db(error=None):
#     if hasattr(con, 'connection'):
#         con.connection.close()

#Ruta de manejo de errores
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)