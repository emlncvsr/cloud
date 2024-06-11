from app import freezer, app

# Set the freezing flag to True
app.config['IS_FREEZING'] = True

if __name__ == '__main__':
    freezer.freeze()
