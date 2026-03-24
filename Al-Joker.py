from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "نظام الجوكر يعمل بنجاح.. العقل متصل"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    return jsonify({"reply": f"الجوكر: تم استلام أمرك '{user_msg}' وجاري التنفيذ يا عبد الله."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
