import sqlite3
from tkinter import Tk, Listbox, Scrollbar, Frame, Button, Entry, messagebox, Label, END, IntVar, Radiobutton
from ttkbootstrap import Style

# Andmebaasi teekond ja tabel
database_path = "C:/sqlite/epood_kjoarand.db"
table_name = "kjoarand"

# Loome andmebaasi ühenduse
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Funktsioon, mis tagastab lehekülje andmed
def get_page_data(page_num, page_size):
    offset = (page_num - 1) * page_size
    query = f"SELECT * FROM {table_name} LIMIT {page_size} OFFSET {offset}"
    cursor.execute(query)
    return cursor.fetchall()

# Funktsioon, mis arvutab lehekülgede arvu
def calculate_page_count(page_size):
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    total_records = cursor.fetchone()[0]
    return (total_records // page_size) + 1

# Funktsioon, mis kuvab lehekülje andmed
def display_page(page_num, page_size):
    listbox.delete(0, END)
    data = get_page_data(page_num, page_size)
    for row in data:
        for i, value in enumerate(row):
            listbox.insert("end", f"{columns[i]}: {value}")
        listbox.insert("end", "------------------------")

# Funktsioon, mis kerib edasi
def next_page():
    global current_page
    if current_page < page_count:
        current_page += 1
        display_page(current_page, current_page_size.get())

# Funktsioon, mis kerib tagasi
def previous_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        display_page(current_page, current_page_size.get())

# Funktsioon, mis otsib andmeid
def search_data():
    search_term = search_entry.get()
    query = f"SELECT * FROM {table_name} WHERE 'First Name' LIKE ? OR 'Last Name' LIKE ? OR Email LIKE ? OR 'Car Make' LIKE ? OR 'Car Model' LIKE ? OR 'Car Year' LIKE ? OR 'Car Price' LIKE ?"
    cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
    search_results = cursor.fetchall()
    if not search_results:
        messagebox.showinfo("Otsingu tulemused", "Andmeid ei leitud vastavalt otsingukriteeriumidele.")
    else:
        listbox.delete(0, END)
        for row in search_results:
            for i, value in enumerate(row):
                listbox.insert("end", f"{columns[i]}: {value}")
            listbox.insert("end", "------------------------")

# Funktsioon, mis lisab andmeid
def add_data():
    values = [entry.get() for entry in add_entries]
    if any(value == "" for value in values):
        messagebox.showwarning("Andmete lisamine", "Palun täitke kõik väljad.")
        return
    query = f"INSERT INTO {table_name} ('First Name', 'Last Name', Email, 'Car Make', 'Car Model', 'Car Year', 'Car Price') VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, values)
    conn.commit()
    messagebox.showinfo("Andmete lisamine", "Andmed on edukalt lisatud.")
    # Clear the entry fields
    for entry in add_entries:
        entry.delete(0, END)
    # Refresh the current page to display the updated data
    display_page(current_page, current_page_size.get())

# Funktsioon, mis kustutab valitud rea
def delete_row():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Rea kustutamine", "Palun valige rida, mida soovite kustutada.")
        return
    result = messagebox.askyesno("Rea kustutamine", "Kas olete kindel, et soovite valitud rea kustutada?")
    if result == "yes":
        for index in reversed(selected_indices):
            data = get_page_data(current_page, current_page_size.get())
            row_index = index % len(data)
            record_id = data[row_index][0]
            query = f"DELETE FROM {table_name} WHERE ID = ?"
            cursor.execute(query, (record_id,))
            conn.commit()
        display_page(current_page, current_page_size.get())
        messagebox.showinfo("Rea kustutamine", "Valitud read on edukalt kustutatud.")

# Loome tkinteri akna
root = Tk()
root.title("Andmete kuvamine")

# Lae ttkbootstrap stiil
style = Style(theme="darkly")

# Loome keritava raami
frame = Frame(root)
frame.pack(fill="both", expand=True)

# Loome keritava listboxi
listbox = Listbox(frame)
listbox.pack(side="left", fill="both", expand=True)

# Loome kerimisribad
yscrollbar = Scrollbar(frame, orient="vertical")
yscrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=yscrollbar.set)
yscrollbar.config(command=listbox.yview)

# Nupud lehekülje kerimiseks
button_frame = Frame(root)
button_frame.pack()

previous_button = Button(button_frame, text="Eelmine leht", command=previous_page)
previous_button.pack(side="left")

next_button = Button(button_frame, text="Järgmine leht", command=next_page)
next_button.pack(side="left")

# Otsinguväljad
search_label = Label(root, text="Otsi:")
search_label.pack()

search_entry = Entry(root)
search_entry.pack()

search_button = Button(root, text="Otsi", command=search_data)
search_button.pack()

# Andmete lisamise väljad
add_label = Label(root, text="Lisa andmed:")
add_label.pack()

add_entries = []
add_fields = ["First Name", "Last Name", "Email", "Car Make", "Car Model", "Car Year", "Car Price"]

for field in add_fields:
    add_label = Label(root, text=field + ":")
    add_label.pack()

    add_entry = Entry(root)
    add_entry.pack()

    add_entries.append(add_entry)

add_button = Button(root, text="Lisa", command=add_data)
add_button.pack()

# Kustutamise nupp
delete_button = Button(root, text="Kustuta rida", command=delete_row)
delete_button.pack()

# Lehekülje suuruse valimise nupp
page_size_label = Label(root, text="Lehekülje suurus:")
page_size_label.pack()

current_page_size = IntVar(value=5)

def update_page_size():
    global current_page
    current_page = 1
    display_page(current_page, current_page_size.get())

page_size_5_button = Radiobutton(root, text="5", variable=current_page_size, value=5, command=update_page_size)
page_size_5_button.pack()

page_size_10_button = Radiobutton(root, text="10", variable=current_page_size, value=10, command=update_page_size)
page_size_10_button.pack()

page_size_25_button = Radiobutton(root, text="25", variable=current_page_size, value=25, command=update_page_size)
page_size_25_button.pack()

page_size_50_button = Radiobutton(root, text="50", variable=current_page_size, value=50, command=update_page_size)
page_size_50_button.pack()

# Kuvame esimese lehekülje andmed
current_page = 1
columns = ["ID", "First Name", "Last Name", "Email", "Car Make", "Car Model", "Car Year", "Car Price"]
page_count = calculate_page_count(current_page_size.get())
display_page(current_page, current_page_size.get())

# Käivitame tkinteri akna sündmuse tsükli
root.mainloop()

# Sulgeme andmebaasi ühenduse
cursor.close()
conn.close()