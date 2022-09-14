n = int(input("Masukkan range data : "))
kamus = {}
for i in range(n):
    if i%2==0:
        if i == 0:
            kamus[i] = 1
        else:
            faktorial = 1
            for j in range (2, i+1):
                faktorial *= j
            kamus[i] = faktorial
print(kamus)

list_key = list(kamus.keys())
data = int(input("Data Ditampilkan : "))
if data not in list_key:
    print("Data tidak ditemukan")
else:
    print(f'Data ditemukan = {kamus[data]}')