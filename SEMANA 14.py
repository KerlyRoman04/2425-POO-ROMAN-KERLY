import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame de entrada de datos
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(self.frame_inputs, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_inputs, text="Hora:").grid(row=1, column=0)
        self.time_entry = tk.Entry(self.frame_inputs)
        self.time_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_inputs, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_inputs)
        self.desc_entry.grid(row=2, column=1, padx=5)

        # Botón para agregar evento
        self.add_button = tk.Button(self.frame_inputs, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10)

        # Botón para eliminar evento seleccionado
        self.del_button = tk.Button(self.root, text="Eliminar Evento", command=self.delete_event)
        self.del_button.pack(pady=5)

        # Botón para salir
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()
        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Error", "Selecciona un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
