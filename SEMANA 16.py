import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.tasks = []

        # Entrada de texto
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        frame = tk.Frame(root)
        frame.pack()

        add_button = tk.Button(frame, text="Añadir Tarea", command=self.add_task)
        add_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(frame, text="Completar", command=self.mark_completed)
        complete_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(frame, text="Eliminar", command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=45, height=15, selectbackground="lightblue", font=("Arial", 12))
        self.listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.mark_completed())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
        else:
            messagebox.showinfo("Seleccionar", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Seleccionar", "Selecciona una tarea para eliminarla.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"[✓] {task['task']}" if task["completed"] else f"[ ] {task['task']}"
            self.listbox.insert(tk.END, display)
            if task["completed"]:
                self.listbox.itemconfig(tk.END, fg="gray")
            else:
                self.listbox.itemconfig(tk.END, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
