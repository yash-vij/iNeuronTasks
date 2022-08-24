from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route('/getDatabaseData')
def test():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try :
        mydb = conn.connect(host="localhost", user='root', passwd="0000", database = db)
        cursor = mydb.cursor()
        cursor.execute(f'select * from {tn}')
        data = cursor.fetchall()
        mydb.commit()
        mydb.close()

    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5004)

