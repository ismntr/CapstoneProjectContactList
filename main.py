import sqlite3
import csv
import json
import os

from simple_term_menu import TerminalMenu

# Klasörleri oluşturmak için yardımcı fonksiyon
def create_folders():
    folders = ["SQLData", "CSVData", "JSONData", "IsmetifyData"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

# SQLite veritabanı oluşturma
def create_sqlite_database():
    conn = sqlite3.connect("SQLData/mydatabase.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT,
                   last_name TEXT,
                   phone_number TEXT,
                   email TEXT,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

# CSV, JSON ve İsmetify dosyalarını oluşturma
def create_data_files():
    files = {
        "CSVData/contacts.csv": ["first_name", "last_name", "phone_number", "email"],
        "JSONData/contacts.json": [],
        "IsmetifyData/contacts.txt": [],
    }

    for file, header in files.items():
        if not os.path.exists(file):
            with open(file, 'w', newline='') as f:
                if header:
                    writer = csv.writer(f)
                    writer.writerow(header)

# SQLite veritabanına kişi ekleme fonksiyonu
def add_contact_to_sqlite(first_name, last_name, phone_number, email):
    conn = sqlite3.connect("SQLData/mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM contacts WHERE first_name = ? AND email = ?", (first_name, email))
    existing_contact = cursor.fetchone()

    if existing_contact:
        print("A contact with the same name and email already exists.")
    else:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?)",
                       (first_name, last_name, phone_number, email))
        conn.commit()
        conn.close()
        print("Contact added successfully to SQLite.")

# CSV verilerine kişi ekleme fonksiyonu
def add_contact_to_csv(first_name, last_name, phone_number, email):
    new_contact = [first_name, last_name, phone_number, email]
    with open("CSVData/contacts.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_contact)
    print("Contact added successfully to CSV.")

# JSON verilerine kişi ekleme fonksiyonu
def add_contact_to_json(first_name, last_name, phone_number, email):
    new_contact_dict = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number, "email": email}
    json_file = "JSONData/contacts.json"

    if not os.path.exists(json_file):
        with open(json_file, 'w') as file:
            json.dump([new_contact_dict], file, indent=4)
    else:
        with open(json_file, 'r') as file:
            try:
                json_data = json.load(file)
            except json.decoder.JSONDecodeError:
                json_data = []

        json_data.append(new_contact_dict)
        with open(json_file, 'w') as file:
            json.dump(json_data, file, indent=4)

    print("Contact added successfully to JSON.")


# İsmetify verilerine kişi ekleme fonksiyonu
def add_contact_to_ismetify(first_name, last_name, phone_number, email):
    new_contact_str = "|".join([first_name, last_name, phone_number, email])
    with open("IsmetifyData/contacts.txt", 'a') as file:
        file.write(new_contact_str + '\n')
    print("Contact added successfully to İsmetify.")

# Kişi ekleme işlemlerini birleştiren fonksiyon
def add_contact_to_all_sources(first_name, last_name, phone_number, email):
    add_contact_to_sqlite(first_name, last_name, phone_number, email)
    add_contact_to_csv(first_name, last_name, phone_number, email)
    add_contact_to_json(first_name, last_name, phone_number, email)
    add_contact_to_ismetify(first_name, last_name, phone_number, email)

# Ana menü içindeki fonksiyonlar
def list_contacts_menu():
    contacts = list_contacts()
    if not contacts:
        print("Listelenecek kişi bulunamadı.")
    else:
        for contact in contacts:
            print("Ad: {}, Soyad: {}, Telefon: {}, E-posta: {}".format(contact[1], contact[2], contact[3], contact[4]))

# Kişileri Listeleme işlemi
def list_contacts():
    conn = sqlite3.connect("SQLData/mydatabase.db")
    cursor = conn.cursor()

    # Varsayılan olarak, ad ve soyada göre sırala
    cursor.execute("SELECT * FROM contacts ORDER BY first_name, last_name")

    contacts = cursor.fetchall()
    conn.close()

    return contacts
# SQLite veritabanından kişi silme fonksiyonu
def delete_contact_from_sqlite(first_name, last_name, email):
    conn = sqlite3.connect("SQLData/mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM contacts WHERE first_name = ? AND last_name = ? AND email = ?", (first_name, last_name, email))
    existing_contact = cursor.fetchone()

    if existing_contact:
        contact_id = existing_contact[0]
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()
        print("Contact deleted successfully from SQLite.")
    else:
        print("Contact not found in SQLite.")

# CSV verilerinden kişi silme fonksiyonu
def delete_contact_from_csv(first_name, last_name, email):
    with open("CSVData/contacts.csv", 'r') as file:
        csv_data = list(csv.reader(file))

    deleted = False
    for row in csv_data:
        if row[0] == first_name and row[1] == last_name and row[3] == email:
            csv_data.remove(row)
            deleted = True

    if deleted:
        with open("CSVData/contacts.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)
        print("Contact deleted successfully from CSV.")
    else:
        print("Contact not found in CSV.")

# JSON verilerinden kişi silme fonksiyonu
def delete_contact_from_json(first_name, last_name, email):
    json_file = "JSONData/contacts.json"

    if not os.path.exists(json_file):
        print("Contact not found in JSON.")
        return

    with open(json_file, 'r') as file:
        json_data = json.load(file)

    deleted = False
    for contact in json_data:
        if contact.get("first_name") == first_name and contact.get("last_name") == last_name and contact.get("email") == email:
            json_data.remove(contact)
            deleted = True

    if deleted:
        with open(json_file, 'w') as file:
            json.dump(json_data, file, indent=4)
        print("Contact deleted successfully from JSON.")
    else:
        print("Contact not found in JSON.")

# İsmetify verilerinden kişi silme fonksiyonu
def delete_contact_from_ismetify(first_name, last_name, email):
    ismetify_file = "IsmetifyData/contacts.txt"

    if not os.path.exists(ismetify_file):
        print("Contact not found in İsmetify.")
        return

    with open(ismetify_file, 'r') as file:
        lines = file.readlines()

    deleted = False
    with open(ismetify_file, 'w') as file:
        for line in lines:
            contact_data = line.strip().split('|')
            if contact_data[0] == first_name and contact_data[1] == last_name and contact_data[3] == email:
                deleted = True
            else:
                file.write(line)

    if deleted:
        print("Contact deleted successfully from İsmetify.")
    else:
        print("Contact not found in İsmetify.")

# Kişiyi tüm veri kaynaklarından silen fonksiyon
def delete_contact_from_all_sources(first_name, last_name, email):
    delete_contact_from_sqlite(first_name, last_name, email)
    delete_contact_from_csv(first_name, last_name, email)
    delete_contact_from_json(first_name, last_name, email)
    delete_contact_from_ismetify(first_name, last_name, email)

# Ana menü içindeki fonksiyonlar
def edit_contact_menu():
    contacts = list_contacts()
    if not contacts:
        print("Düzenlenecek kişi bulunamadı.")
    else:
        for index, contact in enumerate(contacts):
            print("{}. Ad: {}, Soyad: {}, Telefon: {}, E-posta: {}".format(index, contact[1], contact[2], contact[3], contact[4]))
        contact_index = int(input("Düzenlemek istediğiniz kişinin sıra numarasını girin 0'dan başlar. (q: İptal): "))
        
        if contact_index == 'q':
            print("İptal edildi.")
        elif 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            first_name, last_name, phone_number, email = contact[1], contact[2], contact[3], contact[4]

            # Düzenlenecek kişinin bilgilerini göster
            print("Düzenleniyor: ")
            print("Ad: {}".format(first_name))
            print("Soyad: {}".format(last_name))
            print("Telefon Numarası: {}".format(phone_number))
            print("E-posta: {}".format(email))

            # Yeni bilgileri al
            new_first_name = input("Yeni Ad: ")
            new_last_name = input("Yeni Soyad: ")
            new_phone_number = input("Yeni Telefon Numarası: ")
            new_email = input("Yeni E-posta: ")

            # Kişiyi güncelle
            delete_contact_from_all_sources(first_name, last_name, email)
            add_contact_to_all_sources(new_first_name, new_last_name, new_phone_number, new_email)
            print("Kişi başarıyla güncellendi.")
        else:
            print("Geçersiz bir sıra numarası girdiniz.")

def main_menu():
    menu_title = "Ana Menü"
    menu_items = ["Kişi Ekle", "Kişi Sil", "Kişileri Listele", "Kişi Düzenle", "Yedekten Geri Yükle", "Çıkış"]
    menu = TerminalMenu(menu_items, title=menu_title)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            first_name = input("Ad: ")
            last_name = input("Soyad: ")
            phone_number = input("Telefon Numarası: ")
            email = input("E-posta: ")
            add_contact_to_all_sources(first_name, last_name, phone_number, email)
        elif selected_index == 1:
            first_name = input("Ad: ")
            last_name = input("Soyad: ")
            email = input("E-posta: ")
            delete_contact_from_all_sources(first_name, last_name, email)
        elif selected_index == 2:
            list_contacts_menu()
        elif selected_index == 3:
            edit_contact_menu()
        elif selected_index == 4:
            # Yedekten Geri Yükleme işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 5:
            print("Çıkış yapılıyor...")
            break


if __name__ == "__main__":
    create_folders()
    create_sqlite_database()
    create_data_files()
    main_menu()
