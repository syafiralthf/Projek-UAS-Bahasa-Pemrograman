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
