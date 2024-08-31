import tkinter as tk
from tkinter import messagebox

def remove_common_chars(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    
    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    
    return len(list1 + list2)

def flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]

def get_flames_relationship(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    count = remove_common_chars(name1, name2)
    result = flames_result(count)
    return result

def on_submit():
    name1 = entry1.get()
    name2 = entry2.get()
    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Please enter both names.")
        return
    
    relationship = get_flames_relationship(name1, name2)
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    
    messagebox.showinfo("Relationship Status", f"Relationship status: {relationships[relationship]}")

def on_restart():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("FLAMES Game")
root.geometry("250x250")
root.configure(bg="gray")

# Create and place labels and entries
label1 = tk.Label(root, text="Enter the first name:", bg="gray")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter the second name:", bg="gray")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit, bg="green", fg="white")
submit_button.pack(pady=5)

# Create and place the restart button
restart_button = tk.Button(root, text="Restart", command=on_restart, bg="green", fg="white")
restart_button.pack(pady=5)

# Run the main loop
root.mainloop()
