from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ตัวแปรสำหรับเก็บค่า Rotary Encoder ล่าสุด
encoder_data = {"value": 0}

@app.route('/')
def index():
    return render_template('index.html')

# เพิ่ม route รองรับทั้ง /update และ /
@app.route('/update', methods=['POST', 'GET'])
def update_data():
    global encoder_data
    try:
        data = request.get_json()
        if data and 'value' in data:
            encoder_data['value'] = data['value']
            return jsonify({"status": "success", "value": encoder_data['value']}), 200
        return jsonify({"status": "error", "message": "Invalid format"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(encoder_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)