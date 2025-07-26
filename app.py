from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from stream import start_stream, stop_stream

app = Flask(__name__)
UPLOAD_FOLDER = "uploaded_videos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

stream_process = None

# 🔐 Login Page
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'arshit raj' and password == 'Rajnandni2310':
            return redirect('/dashboard')
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

# 🧭 Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 📤 Upload Video
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file sent"}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"message": "Uploaded", "path": filepath}), 200

# ▶️ Start Stream
@app.route('/start')
def start():
    global stream_process
    if stream_process:
        return jsonify({"error": "Already running"}), 400
    stream_process = start_stream()
    return jsonify({"message": "Stream started"}), 200

# ⏹ Stop Stream
@app.route('/stop')
def stop():
    global stream_process
    if not stream_process:
        return jsonify({"error": "No active stream"}), 400
    stop_stream(stream_process)
    stream_process = None
    return jsonify({"message": "Stream stopped"}), 200

if __name__ == '__main__':
    app.run(debug=True)
