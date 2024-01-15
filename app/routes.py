from app import app
from app.controller import DosenController


@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/dosen', methods=['GET'])
def dosens():
    return DosenController.index()