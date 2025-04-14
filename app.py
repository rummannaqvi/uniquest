from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "UniQuest Backend is running!"

@app.route('/dummy', methods=['POST'])
def dummy():
    data = request.json
    return jsonify({"message": "Received!", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
