async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file.');
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('downloadLink').value = data.downloadUrl;
        document.getElementById('linkContainer').style.display = 'block';
    } else {
        alert('Failed to upload file.');
    }
}

function copyLink() {
    const downloadLink = document.getElementById('downloadLink');
    downloadLink.select();
    document.execCommand('copy');
    alert('Link copied to clipboard.');
}