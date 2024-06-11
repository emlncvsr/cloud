
# File Storage and Sharing Website

Welcome to the GitHub repository for our File Storage and Sharing Website. This project allows users to upload files to a storage server and generate sharing links that can be set to expire or remain available indefinitely.

## Features

- **File Upload**: Users can upload files of any type and size.
- **Link Generation**: Generate sharing links for uploaded files.
- **Link Expiry**: Set an expiration time for sharing links or make them permanent.
- **Secure Storage**: Files are securely stored on our server.
- **User Authentication**: Ensure that only registered users can upload and manage files.

## Getting Started

### Prerequisites

- Node.js
- npm (Node Package Manager)
- MongoDB (for user authentication and file metadata)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/emlncvsr/cloud.git
    cd cloud
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Set up your environment variables. Create a `.env` file in the root directory and add the following:
    ```env
    MONGODB_URI=your_mongodb_uri
    STORAGE_PATH=path_to_storage_directory
    SERVER_PORT=your_desired_port
    ```

4. Start the server:
    ```bash
    npm start
    ```

## Usage

### Uploading Files

1. Navigate to the upload page.
2. Select the file you want to upload.
3. Click the "Upload" button.
4. Upon successful upload, a sharing link will be generated.

### Generating Sharing Links

1. Uploaded files will have an option to generate sharing links.
2. Choose the expiration time for the link or set it to be permanent.
3. Click "Generate Link" to create a sharable URL.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Storage**: Local storage or cloud storage services (e.g., AWS S3, Google Cloud Storage)

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.