from flask import Flask, request, jsonify, render_template
from flask_frozen import Freezer
import os
import pcloud

app = Flask(__name__)
freezer = Freezer(app)

# pCloud Configuration
PCLOUD_EMAIL = os.getenv('PCLOUD_EMAIL')
PCLOUD_PASSWORD = os.getenv('PCLOUD_PASSWORD')

client = pcloud.PyCloud(PCLOUD_EMAIL, PCLOUD_PASSWORD)

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
        response = client.uploadfile(file, path='/')
        download_url = response.get('download')
        return jsonify({'downloadUrl': download_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
