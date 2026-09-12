from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ตัวแปรเก็บค่าล่าสุด
latest_data = "ยังไม่มีข้อมูล"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    # รับข้อมูลแบบ Plain Text ที่ ESP32 ส่งมา
    data = request.data.decode('utf-8')
    if data:
        latest_data = data
        return "OK", 200
    return "No data", 400

@app.route('/get_data')
def get_data():
    # ส่งค่าล่าสุดกลับไปให้หน้าเว็บในรูปแบบ JSON
    return jsonify({'status': latest_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)