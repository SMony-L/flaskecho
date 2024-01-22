from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def main():
    return "Hello from Flask Echo Server"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
