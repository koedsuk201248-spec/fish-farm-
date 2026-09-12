import os
from flask import Flask, request, render_template

app = Flask(__name__)
latest_message = "ยังไม่มีข้อมูลจาก ESP32"

@app.route('/')
def index():
    return render_template('index.html', message=latest_message)

@app.route('/api/data', methods=['POST'])
def receive_data():
    global latest_message
    latest_message = request.data.decode('utf-8')
    print(f"ได้รับข้อความ: {latest_message}")
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)