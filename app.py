import json
from rapidfuzz import process

# Memuat data curug dari file JSON
with open("curug_data.json", "r") as file:
    data_curug = json.load(file)

# Fungsi untuk normalisasi input
def normalize_text(text):
    return text.strip().lower()

# Fungsi untuk mencocokkan nama curug dengan RapidFuzz
def cari_curug(input_name):
    curug_names = list(data_curug.keys())
    matched_name, score, _ = process.extractOne(input_name, curug_names)
    if score >= 70:  # Ambang batas kesamaan 70%
        return matched_name
    return None

# Fungsi utama chatbot
def chatbot():
    print("Selamat datang di chatbot rekomendasi curug Bogor!")
    
    while True:
        # Menu utama
        print("\nPilih opsi berikut:")
        print("1. Lihat daftar curug")
        print("2. Cari berdasarkan aktivitas (misalnya: berenang, trekking)")
        print("3. Cari berdasarkan lokasi")
        print("4. Cari berdasarkan fasilitas (misalnya: tempat istirahat)")
        print("5. Tanya langsung (misalnya: Di mana saya bisa berenang?)")
        print("6. Keluar")
        
        user_input = input("Anda: ").strip()
        normalized_input = normalize_text(user_input)

        if normalized_input == "1":
            print("\nBerikut adalah daftar curug yang tersedia:")
            for idx, curug in enumerate(data_curug.keys(), start=1):
                print(f"{idx}. {curug}")
            print("8. Kembali")

            choice = input("Pilih curug atau '8' untuk kembali: ").strip()
            if choice == "8":
                continue
            else:
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(data_curug):
                        curug_name = list(data_curug.keys())[choice - 1]
                        print(f"\nDeskripsi Curug {curug_name}: {data_curug[curug_name]['deskripsi']}")
                    else:
                        print("Pilihan tidak valid.")
                else:
                    curug_name = cari_curug(choice)
                    if curug_name:
                        print(f"\nDeskripsi Curug {curug_name}: {data_curug[curug_name]['deskripsi']}")
                    else:
                        print("Input tidak valid, tidak ditemukan curug yang cocok.")
            
            # Berikan opsi kembali ke menu utama
            input("\nTekan Enter untuk kembali ke opsi awal...")
            continue

        elif normalized_input == "2":
            aktivitas_tersedia = sorted(set([item for curug in data_curug.values() for item in curug["fitur"]["aktivitas"]]))
            print("\nBerikut adalah aktivitas yang tersedia:")
            for idx, aktivitas in enumerate(aktivitas_tersedia, start=1):
                print(f"{idx}. {aktivitas}")
            print("8. Kembali")
            
            activity_choice = input("Pilih aktivitas yang diinginkan (masukkan nomor atau teks) atau '8' untuk kembali: ").strip()
            if activity_choice == "8":
                continue
            else:
                if activity_choice.isdigit():
                    activity_choice = int(activity_choice)
                    if 1 <= activity_choice <= len(aktivitas_tersedia):
                        aktivitas_input = aktivitas_tersedia[activity_choice - 1]
                    else:
                        print("Pilihan tidak valid.")
                        continue
                else:
                    aktivitas_input = activity_choice

                curug_aktivitas = [
                    curug_name
                    for curug_name, curug_info in data_curug.items()
                    if aktivitas_input.lower() in map(str.lower, curug_info["fitur"]["aktivitas"])
                ]
                if curug_aktivitas:
                    print(f"\nBerikut adalah curug yang cocok dengan aktivitas '{aktivitas_input}':")
                    for curug in curug_aktivitas:
                        print(f"- {curug}")
                else:
                    print(f"Tidak ada curug yang cocok dengan aktivitas '{aktivitas_input}'.")
            
            input("\nTekan Enter untuk kembali ke opsi awal...")
            continue

        elif normalized_input == "3":
            lokasi_tersedia = sorted(set([curug_info["lokasi"] for curug_info in data_curug.values()]))
            print("\nBerikut adalah lokasi curug yang tersedia:")
            for idx, lokasi in enumerate(lokasi_tersedia, start=1):
                print(f"{idx}. {lokasi}")
            print("8. Kembali")

            location_choice = input("Pilih lokasi yang diinginkan (masukkan nomor atau teks) atau '8' untuk kembali: ").strip()
            if location_choice == "8":
                continue
            else:
                if location_choice.isdigit():
                    location_choice = int(location_choice)
                    if 1 <= location_choice <= len(lokasi_tersedia):
                        lokasi_input = lokasi_tersedia[location_choice - 1]
                    else:
                        print("Pilihan tidak valid.")
                        continue
                else:
                    lokasi_input = location_choice
                
                curug_lokasi = [
                    curug_name
                    for curug_name, curug_info in data_curug.items()
                    if lokasi_input.lower() in curug_info["lokasi"].lower()
                ]
                if curug_lokasi:
                    print(f"\nBerikut adalah curug yang ada di lokasi '{lokasi_input}':")
                    for curug in curug_lokasi:
                        print(f"- {curug}")
                else:
                    print(f"Tidak ada curug yang ditemukan di lokasi '{lokasi_input}'.")
            
            input("\nTekan Enter untuk kembali ke opsi awal...")
            continue

        elif normalized_input == "4":
            fasilitas_tersedia = sorted(set([item for curug in data_curug.values() for item in curug["fitur"]["fasilitas"]]))
            print("\nBerikut adalah fasilitas yang tersedia:")
            for idx, fasilitas in enumerate(fasilitas_tersedia, start=1):
                print(f"{idx}. {fasilitas}")
            print("8. Kembali")

            fasilitas_choice = input("Pilih fasilitas yang diinginkan (masukkan nomor atau teks) atau '8' untuk kembali: ").strip()
            if fasilitas_choice == "8":
                continue
            else:
                if fasilitas_choice.isdigit():
                    fasilitas_choice = int(fasilitas_choice)
                    if 1 <= fasilitas_choice <= len(fasilitas_tersedia):
                        fasilitas_input = fasilitas_tersedia[fasilitas_choice - 1]
                    else:
                        print("Pilihan tidak valid.")
                        continue
                else:
                    fasilitas_input = fasilitas_choice
                
                curug_fasilitas = [
                    curug_name
                    for curug_name, curug_info in data_curug.items()
                    if fasilitas_input.lower() in map(str.lower, curug_info["fitur"]["fasilitas"])
                ]
                if curug_fasilitas:
                    print(f"\nBerikut adalah curug yang memiliki fasilitas '{fasilitas_input}':")
                    for curug in curug_fasilitas:
                        print(f"- {curug}")
                else:
                    print(f"Tidak ada curug yang memiliki fasilitas '{fasilitas_input}'.")
            
            input("\nTekan Enter untuk kembali ke opsi awal...")
            continue

        elif normalized_input == "5":
            print("\nAnda dapat bertanya seperti: 'Di mana saya bisa berenang?', 'Ada tempat istirahat di curug mana saja?', dll.")
            user_question = input("Tanya saya: ").strip().lower()
            aktivitas_input = None
            for aktivitas in ["berenang", "trekking", "fotografi", "wisata keluarga", "istirahat"]:
                if aktivitas in user_question:
                    aktivitas_input = aktivitas
                    break
            if aktivitas_input:
                curug_aktivitas = [
                    curug_name
                    for curug_name, curug_info in data_curug.items()
                    if aktivitas_input in curug_info["fitur"]["aktivitas"]
                ]
                if curug_aktivitas:
                    print(f"\nBerikut adalah curug yang cocok dengan aktivitas '{aktivitas_input}':")
                    for curug in curug_aktivitas:
                        print(f"- {curug}")
                else:
                    print(f"Tidak ada curug yang cocok dengan aktivitas '{aktivitas_input}'.")
            else:
                print("Maaf, saya tidak mengerti pertanyaan Anda.")
            
            input("\nTekan Enter untuk kembali ke opsi awal...")
            continue

        elif normalized_input == "6":
            print("Terima kasih telah menggunakan chatbot rekomendasi curug Bogor. Sampai jumpa!")
            break

        else:
            print("Maaf, pilihan tidak dikenali. Silakan pilih opsi yang valid.")

chatbot()
