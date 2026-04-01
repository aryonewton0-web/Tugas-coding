#berinteraksi dengan pengguna (tampilan menu, input/output)
import backend
import logger

def tampilan_menu():
    print("\n===APLIKASI DAFTAR BELANJA===")
    print("1. Tambah item")
    print("2. Lihat semua item")
    print("3. Hapus item")
    print("4. Edit item")
    print("5. Cari item")
    print("6. Saran Bahan (API)")
    print("7. Keluar")
def main():
    """Loop utama program"""
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu (1-7):")
        
        if pilihan =='1':
            item=input("Nama item: ")
            pesan = backend.tambah_item(item) #panggil backend
            print(pesan)
            
        elif pilihan =='2':
            daftar = backend.semua_item() #panggil backend
            if not daftar:
                print("Daftar belanja kosong")
            else:
                print("\n Daftar belanja: ")
                for i, nama in enumerate(daftar, start=1):
                    print(f" {i}.{nama}")
        
        elif pilihan =='3':
            daftar = backend.semua_item()
            if not daftar:
                print("Tidak ada item untuk dihapus ")
                continue
            for i, nama in enumerate(daftar, start=1):
                print(f" {i}.{nama}")
            try:
                no = int(input("Nomor item yang akan dihapus: "))
                pesan = backend.hapus_item(no)
                print(pesan)
            except ValueError:
                print("Masukkan angka .")
        elif pilihan =='4':
            daftar=backend.semua_item() 
            if not daftar:
                print("tidak untuk diedit")
                continue
            for i, nama in enumerate (daftar, start=1):
                print (f" {i}.{nama}")
            try:
                no= int(input("nomor items yang akan di edit"))
                nama_baru=input("nama baru: ")
                if nama_baru.strip()=="":
                    print("nmaa tidak boleh kosong")
                else:
                    pesan =backend.edit_item(no, nama_baru)
                    print(pesan)
            except ValueError:
                    print("masukkan angka")
        elif pilihan=='5':
            kata=input("masukkan kata kunci: ")
            hasil=backend.cari_item(kata)
            if kata.strip() == "":
                print ("kata kunci gak bisa kosong ")
            else: 
                hasil = backend.cari_item(kata)
            if not hasil:
                print("tidak ada item yang cocok ")
            else:
                print("\n Hasil Pencarian:")
            for i, item in enumerate (hasil, start=1):
                print(f"   {i}.{item}")
        elif pilihan=='6':
            print("\n🌐 Mengambil saran bahan dari internet...")
            logger.tulis_log("Memanggil API saran bahan")
            saran = backend.saran_bahan()
            if not saran or "⚠️ Gagal" in saran[0]:
                print(saran[0])
                logger.tulis_log("Gagal mengambil saran dari API")
            else:
                print("\n📋 Saran Bahan (dari API):")
                for i, item in enumerate(saran, start=1):
                    print(f"   {i}. {item}")
                    logger.tulis_log("Berhasil mengambil saran dari API")
        elif pilihan=='7':
            print("Sampai jumpa") 
            break
        else:
           print("pilihan tidak valid")
            
if __name__== "__main__":
    main()