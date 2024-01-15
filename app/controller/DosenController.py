from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)


def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'nidn' : data.nidn,
        'nama' : data.nama,
        'phone' : data.phone,
        'alamat' : data.alamat
    }

    return data

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], 'Tidak ada data dosen')

        datamahasiswa = formatMahasiswa(mahasiswa)

        data = singleDetailMahasiswa(dosen, datamahasiswa)

        return response.success(data, "success")

    except Exception as e:
        print(e)

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id' : dosen.id,
        'nidn' : dosen.nidn,
        'nama' : dosen.nama,
        'phone' : dosen.phone,
        'mahasiswa' : mahasiswa
    }

    return data


def singleMahasiswa(mahasiswa):
    data = {
        'id' : mahasiswa.id,
        'nim' : mahasiswa.nim,
        'nama' : mahasiswa.nama,
        'phone' : mahasiswa.phone
    }

    return data


def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    return array