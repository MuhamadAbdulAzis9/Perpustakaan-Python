from os import curdir
from pickle import TRUE
from sqlite3 import Cursor
from tkinter import Menu
from turtle import update
from unicodedata import name
from unittest import result
import mysql.connector
import os

db = mysql.connector.connect(host="localhost",user = "root",password ="",database ="perpustakaan")

if db.is_connected():
    print("connect")

def insert_data(db):
    name= input("Masukkan nama: ")
    address= input("Masukan alamat: ")
    book= input("Masukan judul buku: ")
    val =(name,address,book)
    cursor=db.cursor()
    sqlInsert = "INSERT INTO peminjam (nama_peminjam,alamat,buku) VALUES (%s,%s,%s)"
    cursor.execute(sqlInsert, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data(db):
    cursor= db.cursor()
    sqlRead="SELECT * FROM peminjam"
    cursor.execute(sqlRead)
    result=cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in result:
            print(data)

def update_data(db):
    cursor= db.cursor()
    show_data(db)
    id_peminjam= input("Pilih id peminjam=> ")
    name= input("Nama baru: ")
    alamat= input("Alamat baru: ")
    buku= input("Buku baru: ")
    sqlUpdate= "UPDATE peminjam SET nama_peminjam=%s, alamat=%s, buku=%s WHERE id_peminjam=%s"
    val=(name, alamat, buku, id_peminjam)
    cursor.execute(sqlUpdate, val)
    db.commit()
    print("{} Data berhasil  diubah".format(cursor.rowcount))

def delete_data(db):
    cursor=db.cursor()
    show_data(db)
    id_peminjam= input("Pilih id peminjam=> ")
    sqlDelete= 'DELETE FROM peminjam WHERE id_peminjam='+id_peminjam
    cursor.execute(sqlDelete)
    db.commit()
    print("{} Data berhasil dihapus".format(cursor.rowcount))

def main(db):
    print("Perpustakaan Asgard")
    print("1. Insert data")
    print("2. Tampil data")
    print("3. Update data")
    print("4. Hapus data")
    print("0. Keluar")
    menu= input("Pilih menu=> ")

    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu tidak ada")

if __name__ =="__main__":
    while(True):
        main(db)


    



     

