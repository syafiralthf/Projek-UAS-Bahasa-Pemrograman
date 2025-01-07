## Biodata
Nama: Syafira Luthfi Azzahra

Kelas: TI.24.A.4

NIM: 312410353

# Projek UAS Bahasa Pemrograman
Program ini adalah aplikasi sederhana untuk sistem pendaftaran booking hotel berbasis terminal. Program ini dibuat dengan pendekatan modular dan menggunakan prinsip OOP (Object-Oriented Programming). Program memungkinkan pengguna untuk memesan hotel, menentukan jenis kamar yang diinginkan, dan menentukan berapa hari mereka akan menginap.

```python
# Class untuk menyimpan data pendaftaran
class RegistrationData:
    def __init__(self):
        self.registrations = []

    def add_registration(self, name, phone, email, room_type, hotel_booking):
        self.registrations.append({
            "name": name,
            "phone": phone,
            "email": email,
            "room_type": room_type,
            "hotel_booking": hotel_booking
        })

    def get_registrations(self):
        return self.registrations


# Class untuk memproses data
class Processor:
    def validate_name(name):
        if not name.replace(" ", "").isalpha():
            raise ValueError("Nama hanya boleh berisi huruf!")
        return name

    def validate_phone(phone):
        if not phone.isdigit():
            raise ValueError("Nomor telepon hanya boleh berisi angka!")
        return phone

    def validate_email(email):
        if "@" not in email or "." not in email:
            raise ValueError("Email harus mengandung '@' dan '.'!")
        return email

    def validate_room_type(room_type):
        valid_rooms = ["single", "double", "suite"]
        if room_type.lower() not in valid_rooms:
            raise ValueError(f"Tipe kamar harus salah satu dari: {', '.join(valid_rooms)}")
        return room_type.capitalize()

    def validate_hotel_booking(booking):
        if not booking.isdigit() or int(booking) <= 0:
            raise ValueError("Jumlah malam hotel harus berupa angka positif!")
        return int(booking)


# Class untuk menampilkan hasil
class View:
    def display_table(data):
        print("\nNama                 | Nomor Telepon      | Email                  | Tipe Kamar        | Booking Hotel")
        print("---------------------+--------------------+------------------------+-------------------+----------------")
        for entry in data:
            print(f"{entry['name']:<20} | {entry['phone']:<18} | {entry['email']:<22} | {entry['room_type']:<17} | {entry['hotel_booking']:<16}")


# Main Program 
def main():
    data = RegistrationData()

    while True:
        try:
            print("\n=== Input Data Pendaftaran ===")
            name = Processor.validate_name(input("Nama Lengkap: "))
            phone = Processor.validate_phone(input("Nomor Telepon: "))
            email = Processor.validate_email(input("Email: "))
            room_type = Processor.validate_room_type(input("Tipe Kamar (Single/Double/Suite): "))
            hotel_booking = Processor.validate_hotel_booking(input("Booking Hotel (jumlah malam): "))

            data.add_registration(name, phone, email, room_type, hotel_booking)

            more = input("Tambah data lagi? (y/n): ").strip().lower()
            if more != 'y':
                break
        except ValueError as e:
            print(f"Input Error: {e}")

    print("\n=== Hasil Akhir Pendaftaran ===")
    View.display_table(data.get_registrations())


if __name__ == "__main__":
    main()
```

# Class `RegistrationData`
Class ini bertanggung jawab untuk menyimpan dan mengelola data pendaftaran yang dilakukan oleh pengguna.

```python
class RegistrationData:
    def __init__(self):
        self.registrations = []  # Menyimpan data pendaftaran dalam list kosong

    def add_registration(self, name, phone, email, room_type, hotel_booking):
        # Menambahkan data pendaftaran ke dalam list 'registrations'
        self.registrations.append({
            "name": name,
            "phone": phone,
            "email": email,
            "room_type": room_type,
            "hotel_booking": hotel_booking
        })

    def get_registrations(self):
        # Mengembalikan seluruh data pendaftaran yang sudah disimpan
        return self.registrations
```

Penjelasan:

- `__init__(self)`: Menginisialisasi list kosong registrations yang nantinya akan menyimpan data pendaftaran.
- `add_registration(self, name, phone, email, room_type, hotel_booking)`: Menambahkan data baru ke dalam list registrations dalam bentuk dictionary.
- `get_registrations(self)`: Mengembalikan data pendaftaran yang telah disimpan dalam bentuk list.

# Class `Processor`
Class ini berfungsi untuk memvalidasi input dari pengguna untuk memastikan data yang dimasukkan sesuai dengan format yang benar.

```python
class Processor:
    def validate_name(name):
        # Memastikan nama hanya berisi huruf dan spasi
        if not name.replace(" ", "").isalpha():
            raise ValueError("Nama hanya boleh berisi huruf!")
        return name

    def validate_phone(phone):
        # Memastikan nomor telepon hanya berisi angka
        if not phone.isdigit():
            raise ValueError("Nomor telepon hanya boleh berisi angka!")
        return phone

    def validate_email(email):
        # Memastikan email mengandung '@' dan '.'
        if "@" not in email or "." not in email:
            raise ValueError("Email harus mengandung '@' dan '.'!")
        return email

    def validate_room_type(room_type):
        # Memastikan tipe kamar valid (single, double, atau suite)
        valid_rooms = ["single", "double", "suite"]
        if room_type.lower() not in valid_rooms:
            raise ValueError(f"Tipe kamar harus salah satu dari: {', '.join(valid_rooms)}")
        return room_type.capitalize()  # Mengubah tipe kamar menjadi format yang benar (misalnya 'Single' atau 'Suite')

    def validate_hotel_booking(booking):
        # Memastikan jumlah malam hotel berupa angka positif
        if not booking.isdigit() or int(booking) <= 0:
            raise ValueError("Jumlah malam hotel harus berupa angka positif!")
        return int(booking)
```

Penjelasan:

- `validate_name(name)`: Memastikan nama hanya berisi huruf dan spasi. Jika ada karakter lain selain huruf, program akan menampilkan pesan error.
- `validate_phone(phone)`: Memastikan nomor telepon hanya berisi angka. Jika ada karakter selain angka, akan muncul pesan error.
- `validate_email(email)`: Memeriksa apakah email mengandung simbol "@" dan ".", yang merupakan bagian dari format email yang benar.
- `validate_room_type(room_type)`: Memastikan tipe kamar yang dimasukkan valid (dalam pilihan yang sudah ditentukan: "single", "double", atau "suite").
- `validate_hotel_booking(booking)`: Memastikan jumlah malam hotel yang dimasukkan adalah angka positif.

# Class `View`
Class ini bertanggung jawab untuk menampilkan data pendaftaran dalam bentuk tabel yang rapi.

```python
class View:
    def display_table(data):
        # Menampilkan data pendaftaran dalam format tabel yang rapi
        print("\nNama                 | Nomor Telepon      | Email                  | Tipe Kamar        | Booking Hotel")
        print("---------------------+--------------------+------------------------+-------------------+----------------")
        for entry in data:
            print(f"{entry['name']:<20} | {entry['phone']:<18} | {entry['email']:<22} | {entry['room_type']:<17} | {entry['hotel_booking']:<16}")
```

Penjelasan:

- `display_table(data)`: Fungsi ini digunakan untuk menampilkan seluruh data pendaftaran dalam bentuk tabel. Setiap kolom dipisahkan dengan simbol | dan data ditampilkan dengan lebar yang sama agar terlihat rapi.

# Fungsi Main
Bagian ini mengatur alur utama program, termasuk meminta input dari pengguna, memvalidasi input, menyimpan data, dan menampilkan hasilnya.

```python
def main():
    data = RegistrationData()  # Membuat objek untuk menyimpan data pendaftaran

    while True:
        try:
            print("\n=== Input Data Pendaftaran ===")
            name = Processor.validate_name(input("Nama Lengkap: "))  # Memvalidasi nama
            phone = Processor.validate_phone(input("Nomor Telepon: "))  # Memvalidasi nomor telepon
            email = Processor.validate_email(input("Email: "))  # Memvalidasi email
            room_type = Processor.validate_room_type(input("Tipe Kamar (Single/Double/Suite): "))  # Memvalidasi tipe kamar
            hotel_booking = Processor.validate_hotel_booking(input("Booking Hotel (jumlah malam): "))  # Memvalidasi jumlah malam hotel

            data.add_registration(name, phone, email, room_type, hotel_booking)  # Menyimpan data pendaftaran

            more = input("Tambah data lagi? (y/n): ").strip().lower()  # Menanyakan apakah ingin menambah data lagi
            if more != 'y':
                break  # Keluar dari loop jika pengguna tidak ingin menambah data lagi
        except ValueError as e:
            print(f"Input Error: {e}")  # Menampilkan pesan error jika input tidak valid

    print("\n=== Hasil Akhir Pendaftaran ===")
    View.display_table(data.get_registrations())  # Menampilkan data pendaftaran dalam format tabel

if __name__ == "__main__":
    main()  # Menjalankan fungsi main saat program dijalankan
```

Penjelasan:

- `data = RegistrationData()`: Membuat objek `RegistrationData` untuk menyimpan data pendaftaran.
- `while True:`: Program meminta input berulang kali hingga pengguna memilih untuk berhenti dengan mengetikkan "n".
- `try-except`: Jika terjadi kesalahan input (misalnya format email salah atau nama mengandung angka), error akan ditangkap dan ditampilkan dengan pesan yang sesuai.
- `data.add_registration()`: Menambahkan data pendaftaran yang telah divalidasi ke dalam objek `RegistrationData`.
- `View.display_table()`: Setelah selesai, data ditampilkan dalam bentuk tabel yang rapi menggunakan class `View`.

# Penanganan Error
Program ini menggunakan `try-except` untuk menangkap kesalahan input. Jika pengguna memasukkan data yang tidak sesuai format (seperti nomor telepon yang mengandung huruf atau email yang tidak lengkap), program akan menampilkan pesan kesalahan yang memberi tahu pengguna tentang masalah tersebut.

# Contoh Output Program
Berikut adalah contoh output setelah pengguna berhasil memasukkan data:

![Cuplikan layar 2025-01-06 122444](https://github.com/user-attachments/assets/d9bca156-462b-4e4d-9837-09c3b5a2ba63)
