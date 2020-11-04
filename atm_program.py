import random
from datetime import date
from customer import Customer
from atm_card import ATMCard

menu1 = ['Buat ATM', 'Login', 'Exit']
menu2 = ['Cek saldo', 'Debet', 'Simpan', 'Ganti PIN', 'Keluar']

while True:
    no_item1 = 0
    for item1 in menu1:
        print(str(no_item1) + '. ' + item1)
        no_item1 += 1
    selected1 = int(input('Masukkan pilihan Anda: '))
    if selected1 == 0:
        atm = ATMCard()
        cust = Customer(int(atm.checkPin()), int(atm.checkBalance()))
    elif selected1 == 1:
        if 'atm' in globals():
            inCard = int(input('\nMasukkan nomor kartu:\n'))
            while(inCard != int(atm.checkCard())):
                inCard = int(input('Kartu tidak dikenali. silahkan masukkan kartu lain: '))
            while(inCard == int(atm.checkCard())):
                inPin = int(input('Masukkan pin:\n'))
                if inPin != int(atm.checkPin()):
                    coba = 0
                    while(coba < 3):
                        inPin = int(input('pin salah. silahkan masukan lagi: '))
                        coba += 1
                        if inPin == int(atm.checkPin()):
                            break
                        elif coba >= 3:
                            print('diblokir')
                            exit()
                while(inPin == int(atm.checkPin()) and inCard == int(atm.checkCard())):
                    no_item2 = 0
                    print('')
                    for item2 in menu2:
                        print(str(no_item2) + '. ' + item2)
                        no_item2 += 1
                    no = int(input('masukkan perintah: '))
                    if no == 0:
                        print(cust.checkBalance())
                    elif no == 1:
                        nominal = int(input('\nMasukkan nominal untuk debet: '))
                        print(cust.withdrawBalance(nominal))
                    elif no == 2:
                        nominal = int(input('\nMasukkan nominal untuk simpan: '))
                        print(cust.depositBalance(nominal))
                    elif no == 3:
                        inPin = int(input('\nMasukkan pin lama:\n'))
                        if inPin != int(atm.checkPin()):
                            coba = 0
                            while(coba < 3):
                                inPin = int (input('pin salah. silahkan masukan lagi: '))
                                coba += 1
                                if inPin == int(atm.checkPin()):
                                    break
                                elif coba >= 3:
                                    print('diblokir')
                                    exit()
                        if inPin == int(atm.checkPin()):
                            npin = int(input('Masukkan pin yang baru: '))
                            print(atm.gantiPin(npin))
                    elif no == 4:
                        resi = random.randint(100000, 1000000)
                        tanggal = date.today()
                        print('\n' + '''resi       : ''' + str(resi))
                        print('''tanggal    : ''' + str(tanggal))
                        print('''Sisa saldo : ''' + str(cust.custBalance) + '\n')
                        exit()
                    else:
                        print('\ninputan tidak dikenali')
        else:
            print('Anda belum membuat kartu')
    elif selected1 == 3:
        exit()
    else:
        print('Inputan tidak dikenali')
        exit()

