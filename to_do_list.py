import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = {}

        
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10)

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_as_completed)
        self.mark_completed_button.pack(padx=10, pady=10)

    def add_task(self):
        task_name = self.task_entry.get()
        self.tasks[task_name] = {"completed": False}
        self.task_listbox.insert(tk.END, task_name)
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        task_name = self.task_listbox.get(tk.ACTIVE)
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.task_listbox.delete(tk.ACTIVE)

    def mark_task_as_completed(self):
        task_name = self.task_listbox.get(tk.ACTIVE)
        if task_name in self.tasks:
            self.tasks[task_name]["completed"] = True
            self.task_listbox.itemconfig(tk.ACTIVE, {'fg': 'green'})

root = tk.Tk()
root.title("To-Do List App")
app = ToDoListApp(root)
root.mainloop()
