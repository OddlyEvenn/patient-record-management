# gui.py

import tkinter as tk
from tkinter import ttk, messagebox

from modules.clear_fields import clear_entry_fields

class PatientGUI:
    def __init__(self, root, callbacks, logo_path=None):
        self.root = root
        self.root.title("Patient Record Management System")
        self.root.geometry("950x550")
        self.root.resizable(False, False)

        self.callbacks = callbacks  # Dictionary of callback functions

        if logo_path:
            self.logo = tk.PhotoImage(file=logo_path)
            tk.Label(root, image=self.logo).pack(pady=5)

        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack()

        # Input Fields in 5 rows x 2 columns
        fields = [
            "Patient Id", "Name", "Age", "Gender", "Diagnosis",
            "Medical History", "Current Treatment", "Date of registration",
            "Fees", "Email-id"
        ]

        for idx, field in enumerate(fields):
            row = idx % 5
            col = idx // 5

            label = ttk.Label(frame, text=field + ":")
            entry = ttk.Entry(frame, width=30)

            label.grid(row=row, column=col * 2, sticky='e', padx=5, pady=5)
            entry.grid(row=row, column=col * 2 + 1, padx=5, pady=5)

            self.entries[field] = entry

        # Buttons
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack()

        buttons = [
            ("Add Patient", self.callbacks["add"]),
            ("Edit Patient", self.callbacks["edit"]),
            ("Delete Patient", self.callbacks["delete"]),
            ("Display Patient", self.callbacks["display"]),
            ("Clear Fields", lambda: clear_entry_fields(self.entries)),
            ("Export CSV", self.callbacks.get("export", lambda: None)),
            ("Summary", self.callbacks.get("summary", lambda: None)),
        ]

        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(button_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=8, pady=10)

        # Status Bar
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken', anchor='w')
        status_bar.pack(fill='x', side='bottom')

    def get_form_data(self):
        return {key: entry.get().strip() for key, entry in self.entries.items()}

    def set_form_data(self, data):
        for key, value in data.items():
            if key in self.entries:
                self.entries[key].delete(0, 'end')
                self.entries[key].insert(0, str(value))

    def show_message(self, message, success=True):
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        self.status_var.set(message)
