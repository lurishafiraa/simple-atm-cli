
from model.user_atm import *
from controller.controller_atm import cek_login, cek_user, cek_rekening, transfer_uang, ambil_uang

status_login = False
pakai_atm = "y"

while pakai_atm == "y":
    while not status_login:
        print("----------------------------")
        print("SELAMAT DATANG DI SIMPLE ATM")
        print("----------------------------")
        print("Silahkan masukkan PIN anda")
        pin = input("Masukkan PIN : ")
 
        cl = cek_login(pin)
        if cl:
            print("Halo, " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Maaf PIN anda salah")
            print("")
 
    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("----------------------------")
        print("SELAMAT DATANG DI SIMPLE ATM")
        print("----------------------------")
        print("1. Cek Saldo")
        print("2. Transfer Uang")
        print("3. Ambil Uang")
        print("4. Logout")
        print("5. Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Transfer Uang Silahkan Masukkan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
 
            if cnk >= 0:
                print("Nomor rekening ditemukan, silahkan masukkan nominal yang yang akan di transfer")
                nominal = input("Nominal Transfer : ")
                transfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            nominal = input("Nominal Penarikan : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
 
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"

 
 
