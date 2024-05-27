#Capstone Project Module 1
#Case Study: Data Pasien Rumah Sakit

#Data Dummy Pasien
data_pasien = [{'tgl_registrasi': '2024-05-01', 'id': 111110, 'nama': 'Sumadi Joko', 'usia': 30, 'jenis_kelamin': 'Pria'},
    {'tgl_registrasi': '2024-05-02', 'id': 111111, 'nama': 'Dwi Fajar', 'usia': 28, 'jenis_kelamin': 'Pria'},
    {'tgl_registrasi': '2024-05-03','id': 111112, 'nama': 'Rita Yunita', 'usia': 32, 'jenis_kelamin': 'Wanita'}]

#Menu Input
def MainMenu():
    menu = input('''
Selamat Datang di Rumah Sakit Aman Jiwa
             
Menu :
1. Menampilkan Daftar Pasien
2. Registrasi Pasien
3. Update Data Pasien
4. Menghapus Data Pasien
5. Pembelian Obat dan Vitamin
6. Exit
             
Pilih Menu: ''')

    if (menu == '1'): 
        menu1()
    elif (menu == '2'):
        menu2()
    elif (menu == '3'):
        menu3()
    elif (menu == '4'):
        menu4()
    elif (menu == '5'):
        menu5()
    elif (menu == '6'):
        print ('Terima Kasih Atas Kunjungan Anda!')
        exit()
    else:
        print ('Masukkan Pilihan Menu yang Tepat')
        MainMenu()

#1. Menampilkan Daftar Pasien (Read Menu)
def menu1():
    menu = input ('''
Menampilkan Daftar Pasien
1. Menampilkan Seluruh Data
2. Mencari Data Pasien
3. Kembali ke Menu Awal
                  
Masukkan Pilihan Menu: ''')
    if menu == '1':
        MenampilkanDaftarPasien()
    elif menu == '2':
        IDCari = int(input('Masukkan ID Pasien yang Dicari: '))
        for i in range(0,len(data_pasien),1):
            if IDCari == data_pasien[i]['id']:
                print ('ID {}'.format(IDCari),'sama dengan ID Pasien nomor {} Rumah Sakit Aman Jiwa'.format(i))
            else:
                print ('ID {}'.format(IDCari),'tidak sama dengan ID Pasien nomor {} Rumah Sakit Aman Jiwa'.format(i))
    elif menu == '3':
        MainMenu()
    else:
        print ('\nMasukkan Pilihan Menu yang Tepat')
    menu1()    

#2. Registrasi Pasien (Create Menu)
def menu2():
    menu = input('''
Registrasi Pasien
1. Input Registrasi Pasien Baru
2. Kembali ke Menu Awal
                 
Masukkan Pilihan Menu: ''') 
    if menu == '1':
        #Input ID Pasien
        konfirmasi_id = True
        while konfirmasi_id:
            IDPasien = input('Masukkan ID Pasien: ')
            if len(IDPasien) == 6:
                konfirmasi_id = False
            elif IDPasien in data_pasien['id']:
                print ('ID sudah terdaftar')
            else:
                print ('Masukkan ID yang Benar')
        #Input Nama Pasien
        NamaPasien = input ('Masukkan Nama Pasien: ')
        #Input Usia Pasien
        UsiaPasien = input ('Masukkan Usia Pasien: ')
        #Input Jenis Kelamin Pasien
        konfirmasi_kelamin = True
        while konfirmasi_kelamin:
            KelaminPasien = input ('Masukkan Jenis Kelamin Pasien (Pria/Wanita): ')
            if KelaminPasien.lower() == 'pria' or KelaminPasien.lower() == 'wanita':
                konfirmasi_kelamin = False
            else:
                print ('Masukkan Jenis Kelamin yang Benar')
        #Import Date Time        
        import datetime
        #Penambahan Dalam List Pasien
        data_pasien.append({
            'tgl_registrasi': datetime.date.today(),
            'id': IDPasien,
            'nama': NamaPasien.capitalize(),
            'usia': UsiaPasien,
            'jenis_kelamin': KelaminPasien.capitalize()
        })
        MenampilkanDaftarPasien()
    elif menu == '2':
        MainMenu()
    else:
        print ('\nMasukkan Pilihan Menu yang Tepat')
    menu2()

#3. Update Data Pasien
def menu3():
    menu = input('''
Registrasi Pasien
1. Update Data Pasien
2. Kembali ke Menu Awal
                 
Masukkan Pilihan Menu: ''')
    if menu == '1':
        MenampilkanDaftarPasien()
        NomorPasien = int(input('Masukkan Nomor Pasien yang akan di edit data: '))
        MenuEdit = input('''
Pilih Kolom yang Akan di Update:
1. ID Pasien
2. Nama Pasien
3. Usia Pasien
4. Jenis Kelamin Pasien
5. Kembali ke Menu Update Data Pasien
                         
Masukkan Pilihan Menu: ''')
        #Edit ID Pasien
        if MenuEdit == '1':
            konfirmasi_id = True
            while konfirmasi_id:
                IDPasienBaru = input ('Masukkan ID Pasien: ')
                if len(IDPasienBaru) == 6:
                    data_pasien[NomorPasien]['id'] = IDPasienBaru
                    MenampilkanDaftarPasien()
                    konfirmasi_id = False
                elif IDPasienBaru in data_pasien[0:len(data_pasien)]['id']:
                    print ('ID sudah terdaftar')
                else:
                    print ('Masukkan ID yang Benar')
        #Edit Nama Pasien
        elif MenuEdit == '2':
            NamaPasienBaru = input ('Masukkan Nama Pasien: ')
            data_pasien[NomorPasien]['nama'] = NamaPasienBaru.capitalize()
            MenampilkanDaftarPasien()
        #Edit Usia Pasien
        elif MenuEdit == '3':
            UsiaPasienBaru = input ('Masukkan Usia Pasien: ')
            data_pasien[NomorPasien]['usia'] = UsiaPasienBaru
            MenampilkanDaftarPasien()
        #Edit Jenis Kelamin Pasien
        elif MenuEdit == '4':
            konfirmasi_kelamin = True
            while konfirmasi_kelamin:
                KelaminPasienBaru = input ('Masukkan Jenis Kelamin Pasien (Pria/Wanita): ')
                if KelaminPasienBaru.lower() == 'pria' or KelaminPasienBaru.lower() == 'wanita':
                    data_pasien[NomorPasien]['jenis_kelamin'] = KelaminPasienBaru.capitalize()
                    MenampilkanDaftarPasien()
                    konfirmasi_kelamin = False
                else:
                    print ('Masukkan Jenis Kelamin yang Benar')
        elif MenuEdit == '5':
            menu3()
        else:
            print ('Masukkan Pilihan yang Benar')
    elif menu == '2':
        MainMenu()
    else:
        print ('\nMasukkan Pilihan Menu yang Tepat')
    menu3()
    
#4. Menghapus Data Pasien
def menu4():
    menu = input('''
Registrasi Pasien
1. Menghapus Data Pasien
2. Kembali ke Menu Awal
                 
Masukkan Pilihan Menu: ''')
    if menu == '1':
        MenampilkanDaftarPasien()
        try:
            NomorPasien = int(input('Masukkan Nomor Pasien yang akan dihapus: '))
            del data_pasien[NomorPasien]
            MenampilkanDaftarPasien()
        except IndexError:
            print ('Masukkan Nomor yang Benar')
    elif menu == '2':
        MainMenu()
    else:
        print ('\nMasukkan Pilihan Menu yang Tepat')
    menu4()

#Menampilakan Seluruh Data Pasien
def MenampilkanDaftarPasien():
    print ('\nDaftar Pasien\n')
    print ('Nomor\t| Tgl Regist\t| ID Pasien\t| Nama\t\t| Usia\t| Kelamin')
    for i in range(len(data_pasien)):
        print ('{}\t| {}\t| {}\t| {}\t| {}\t| {}'.format(i,data_pasien[i]['tgl_registrasi'],data_pasien[i]['id'],data_pasien[i]['nama'],data_pasien[i]['usia'],data_pasien[i]['jenis_kelamin']))

#5. Pembelian Obat dan Vitamin
def menu5():
    menu = input('''
Registrasi Pasien
1. Pembelian Obat dan Vitamin
2. Kembali ke Menu Awal
                 
Masukkan Pilihan Menu: ''')
    if menu == '1':
        #Input Jumlah Vitamin
        jumlah_vitamin = int(input("Masukkan Jumlah Vitamin: "))
        stock_vitamin = 100
        while (jumlah_vitamin > stock_vitamin):
            print ('Jumlah yang dimasukkan terlalu banyak')
            print ('Stock Vitamin Tinggal: {}'.format(stock_vitamin))
            jumlah_vitamin=int(input('Masukkan Jumlah Vitamin: '))
        #Input Jumlah Obat
        jumlah_obat = int(input("Masukkan Jumlah Obat: "))
        stock_obat = 100
        while (jumlah_obat > stock_obat):
            print ('Jumlah yang dimasukkan terlalu banyak')
            print ('Stock Obat Tinggal: {}'.format(stock_obat))
            jumlah_obat=int(input('Masukkan Jumlah Obat: '))
        #Harga Pembelian Vitamin dan Obat
        print ('\nDetail Pembelian Obat dan Vitamin\n')
        harga_vitamin = jumlah_vitamin*50000
        print ('Vitamin: {}'.format(jumlah_vitamin),'x 50000 = {}'.format(harga_vitamin))
        harga_obat = jumlah_obat *100000
        print ('Obat: {}'.format(jumlah_obat),'x 100000 = {}'.format(harga_obat))
        total = harga_vitamin + harga_obat
        print ('\nTotal: {}\n'.format(total))
        #Pembayaran Vitamin dan Obat
        jumlah_uang = int(input("Masukkan Jumlah Uang: "))
        while (jumlah_uang < total):
            kekurangan = total - jumlah_uang
            print ('Uang anda kurang sebesar {}'.format(kekurangan))
            jumlah_uang = int(input('Masukkan Jumlah Uang: '))
        if (jumlah_uang > total):
            kembalian = jumlah_uang - total
            print ('Uang Kembali Anda: {}'.format(kembalian))
            print ('Terima Kasih')
        else:
            print ('Terima kasih')
    elif menu == '2':
        MainMenu()
    else:
        print ('\nMasukkan Pilihan Menu yang Tepat')
    menu5()
    
#Menjalankan Menu Utama
MainMenu()

