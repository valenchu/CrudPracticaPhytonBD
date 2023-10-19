import tkinter as tk
import sqlite3
from tkinter import messagebox

from LogicBD.UserEntity import User


class BDConnect:

    def conectBd(self):
        conect = sqlite3.connect("Usuario")
        curse = conect.cursor()
        varReturnTableExiste = curse.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Usuario'")
        if varReturnTableExiste.fetchone()[0] == 1:
            messagebox.showinfo(message="The table existed", title="Existed")
            return
        curse.execute(
            "CREATE TABLE IF NOT EXISTS Usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pas TEXT, surname TEXT, addres TEXT, coment TEXT)")
        messagebox.showinfo(message="Tabled created", title="Created")
        conect.close()

    def salirBD(self, root):
        varSalir = messagebox.askyesno(message="¿Wish to exit?", title="Title")
        if varSalir:
            root.destroy()
        else:
            pass

    def save(self, user):
        if not user.getId() and len(user.getId()) <= 1:
            conect = sqlite3.connect("Usuario")
            curse = conect.cursor()
            curse.execute("INSERT INTO Usuario (name, pas, surname, addres, coment) VALUES (?,?,?,?,?)",
                          (user.getName(), user.getPas(), user.getSurname(), user.getAddres(), user.getComent()))
            conect.commit()
            conect.close()
        else:
            messagebox.showerror(message="Clear ID for create a new user", title="ERROR ID EXIST")

    def getData(self, id):
        conect = sqlite3.connect("Usuario")
        curse = conect.cursor()
        varReturnTableExiste = curse.execute("SELECT * FROM Usuario WHERE id=?", (id,)).fetchone()
        if varReturnTableExiste is None:
            messagebox.showerror(message="Error", title="Error id not exist")
            return None
        u = User(varReturnTableExiste[0], varReturnTableExiste[1], varReturnTableExiste[2], varReturnTableExiste[3],
                 varReturnTableExiste[4], varReturnTableExiste[5])
        return u

    def update(self, user):
        conect = sqlite3.connect("Usuario")
        curse = conect.cursor()
        curse.execute("UPDATE Usuario SET name=?, pas=?, surname=?, addres=?, coment=? WHERE id=?", (
            user.getName(), user.getPas(), user.getSurname(), user.getAddres(), user.getComent(), user.getId()))
        conect.commit()
        conect.close()

    def deletee(self, idu):
        conect = sqlite3.connect("Usuario")
        curse = conect.cursor()
        curse.execute("DELETE FROM Usuario WHERE id=?", (idu.get(),))
        conect.commit()
        conect.close()
        idu.delete(0, tk.END)
        return
