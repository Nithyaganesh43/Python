import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['e-donate']
help_requests_collection = db['help_requests']
category_collection = db['category_amounts']

def submit():
    global request_data
    
    if donate_var.get() == 1:
        try:
            amount_needed = float(request_data['amount_needed'])
        except ValueError:
            messagebox.showerror("Error", "Invalid amount needed.")
            return

        if 'type' in request_data:
            selected_type = request_data['type']
        else:
            messagebox.showerror("Error", "No type available for this request.")
            return

        category_doc = category_collection.find_one({"category": selected_type})
        if category_doc and category_doc['amount'] >= amount_needed:
            category_collection.update_one({"category": selected_type}, {"$inc": {"amount": -amount_needed}})
            help_requests_collection.update_one({"_id": request_data["_id"]}, {"$set": {"status": "Donated"}})
            messagebox.showinfo("Success", "Donation successful!")
        else:
            messagebox.showerror("Error", f"Insufficient funds for {selected_type}.")
    elif declaim_var.get() == 1:
        help_requests_collection.delete_one({"_id": request_data["_id"]})
        messagebox.showinfo("Success", "Request declined!")
    else:
        messagebox.showerror("Error", "Please select an action.")

def manager_view():
    global request_data, donate_var, declaim_var
    
    manager_window = tk.Tk()
    manager_window.title("Manager View")
    manager_window.configure(background='light grey') 
    help_requests = list(help_requests_collection.find())
    for idx, request_data in enumerate(help_requests):
        tk.Label(manager_window, text=f"Request Number: {request_data['request_number']}", bg="light grey").grid(row=idx*5, column=0, padx=5, pady=5, sticky="w")
        tk.Label(manager_window, text=f"Organization Name: {request_data['org_name']}", bg="light grey").grid(row=idx*5+1, column=0, padx=5, pady=5, sticky="w")
        tk.Label(manager_window, text=f"Amount Needed: {request_data['amount_needed']}", bg="light grey").grid(row=idx*5+2, column=0, padx=5, pady=5, sticky="w")
        
        if 'type' in request_data:
            tk.Label(manager_window, text=f"Type: {request_data['type']}", bg="light grey").grid(row=idx*5+3, column=0, padx=5, pady=5, sticky="w")
        else:
            tk.Label(manager_window, text="Type: None", bg="light grey").grid(row=idx*5+3, column=0, padx=5, pady=5, sticky="w")
        
        tk.Label(manager_window, text=f"Status: {request_data['status']}", bg="light grey").grid(row=idx*5+4, column=0, padx=5, pady=5, sticky="w")

        donate_var = tk.IntVar()
        declaim_var = tk.IntVar()
        tk.Checkbutton(manager_window, text="Donate", variable=donate_var).grid(row=idx*5, column=1, padx=5, pady=5, sticky="w")
        tk.Checkbutton(manager_window, text="Decline", variable=declaim_var).grid(row=idx*5, column=2, padx=5, pady=5, sticky="w")

    submit_button = tk.Button(manager_window, text="Submit", command=submit, bg="light grey")  # Set button background color
    submit_button.grid(row=len(help_requests)*5, column=0, columnspan=3, pady=10)

    for i in range(len(help_requests) * 5 + 1):
        manager_window.grid_rowconfigure(i, weight=1, uniform="row")
    for i in range(3):
        manager_window.grid_columnconfigure(i, weight=1, uniform="col")

    manager_window.mainloop()

if __name__ == "__main__":
    manager_view()
