from app import freezer

# Mock the authentication process during freezing
def mock_get_auth_token():
    return "mocked_auth_token"

# Replace the actual get_auth_token function with the mock one during freezing
freezer.app.view_functions['initialize_auth_token'] = lambda: None
freezer.app.config['auth_token'] = mock_get_auth_token()

if __name__ == '__main__':
    freezer.freeze()
