from flask import Flask, render_template, request, jsonify
from datetime import datetime
app = Flask(__name__)

alerts = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alerts.append(data)
    return jsonify({"message": "Alert added"}), 201

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)