from flask import Flask, request, render_template

app = Flask(__name__)

# ตัวแปรเก็บข้อมูลล่าสุดจาก ESP32
latest_data = "ยังไม่มีข้อมูลจาก ESP32"

@app.route('/', methods=['GET'])
def index():
    global latest_data
    # ถ้าเปิดหน้าเว็บดูปกติ จะแสดงผลข้อมูลล่าสุด
    return render_template('index.html', data=latest_data)

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    # รับข้อมูลที่ ESP32 ส่งเข้ามาทาง /update
    if request.data:
        latest_data = request.data.decode('utf-8')
    elif request.form:
        latest_data = list(request.form.keys())[0]
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)