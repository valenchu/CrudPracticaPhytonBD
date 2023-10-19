import tkinter as tk
from tkinter import messagebox


class ClearCamp():

    def clearC(self, id, name, pas, surname, addres, coment):
        id.delete(0, tk.END)
        name.delete(0, tk.END)
        pas.delete(0, tk.END)
        surname.delete(0, tk.END)
        addres.delete(0, tk.END)
        coment.delete(1.0, tk.END)

    def licen(self):
        messagebox.showinfo(message="You have a Licence until 2023 to 2028", title="Licence")

    def about(self):
        messagebox.showinfo(message="Copywriter Valentín Cassino", title="About")
