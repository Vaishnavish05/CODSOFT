import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

listbox = tk.Listbox(root, selectbackground="light blue", selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)


entry = tk.Entry(root, width=40)
entry.pack(pady=10, padx=10, fill=tk.BOTH)


add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

add_button.pack(pady=5, padx=10, fill=tk.BOTH)
remove_button.pack(pady=5, padx=10, fill=tk.BOTH)

root.mainloop()
