from flask import  Flask, request, jsonify

app = Flask(__name__)

@app.route('/testapi')
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile_number")

    return "Testing GET API {} {}".format(get_name, mobile_number)

if __name__ == "__main__":
    app.run(port=5003)
