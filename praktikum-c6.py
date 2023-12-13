import os
os.system('clear')

a = True

while a:
    pilih = input('Apakah anda ingin melanjutkan? [y/n]')
    if pilih == 'y':
        print('Terimah kasih!')
    elif pilih == 'n':
        print('sampai jumpa lagi :(')
    else:
        print('Jangan aneh deh :(')