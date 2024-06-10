from flask import Flask, request, jsonify
import uplink
import os

app = Flask(__name__)

# Storj Configuration
STORJ_ACCESS_KEY = 'your-access-key'
STORJ_SECRET_KEY = 'your-secret-key'
STORJ_SATELLITE = 'your-satellite'
STORJ_BUCKET = 'your-bucket'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Initialize the Uplink client
        config = uplink.Config()
        config.set_satellite_address(STORJ_SATELLITE)
        config.set_api_key(STORJ_ACCESS_KEY)
        config.set_enc_access(STORJ_SECRET_KEY)
        
        client = uplink.Client(config)

        # Open project
        project = client.open_project()

        # Upload the file
        with project.upload(STORJ_BUCKET, file.filename) as upload:
            upload.write(file.stream.read())

        download_url = f'https://link.storjshare.io/{STORJ_BUCKET}/{file.filename}'
        return jsonify({'downloadUrl': download_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
