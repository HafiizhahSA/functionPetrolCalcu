#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")
#mmeanggil fungsi untuk dapat  dijalankan
pengenalan_function()

#=============================================================================================================
def identitas_pembeli(nama,nomor_hape,pekerjaan):
  biodata_pembeli = "Nama : "+nama+", No.Hp :"+nomor_hape+", pekerjaan :"+pekerjaan;
  return (biodata_pembeli)
print("Biodata Pembeli = ", identitas_pembeli("Hafiizhah Syachna Azzahra", "08123456789", "Mahasiswi"))

#===============================================================================================================

# object data pembeli yang meliputi (nama,nomerHape, pekerjaan)
data_pembeli = []

# input data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) dari terminal

def identitas_pembeli(nama, nomor_hape, pekerjaan):
    print("Nama Pembeli: ", nama)
    data_pembeli.append(nama)
    print("Nomor Hape: ", nomor_hape)
    data_pembeli.append(nomor_hape)
    print("Pekerjaan: ", pekerjaan)
    data_pembeli.append(pekerjaan)
    return data_pembeli

# get input from terminal
nama = input("Masukkan nama pembeli: ")
data_pembeli.append(nama)
nomor_hape = input("Masukkan nomor hape pembeli: ")
data_pembeli.append(nomor_hape)
pekerjaan = input("Masukkan pekerjaan pembeli: ")
data_pembeli.append(pekerjaan)

#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
fuels_type_price = {"pertalite": 10000, "pertamax": 12000, "solar": 5000}
def hitung_biaya_bbm (jumlah_liter, jenis_bbm):
    fuel_price = fuels_type_price[jenis_bbm]
    total_belanja = jumlah_liter * fuel_price
    print("Total Belanja: ", total_belanja)
    return total_belanja

# get input from terminal
jenis_mobil = input("Masukkan jenis mobil: ")
jumlah_liter = int(input("Masukkan jumlah liter: "))
jenis_bbm = input("Masukkan jenis bbm: ")

# print jenis 
# call function total_belanja
total_belanja = hitung_biaya_bbm(jumlah_liter, jenis_bbm)

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah

print("nama pembeli ",data_pembeli[0], "Jenis Mobil",jenis_mobil, "telah membeli tipe bbm", jenis_bbm, "seharga", fuels_type_price[jenis_bbm], "dengan total belanja", total_belanja, "rupiah")

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
    if uang >= total_belanja:
        sisa_uang = uang - total_belanja
        belanja(sisa_uang)
        print(sisa_uang)
    else:
        sisa_uang = 0
    return sisa_uang


print("\n\nRecursion Example Results")

uang = int(input("Masukkan jumlah uang: "))
belanja(uang)
# output jika uang 720000 dan total_belanja 360000
# 0
# 360000