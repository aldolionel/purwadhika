def HP(n) :
    nomor = [int(i) for i in n]
    print (type(nomor))
    if len(nomor) > 13 :
        print ('Nomor HP hanya maksimal 13 Angka')
    elif nomor[0] != 0 and nomor[1] != 8 :
        print ('Nomor HP harus dimulai dengan "08"')
    else :
        strnomor = [str(i) for i in nomor]
        final = ''.join(strnomor)
        print ('Nomor HP Saya Adalah ' + final)

nomorHP = input ("Masukkan Nomor HP : ")
HP(nomorHP)