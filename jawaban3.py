#no 3
def sort_odd_even(num):
    val_ganjil = []
    val_genap = []
    hasil = []
    for val in num:
        if val % 2 != 0:
            val_ganjil.append(val)
        else:
            val_genap.append(val)
    # val_ganjil.sort()
    for i in range(len(val_ganjil)):
        for j in range(i+1, len(val_ganjil)):
            if val_ganjil[i] > val_ganjil[j]:
                val_ganjil[i], val_ganjil[j] = val_ganjil[j], val_ganjil[i]
    hasil.append(val_ganjil)
    # val_genap.sort(reverse= True)
    for i in range(len(val_genap)):
        for j in range(i+1, len(val_genap)):
            if val_genap[i] < val_genap[j]:
                val_genap[i], val_genap[j] = val_genap[j], val_genap[i]
    hasil.append(val_genap)
    hasil = val_ganjil+val_genap
    print (hasil)
   

sort_odd_even([1,3,2,2,1,5,1,24,12,124,12,21,32,15])

