from flask import Flask, request, jsonify
import pymongo as mb

app = Flask(__name__)
client = mb.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")

database = client['apitest']
collection = database['apicollection']

@app.route('/insert/mongo', methods = ['POST'])
def insert():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("successfully inserted"))

if __name__ == "__main__":
    app.run(port = 5001)