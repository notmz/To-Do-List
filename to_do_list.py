import tkinter as tk
from tkinter import messagebox

# Color scheme
bg_color = "#1c1c1c"         # Black background
accent_color = "#FFD700"     # Gold
entry_bg = "#333333"         # Dark grey 

# List to store task rows
tasks_items = []

def create_task(task_text, completed=False):
    # Frame for the task row
    task_frame = tk.Frame(tasks_frame, bg=bg_color)
    task_frame.pack(fill="x", pady=2)
    
    # Boolean variable for checkbutton state
    var = tk.BooleanVar(value=completed)
    
    # Checkbutton (Gold)
    check = tk.Checkbutton(
        task_frame,
        variable=var,
        bg=bg_color,
        fg=accent_color,
        activebackground=bg_color,
        activeforeground=accent_color,
        highlightthickness=2,
        highlightbackground=accent_color,
        bd=1,
        relief="solid"
    )
    check.pack(side="left", padx=5)
    
    # Label displaying the task text
    label = tk.Label(task_frame, text=task_text, bg=bg_color, fg=accent_color)
    label.pack(side="left", padx=5)
    
    tasks_items.append((task_frame, var, task_text))

def add_task():
    task = task_entry.get()
    if task:
        create_task(task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    global tasks_items
    # Remove tasks (checkbox checked)
    for task in tasks_items[:]:
        frame, var, text = task
        if var.get():
            frame.destroy()
            tasks_items.remove(task)

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks_items:
            frame, var, text = task
            state = "1" if var.get() else "0"
            file.write(f"{text}|{state}\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 2:
                    text, state = parts
                    create_task(text, completed=(state == "1"))
    except FileNotFoundError:
        pass

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg=bg_color)

# Set fixed window size and center it on the screen
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a border frame with gold accent
border_frame = tk.Frame(root, bg=accent_color, padx=3, pady=3)
border_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Main frame inside the border
main_frame = tk.Frame(border_frame, bg=bg_color)
main_frame.pack(fill="both", expand=True)

# Entry box for tasks
task_entry = tk.Entry(main_frame, width=40, bg=entry_bg, fg=accent_color, insertbackground=accent_color)
task_entry.pack(pady=5)

# Buttons frame
btn_frame = tk.Frame(main_frame, bg=bg_color)
btn_frame.pack()

# Button configuration with gold border effect
button_opts = {
    "bg": bg_color,
    "fg": accent_color,
    "activebackground": accent_color,
    "activeforeground": bg_color,
    "relief": "raised",
    "bd": 0,
    "highlightthickness": 2,
    "highlightbackground": accent_color,
    "padx": 10,
    "pady": 5
}

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, **button_opts)
add_btn.pack(side=tk.LEFT, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Completed Tasks", command=remove_task, **button_opts)
remove_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(btn_frame, text="Save Tasks", command=save_tasks, **button_opts)
save_btn.pack(side=tk.LEFT, padx=5)

# Frame to hold task rows
tasks_frame = tk.Frame(main_frame, bg=bg_color)
tasks_frame.pack(fill="both", expand=True, pady=5)

# Load tasks from file (if any)
load_tasks()
root.mainloop()
