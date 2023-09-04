import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    if complexity == "Low":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        result_label.config(text="Select complexity level.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

app = tk.Tk()
app.title("Password Generator")

length_label = tk.Label(app, text="Password Length:")
length_entry = tk.Entry(app)
complexity_label = tk.Label(app, text="Complexity Level:")
complexity_var = tk.StringVar()
complexity_var.set("Low")
complexity_option = tk.OptionMenu(app, complexity_var, "Low", "Medium", "High")
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
result_label = tk.Label(app, text="", wraplength=300)

length_label.pack()
length_entry.pack()
complexity_label.pack()
complexity_option.pack()
generate_button.pack()
result_label.pack()

app.mainloop()
