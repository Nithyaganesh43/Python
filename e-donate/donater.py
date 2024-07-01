import tkinter as tk
from tkinter import messagebox,simpledialog 
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['e-donate']
donations_collection=db['donations']
category_collection=db['category_amounts']

initial_categories = {
    "Cancer Patients": 0,
    "Childs": 0,
    "Age Old Peoples": 0,
    "Physically Challenged": 0,
    "All of the above": 0
}

if category_collection.count_documents({}) == 0:
    category_collection.insert_many([{"category": category, "amount": amount} for category, amount in initial_categories.items()])

def donate():
    name = name_entry.get()
    amount = amount_entry.get()
    selected_category = category_var.get()

    if not name or not amount or not selected_category:
        messagebox.showerror("Error", "Please fill in all fields and select a category.")
        return

    confirm_payment = messagebox.askyesno("Payment Confirmation", f"Please pay Rs. {amount} to Google Pay number 9042421622. After payment, click 'Yes'.")
    if not confirm_payment:
        return

    transaction_id = simpledialog.askstring("Transaction ID", "Enter Transaction ID:")
    if not transaction_id:
        messagebox.showerror("Error", "Transaction ID is required.")
        return

    category_collection.update_one({"category": selected_category}, {"$inc": {"amount": int(amount)}})

    donation_data = {
        "name": name,
        "amount": amount,
        "categories": [selected_category],
        "transaction_id": transaction_id
    }
    donations_collection.insert_one(donation_data)

    messagebox.showinfo("Success", "Payment successful! Thank you for donating.")

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_var.set(categories[0])

root = tk.Tk()
root.title("Donation Form")
root.configure(background='grey')

tk.Label(root, text="Donater Name:", fg="white", bg="grey").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount (Rupees):", fg="white", bg="grey").grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Category:", fg="white", bg="grey").grid(row=2, column=0, padx=5, pady=5)
categories = ["Cancer Patients", "Childs", "Age Old Peoples", "Physically Challenged", "All of the above"]
category_var = tk.StringVar(root)
category_var.set(categories[0])
category_dropdown = tk.OptionMenu(root, category_var, *categories)
category_dropdown.config(fg="white", bg="grey")
category_dropdown.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

donate_button = tk.Button(root, text="Donate", command=donate, bg="light grey", fg="black")
donate_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
