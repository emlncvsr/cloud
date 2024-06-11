function uploadFile() {
    const input = document.getElementById('fileInput');
    const file = input.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.downloadUrl) {
                document.getElementById('result').innerText = `File uploaded successfully. Download URL: ${data.downloadUrl}`;
            } else {
                document.getElementById('result').innerText = `Error: ${data.error}`;
            }
        })
        .catch(error => {
            document.getElementById('result').innerText = `Error: ${error}`;
        });
    } else {
        alert('Please select a file first.');
    }
}
