from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def get_health():
    return jsonify({"healthy": "yes"}), 200

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    msg = data.get('message')

    return jsonify({"reply": msg}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
