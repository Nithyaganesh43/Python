import tkinter as tk
from tkinter import messagebox, simpledialog, OptionMenu
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['e-donate']
help_requests_collection = db['help_requests']

def submit_help():
    org_name = org_name_entry.get()
    amount_needed = amount_needed_entry.get()
    selected_type = type_var.get()

    if not org_name or not amount_needed or not selected_type:
        messagebox.showerror("Error", "Please fill in all fields and select a type.")
        return

    request_number = help_requests_collection.count_documents({}) + 1

    help_request_data = {
        "request_number": request_number,
        "org_name": org_name,
        "amount_needed": amount_needed,
        "type": selected_type,
        "status": "Pending"
    }
    help_requests_collection.insert_one(help_request_data)

    messagebox.showinfo("Success", "Information submitted successfully! Request number: {}".format(request_number))

def check_status():
    request_number = simpledialog.askinteger("Check Status", "Enter request number:")
    if not request_number:
        return

    request = help_requests_collection.find_one({"request_number": request_number})
    if request:
        status = request["status"]
        messagebox.showinfo("Status", f"Request number {request_number} status: {status}")
    else:
        messagebox.showerror("Error", f"Request number {request_number} not found.")

root = tk.Tk()
root.title("Help Request Form")
root.configure(background='grey')

tk.Label(root, text="Organization Name:", bg="grey", fg="white").grid(row=0, column=0, padx=5, pady=5)
org_name_entry = tk.Entry(root)
org_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount Needed:", bg="grey", fg="white").grid(row=1, column=0, padx=5, pady=5)
amount_needed_entry = tk.Entry(root)
amount_needed_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Type:", bg="grey", fg="white").grid(row=2, column=0, padx=5, pady=5)

types = ["Cancer Patients", "Childs", "Age Old Peoples", "Physically Challenged", "All of the above"]
type_var = tk.StringVar(root)
type_var.set(types[0])

type_dropdown = OptionMenu(root, type_var, *types)
type_dropdown.config(bg="grey", fg="white")
type_dropdown.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_help, bg="light grey", fg="black")
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

check_status_button = tk.Button(root, text="Check Status", command=check_status, bg="light grey", fg="black")
check_status_button.grid(row=4, column=0, columnspan=2, pady=10)

for i in range(5):
    root.grid_rowconfigure(i, weight=1, uniform="row")
for i in range(2):
    root.grid_columnconfigure(i, weight=1, uniform="col")

root.mainloop()
