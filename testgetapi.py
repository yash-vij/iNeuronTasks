from flask import  Flask, request, jsonify

app = Flask(__name__)

@app.route('/testapi')
def test():
    get_name = request.args.get("get_name")
    return "Testing GET API {}".format(get_name)

if __name__ == "__main__":
    app.run(port=5003)
