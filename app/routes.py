from app import app

@app.route('/')
def index():
    return 'Hello Flask App'

def ini():
    return 'hello kawan'