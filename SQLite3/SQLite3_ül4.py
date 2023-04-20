import sqlite3
import tkinter as tk
from tkinter import ttk

# Create a connection to the database
conn = sqlite3.connect('C:/sqlite/epood_kjoarand.db')
c = conn.cursor()

# Define a function to retrieve data from the table and display it in the treeview widget
def display_data():
    # Clear the treeview widget
    for i in treeview.get_children():
        treeview.delete(i)
    # Retrieve the selected number of rows from the table
    offset = page_size * (current_page - 1)
    c.execute(f"SELECT * FROM kjoarand LIMIT {page_size} OFFSET {offset}")
    data = c.fetchall()
    # Insert the data into the treeview widget
    for row in data:
        treeview.insert("", "end", values=row)

# Define a function to update the current page number and display the data on the new page
def update_page(*args):
    global current_page
    current_page = int(scrollbar.get())
    display_data()

# Create the main window
root = tk.Tk()
root.title("Data Viewer")

# Create a treeview widget to display the data
treeview = ttk.Treeview(root, columns=("First Name", "Last Name", "Email", "Car Make", "Car Model", "Car Year", "Car Price"))
treeview.heading("#0", text="ID")
treeview.heading("First Name", text="First Name")
treeview.heading("Last Name", text="Last Name")
treeview.heading("Email", text="Email")
treeview.heading("Car Make", text="Car Make")
treeview.heading("Car Model", text="Car Model")
treeview.heading("Car Year", text="Car Year")
treeview.heading("Car Price", text="Car Price")
treeview.pack()

# Add a frame to contain the scrollbar and the page size selector
frame = tk.Frame(root)
frame.pack(side="bottom")

# Add a scrollbar to navigate between pages
scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=update_page)
scrollbar.pack(side="bottom", fill="x")

# Add a label to display the page size selector
label = tk.Label(frame, text="Rows per page:")
label.pack(side="left")

# Add a combobox to select the number of rows to display per page
page_size_var = tk.StringVar()
page_size_var.set("10")
page_size_choices = ["5", "10", "25", "50", "100"]
page_size_combobox = ttk.Combobox(frame, textvariable=page_size_var, values=page_size_choices, state="readonly")
page_size_combobox.pack(side="left")

# Bind the combobox to the display_data() function so that the data is updated when the page size changes
page_size_combobox.bind("<<ComboboxSelected>>", lambda e: display_data())

# Initialize global variables for the current page and page size
current_page = 1
page_size = int(page_size_var.get())

# Call the display_data() function to display the initial data
display_data()

# Start the main event loop
root.mainloop()

# Close the connection to the database
conn.close()
