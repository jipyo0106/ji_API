from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return {"result" : "index_connection_success"}

@app.route('/test', methods=['POST'])
def test():
    return {"result" : "test_connection_success"}

@app.route('/print<print_str>/<int:num>', methods=['POST'])
def test_print(print_str, num):
    return {"result" : f"{print_str} - {num}"}

app.run(host='0.0.0.0', port='8080', debug=True)