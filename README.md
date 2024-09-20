
# Contact Management System

This project is a contact management system that stores, manages, and organizes contact information in multiple formats: SQLite, CSV, JSON, and a custom format called İsmetify. The system allows you to create, read, update, and delete contacts through a terminal-based menu system. The contact data is backed up automatically, and you can also restore it from previous backups.

## Features

- **Multiple Data Sources**: 
  - SQLite database (`SQLData/mydatabase.db`)
  - CSV file (`CSVData/contacts.csv`)
  - JSON file (`JSONData/contacts.json`)
  - İsmetify file (`IsmetifyData/contacts.txt`)

- **CRUD Operations**:
  - **Add Contacts**: Add a new contact to all formats.
  - **List Contacts**: Display all contacts stored in the SQLite database.
  - **Edit Contacts**: Edit contact information and update all formats.
  - **Delete Contacts**: Remove a contact from all formats.

- **Backup and Restore**:
  - **Backup**: Automatically backs up all data into a `Backup` folder.
  - **Restore**: Restore data from the `Backup` folder.

- **Data Formats**:
  - **SQLite**: Stores structured contact data in an SQLite database.
  - **CSV**: Stores contact data as a CSV file.
  - **JSON**: Stores contact data in JSON format.
  - **İsmetify**: Stores contact data in a custom plain text format where each entry is separated by a pipe (`|`).

## File Structure

- **`SQLData/`**: Contains the SQLite database (`mydatabase.db`).
- **`CSVData/`**: Contains the CSV file (`contacts.csv`).
- **`JSONData/`**: Contains the JSON file (`contacts.json`).
- **`IsmetifyData/`**: Contains the custom İsmetify text file (`contacts.txt`).
- **`Backup/`**: Stores backup files for each format.

## Setup

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install sqlite3 csv json os shutil simple_term_menu
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Dependencies

The project relies on the following libraries:

- `sqlite3`: For handling SQLite database operations.
- `csv`: For handling CSV file operations.
- `json`: For handling JSON file operations.
- `os`: For managing directories and file paths.
- `shutil`: For file backup and restoration.
- `simple_term_menu`: For creating a simple terminal-based menu system.

## Usage

When you run the program, you'll see a terminal-based menu with the following options:

1. **Add Contact**: Prompts you to input contact details and adds them to all formats.
2. **Delete Contact**: Removes a contact from all formats.
3. **List Contacts**: Displays all contacts from the SQLite database.
4. **Edit Contact**: Allows you to edit contact details and updates all formats.
5. **Restore Backup**: Restores contact data from the `Backup` folder.
6. **Exit**: Closes the program.

## Backup and Restore

- **Backup**: Every time you add, edit, or delete a contact, the system automatically creates a backup of all data files in the `Backup` folder.
- **Restore**: You can restore the contact data from backups by selecting the "Restore Backup" option from the main menu.

## Future Enhancements

- Add support for importing and exporting data.
- Implement sorting and filtering functionalities for contact listing.
- Add error handling for invalid inputs.

## License

This project is open-source and available under the [MIT License](LICENSE).
