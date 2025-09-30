import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)

        # Check if already marked
        if task.startswith("✔ "):
            # Unmark if already marked
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task[2:])
        else:
            # Mark as completed
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, "✔ " + task)

    except:
        messagebox.showwarning("Warning", "Please select a task to mark!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry box
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark/Unmark Completed", width=20, command=mark_task)
mark_button.pack(pady=5)

# Listbox
tasks_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Run app
root.mainloop()
