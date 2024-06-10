from flask import Flask, request, jsonify, render_template
from flask_frozen import Freezer
import os
import requests
from tenacity import retry, wait_fixed, stop_after_attempt

app = Flask(__name__)
freezer = Freezer(app)

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
    return response.json()['auth']

auth_token = get_auth_token()

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
    app.run(debug=True)
