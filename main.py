from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

encoder_value = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update_data():
    global encoder_value
    try:
        data = request.get_json()
        if data and 'value' in data:
            encoder_value = int(data['value'])
            # ยิงข้อมูลออก WebSocket ทันทีที่ได้รับ POST จาก ESP32
            socketio.emit('update_encoder', {'value': encoder_value})
            return {"status": "success"}, 200
        return {"status": "error"}, 400
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)