import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load environment variables
API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
BACKEND_URL = os.getenv('BACKEND_URL', 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests from the frontend"""
    try:
        data = request.json
        message = data.get('message')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Call Google Gemini API
        headers = {
            'Content-Type': 'application/json',
            'x-goog-api-key': API_KEY
        }
        
        payload = {
            'contents': [
                {
                    'parts': [
                        {'text': message}
                    ]
                }
            ]
        }
        
        response = requests.post(BACKEND_URL, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            reply = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No response')
            return jsonify({'reply': reply}), 200
        else:
            return jsonify({
                'error': 'Failed to get response from AI',
                'details': response.text
            }), response.status_code
            
    except requests.Timeout:
        return jsonify({'error': 'Request timeout - API took too long to respond'}), 504
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/process', methods=['POST'])
def process_request():
    """Process requests with dialect support"""
    try:
        data = request.json
        dialect = data.get('dialect', 'egyptian_arabic')
        task = data.get('task')
        
        if not task:
            return jsonify({'error': 'No task provided'}), 400
        
        # Add dialect context to the message
        full_message = f"[Dialect: {dialect}] {task}"
        
        headers = {
            'Content-Type': 'application/json',
            'x-goog-api-key': API_KEY
        }
        
        payload = {
            'contents': [
                {
                    'parts': [
                        {'text': full_message}
                    ]
                }
            ]
        }
        
        response = requests.post(BACKEND_URL, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({
                'error': 'Failed to process request',
                'details': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Joker API is running'}), 200

if __name__ == '__main__':
    # Check if API key is set
    if not API_KEY:
        print('⚠️  WARNING: GOOGLE_GEMINI_API_KEY is not set!')
        print('Please set the API key in your .env file')
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'
    
    print(f'🚀 Starting Joker API on http://0.0.0.0:{port}')
    print(f'🔑 API Key configured: {bool(API_KEY)}')
    
    app.run(host='0.0.0.0', port=port, debug=debug)
