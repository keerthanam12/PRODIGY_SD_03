import tkinter as tk
from tkinter import messagebox
import json

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        # Load existing contacts from a JSON file or initialize an empty list
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

        # Create the contact listbox
        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create buttons to perform actions
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contact", command=self.view_contact)
        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.save_button = tk.Button(root, text="Save Contacts", command=self.save_contacts)

        self.add_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.view_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.edit_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.delete_button.pack(padx=10, pady=5, fill=tk.BOTH)
        self.save_button.pack(padx=10, pady=5, fill=tk.BOTH)

        # Populate the contact listbox with contact names
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact["name"])

    def add_contact(self):
        # Create a new window for adding a contact
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")

        # Create labels and entry fields
        name_label = tk.Label(add_window, text="Name:")
        phone_label = tk.Label(add_window, text="Phone:")
        email_label = tk.Label(add_window, text="Email:")

        name_entry = tk.Entry(add_window)
        phone_entry = tk.Entry(add_window)
        email_entry = tk.Entry(add_window)

        name_label.grid(row=0, column=0, padx=5, pady=5)
        phone_label.grid(row=1, column=0, padx=5, pady=5)
        email_label.grid(row=2, column=0, padx=5, pady=5)

        name_entry.grid(row=0, column=1, padx=5, pady=5)
        phone_entry.grid(row=1, column=1, padx=5, pady=5)
        email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Function to add a new contact
        def save_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()

            if name and phone and email:
                self.contacts.append({"name": name, "phone": phone, "email": email})
                self.contact_listbox.insert(tk.END, name)
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        save_button = tk.Button(add_window, text="Save", command=save_contact)
        save_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def view_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact_index = selected_index[0]
            contact = self.contacts[contact_index]
            messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
        else:
            messagebox.showerror("Error", "Please select a contact to view.")

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact_index = selected_index[0]
            contact = self.contacts[contact_index]

            # Create a new window for editing a contact
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Contact")

            # Create labels and entry fields with the current contact details
            name_label = tk.Label(edit_window, text="Name:")
            phone_label = tk.Label(edit_window, text="Phone:")
            email_label = tk.Label(edit_window, text="Email:")

            name_entry = tk.Entry(edit_window)
            phone_entry = tk.Entry(edit_window)
            email_entry = tk.Entry(edit_window)

            name_entry.insert(0, contact["name"])
            phone_entry.insert(0, contact["phone"])
            email_entry.insert(0, contact["email"])

            name_label.grid(row=0, column=0, padx=5, pady=5)
            phone_label.grid(row=1, column=0, padx=5, pady=5)
            email_label.grid(row=2, column=0, padx=5, pady=5)

            name_entry.grid(row=0, column=1, padx=5, pady=5)
            phone_entry.grid(row=1, column=1, padx=5, pady=5)
            email_entry.grid(row=2, column=1, padx=5, pady=5)

            # Function to save edited contact
            def save_edited_contact():
                name = name_entry.get()
                phone = phone_entry.get()
                email = email_entry.get()

                if name and phone and email:
                    self.contacts[contact_index] = {"name": name, "phone": phone, "email": email}
                    self.contact_listbox.delete(contact_index)
                    self.contact_listbox.insert(contact_index, name)
                    edit_window.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields.")

            save_button = tk.Button(edit_window, text="Save", command=save_edited_contact)
            save_button.grid(row=3, columnspan=2, padx=5, pady=10)
        else:
            messagebox.showerror("Error", "Please select a contact to edit.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            confirmation = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if confirmation:
                contact_index = selected_index[0]
                self.contacts.pop(contact_index)
                self.contact_listbox.delete(contact_index)
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()