import os

# Set environment variables for other
os.environ['engine'] = 'postgresql'
os.environ['name'] = 'audiodb'
os.environ['user'] = 'audiodev'
os.environ['password'] = 'audiodev'
os.environ['host'] = 'localhost'
os.environ['port'] = '5432'

os.environ['connect'] = 'postgresql://audiodev:audiodev@localhost:5432/audiodb'
