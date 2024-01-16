from app.model.dosen import Dosen

from flask import render_template
from app.model.mahasiswa import Mahasiswa

from app import response, app, db
from flask import request

#function mengambil data dosen
def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        res = response.success(data, "success")
        return data, res
        #return response.success(data, "success")
        #return render_tamplate("dosen.html", )
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

#function mengambil data dosen by ID
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

#menambahkan data dosen
def save():
    try :
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosen = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosen)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Dosen')
    except Exception as e:
        print(e)

#update data dosen
def ubah(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn' : nidn,
                'nama' : nama,
                'phone' : phone,
                'alamat' : alamat
            }
        ]
        
        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.success(input, 'Success Update Data !')
    
    except Exception as e:
        print(e)

#hapus data dosen
def hapus(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], 'Data Dosen Kosong...!!')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data Dosen...!')

    except Exception as e:
        print(e)    