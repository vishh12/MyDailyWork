import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Styled To-Do List")
        self.root.geometry("400x400")
        self.root.configure(bg="#F5F5DC")  # Set background color

        # Task list storage
        self.tasks = []

        # Styled GUI Elements
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14), bg="#E6E6FA")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(
            root, text="Add Task", font=("Arial", 12, "bold"), bg="#ADD8E6", fg="black", command=self.add_task
        )
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(
            root, width=50, height=15, font=("Arial", 12), bg="#FFFACD", selectbackground="#FFD700"
        )
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(
            root, text="Mark Complete", font=("Arial", 12), bg="#90EE90", command=self.mark_complete
        )
        self.complete_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.delete_button = tk.Button(
            root, text="Delete Task", font=("Arial", 12), bg="red", command=self.delete_task
        )
        self.delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"{'[X]' if task['completed'] else '[ ]'} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
