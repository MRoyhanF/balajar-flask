from app import app
from app.controller import DosenController
from flask import request, render_template


@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'GET':
        cont = DosenController.index()[0]
        print(cont)
        return render_template("dosen.html", dosens= cont)  
    else:
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.ubah(id)
    else:
        return DosenController.hapus(id)

