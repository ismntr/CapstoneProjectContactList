import sqlite3
import csv
import json



# Create a connection to the SQLite database
conn = sqlite3.connect("SQLData/mydatabase.db")

# Create a cursor
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT,
                   last_name TEXT,
                   phone_number TEXT,
                   email TEXT,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')

# Değişiklikleri kaydet
conn.commit()

def add_contact(first_name, last_name, phone_number, email):
    # Check if a contact with the same name and email exists
    cursor.execute("SELECT id FROM contacts WHERE first_name = ? AND email = ?", (first_name, email))
    existing_contact = cursor.fetchone()

    if existing_contact:
        print("A contact with the same name and email already exists.")
    else:
        # Add a new contact
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?)",
                       (first_name, last_name, phone_number, email))
        conn.commit()
        print("Contact added successfully.")

# Call the add_contact function with the contact details
add_contact("John", "Doe", "555-123-4567", "john.doe@example.com")

# Close the database connection
conn.close()


# CSV verilerini okuma
def read_csv_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# CSV verilerini yazma
def write_csv_data(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

# CSV verilerini güncelleme
def update_csv_data(filename, row_index, column_index, new_value):
    data = read_csv_data(filename)
    data[row_index][column_index] = new_value
    write_csv_data(filename, data)

# CSV verilerini silme
def delete_csv_data(filename, row_index):
    data = read_csv_data(filename)
    del data[row_index]
    write_csv_data(filename, data)


# JSON verilerini okuma
def read_json_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# JSON verilerini yazma
def write_json_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# JSON verilerini güncelleme
def update_json_data(filename, key, new_value):
    data = read_json_data(filename)
    data[key] = new_value
    write_json_data(filename, data)

# JSON verilerini silme
def delete_json_data(filename, key):
    data = read_json_data(filename)
    del data[key]
    write_json_data(filename, data)

# İsmetify verilerini okuma
def read_ismetify_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split('|')
            data.append(row)
    return data

# İsmetify verilerini yazma
def write_ismetify_data(filename, data):
    with open(filename, 'w') as file:
        for row in data:
            line = '|'.join(row)
            file.write(line + '\n')

# İsmetify verilerini güncelleme
def update_ismetify_data(filename, row_index, column_index, new_value):
    data = read_ismetify_data(filename)
    data[row_index][column_index] = new_value
    write_ismetify_data(filename, data)

# İsmetify verilerini silme
def delete_ismetify_data(filename, row_index):
    data = read_ismetify_data(filename)
    del data[row_index]
    write_ismetify_data(filename, data)

from simple_term_menu import TerminalMenu

def main_menu():
    menu_title = "Ana Menü"
    menu_items = ["Kişi Ekle", "Kişi Sil", "Kişileri Listele", "Kişi Düzenle", "Yedekten Geri Yükle", "Çıkış"]
    menu = TerminalMenu(menu_items, title=menu_title)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            # Kişi Ekle işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 1:
            # Kişi Sil işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 2:
            # Kişileri Listele işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 3:
            # Kişi Düzenle işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 4:
            # Yedekten Geri Yükle işlemi için gerekli kodu buraya ekleyin
            pass
        elif selected_index == 5:
            print("Çıkış yapılıyor...")
            break

if __name__ == "__main__":
    main_menu()
