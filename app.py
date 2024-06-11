from flask import Flask, request, jsonify, render_template
from flask_frozen import Freezer
import os
import requests
from tenacity import retry, wait_fixed, stop_after_attempt

app = Flask(__name__)
freezer = Freezer(app)

# Add a configuration flag to indicate freezing
app.config['IS_FREEZING'] = os.getenv('IS_FREEZING', 'False') == 'True'

# pCloud Configuration
PCLOUD_EMAIL = os.getenv('PCLOUD_EMAIL')
PCLOUD_PASSWORD = os.getenv('PCLOUD_PASSWORD')

@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
def get_auth_token():
    login_url = 'https://api.pcloud.com/login'
    login_data = {
        'username': PCLOUD_EMAIL,
        'password': PCLOUD_PASSWORD
    }
    response = requests.post(login_url, data=login_data)
    response.raise_for_status()
    response_data = response.json()
    print(f"Login response: {response_data}")
    if 'auth' in response_data:
        return response_data['auth']
    else:
        raise KeyError("'auth' key not found in the response")

# Initialize auth_token
auth_token = None

@app.before_first_request
def initialize_auth_token():
    global auth_token
    if not app.config['IS_FREEZING']:
        auth_token = get_auth_token()
    else:
        auth_token = 'mocked_auth_token'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Upload the file to pCloud
        upload_url = 'https://api.pcloud.com/uploadfile'
        files = {
            'file': (file.filename, file.stream, file.mimetype)
        }
        params = {
            'auth': auth_token,
            'folderid': 0  # Root folder
        }
        response = requests.post(upload_url, files=files, params=params)
        response.raise_for_status()
        download_url = response.json()['metadata'][0]['downloadlink']
        return jsonify({'downloadUrl': download_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
