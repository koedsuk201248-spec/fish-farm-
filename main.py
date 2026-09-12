from flask import Flask, request, render_template

app = Flask(__name__)

# ตัวแปรเก็บข้อมูลล่าสุดจาก ESP32
latest_data = "ยังไม่มีข้อมูลจาก ESP32"

@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_data
    if request.method == 'POST':
        # รับข้อมูลที่ ESP32 ส่งมา
        latest_data = request.data.decode('utf-8')
        return "OK", 200
    
    # ถ้าเป็น GET ให้แสดงผลหน้าเว็บปกติ
    return render_template('index.html', data=latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)