import tkinter as tk
from tkinter import messagebox


contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()  # Get text from a Text widget
    
    if not name:
        messagebox.showerror("Error", "Name is required.")
        return
    
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    
    messagebox.showinfo("Success", "Contact added successfully.")
    clear_entries()
    update_contact_list()

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact['name'] + ' - ' + contact['phone'])

def search_contact():
    search_term = search_entry.get().strip().lower()
    if not search_term:
        messagebox.showerror("Error", "Please enter a search term.")
        return
    
    found_contacts = []
    for contact in contacts:
        if (search_term in contact['name'].lower()) or (search_term in contact['phone']):
            found_contacts.append(contact['name'] + ' - ' + contact['phone'])
    
    contact_listbox.delete(0, tk.END)
    if found_contacts:
        for contact in found_contacts:
            contact_listbox.insert(tk.END, contact)
    else:
        messagebox.showinfo("No Results", "No contacts found.")

def delete_contact():
    try:
        index = contact_listbox.curselection()[0]
        del contacts[index]
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    search_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
address_entry = tk.Text(root, width=30, height=5)
address_entry.grid(row=3, column=1, padx=10, pady=5)


add_button = tk.Button(root, text="Add Contact", width=20, command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

search_entry = tk.Entry(root, width=30)
search_entry.grid(row=5, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search Contact", width=20, command=search_contact)
search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", width=20, command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)


contact_listbox = tk.Listbox(root, width=50)
contact_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)


scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=8, column=2, padx=0, pady=5, sticky=tk.N+tk.S)
contact_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_listbox.yview)


update_contact_list()


root.mainloop()
