import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Load environment variables
API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    dialect = data.get('dialect', 'egyptian_arabic')
    task = data.get('task')
    if not task:
        return jsonify({'error': 'No task provided'}), 400
    
    # Integrate with Google Gemini API
    response = requests.post('https://api.google.com/gemini/process', json={'dialect': dialect, 'task': task}, headers={'Authorization': f'Bearer {API_KEY}'})
    if response.status_code != 200:
        return jsonify({'error': 'Failed to process request', 'details': response.json()}), response.status_code
    
    return jsonify(response.json()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))