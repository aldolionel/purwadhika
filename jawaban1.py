def pertama(text):
    z ="*"
    for i in text.split():
        z += i.upper()
    z += '*'      
    
    if len(z) > 202 :
        print("Batas Karakter Maksimal Hanya 200")
    elif z == '**' :
        print ("Masukkan Sebuah Inputan")
    else:
        print(z)

word = input("Masukkan Sebuah Kalimat : ")
pertama(word)