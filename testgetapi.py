from flask import  Flask, request, jsonify

app = Flask(__name__)

@app.route('/testapi')
def test():
    get_name = request.args.get("name") #name is it is getting from browser
    mobile_number = request.args.get("number")

    return "Testing GET API {} {}".format(mobile_number,get_name)

if __name__ == "__main__":
    app.run(port=5003)
