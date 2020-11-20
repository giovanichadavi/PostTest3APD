print("==================================")
print("Hallo Selamat Datang Di Toko Kue SULE")
print("==================================")
print("Toko Kami Lagi Ada Promo Nihhh")
print("==================================")
print("Setiap Pembelian Varian Kue Rasa Coklat 5 - 20 Pcs Anda Akan Mendapatkan Diskon 7 %")
print("Pembelian 21 - 35 Pcs Akan Mendapatkan Diskon 12 %")
print("==================================")
print("DAN")
print("==================================")
print("Setiap Pembelian Varian Kue Rasa Keju 4 - 15 Pcs Anda Akan Mendapatkan Diskon 10 %")
print("Pembelian 16 - 25 Pcs Akan Mendapatkan Diskon 15 % ")
nama= input("Silahkan Masukkan Nama Anda  :")
print ("Hai Semoga Harimu Menyenangkan",nama)

keju = int (6000)
coklat = int (3500)
jumlah_keju = (25)
jumlah_coklat = (35)
n = int(input("Masukkan Jumlah Pembelian Kue Coklat : "))
if ( n <= 5 and n <= 21 ):
    print ("Diskon Yang Anda Dapatkan Adalah 7%")
harga = n*coklat
diskon = n*coklat*(7/100)

if ( n <=21 and n <= 35):
    print("Diskon Yang Anda Dapatkan Adalah 12%")
harga = n*coklat
diskon = n*coklat*(12/100)
sisa_kue_coklat = jumlah_coklat - n
print("Sisa Kue Coklat Yang Ada Ditoko Ini Adalah =",sisa_kue_coklat)
total = harga - diskon
print("Total Yang Harus Anda Bayar Adalah :",total)


n = int(input("Masukkan Jumlah Pembelian Kue Keju Anda : "))
if ( n <= 4 and n <=15  ):
    print ("Diskon Yang Anda Dapatkan adalah 10%")
harga = n*keju
diskon = n*keju*(10/100)

if ( n <=16 and n <= 25  ):
    print ("Diskon Yang Anda Dapatkan Adalah 15%")
harga = n*keju
diskon = n*keju*(15/100)

sisa_kue_keju = jumlah_keju - n
print("Sisa Kue Keju Yang Ada Ditoko Ini Adalah =",sisa_kue_keju)

total = harga - diskon
print("Total Yang Harus Anda Bayar Adalah : ", total)

print("Terima Kasih Sudah Berbelanja Ditoko Kami")
print("HAVE A NICE DAYS")
