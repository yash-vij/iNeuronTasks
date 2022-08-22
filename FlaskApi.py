from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd="0000")
cursor = mydb.cursor()
cursor.execute("create database if not exists APItest")
cursor.execute("create table if not exists APItest.table1 (id int, name varchar(30))")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        id = request.json['id']
        name = request.json['name']
        cursor.execute("insert into APItest.table1 values(%s , %s)", (id, name))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.json['id']
        name = request.json['name']
        cursor.execute("update APItest.table1 set name = (%s) where id = (%s) ",(name,id))
        mydb.commit()
        return jsonify(str('succesfully inserted'))


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.json['id']
        cursor.execute("delete from APItest.table1 where id = (%s)", (id,))
        mydb.commit()
        return jsonify(str('succesfully deleted'))

if __name__ == '__main__':
    app.run()

