import tkinter as tk
from tkinter import *
from tkinter import messagebox

from LogicBD.UserEntity import User
from LogicBD.logicBD import BDConnect
from LogicOtherButtons.ClearCamp import ClearCamp


class MainView:

    def __init__(self, booleanTostart=None):
        if booleanTostart != None and booleanTostart:
            self.root = tk.Tk()
            self.root.title("C-R-U-D")
            self.root.resizable(0, 0)
            self.root.config(cursor="pencil", background="#3B3B3B")
            self.root.geometry("300x400")
            self.createWindows()
            self.root.mainloop()

    def createWindows(self):
        mi_frame = Frame(self.root)
        mi_frame.config(background="#3B3B3B")
        mi_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.barMenu()
        self.datanMenu(mi_frame)
        self.buttonsADD()

    def barMenu(self):
        logicBd = BDConnect()
        clearCamp = ClearCamp()
        bar_menu = Menu(self.root, tearoff=False)
        bar_BD = Menu(bar_menu)
        bar_Clear = Menu(bar_menu)
        bar_CRUD = Menu(bar_menu)
        bar_Help = Menu(bar_menu)
        bar_menu.add_cascade(menu=bar_BD, label="BBDD")
        bar_menu.add_cascade(menu=bar_Clear, label="Clear")
        bar_menu.add_cascade(menu=bar_CRUD, label="CRUD")
        bar_menu.add_cascade(menu=bar_Help, label="Help")

        # ---- BD ----

        bar_BD.add_command(
            label="Conect",
            accelerator="Ctrl+Shift+C",
            command=lambda: logicBd.conectBd()
        )
        bar_BD.add_separator()
        bar_BD.add_command(label="Salir", command=lambda: logicBd.salirBD(self.root))

        # ---- CLEAR ----

        bar_Clear.add_command(
            label="Clear fields",
            command=lambda: clearCamp.clearC(self.id_text, self.name_text, self.pass_text, self.surname_text,
                                             self.addres_text, self.coment_text)
        )

        # ---- CRUD ----

        bar_CRUD.add_command(
            label="Create",
            command=lambda: logicBd.save(self.createUser())
        )
        bar_CRUD.add_command(
            label="Read",
            command=lambda: self.showData(logicBd)
        )
        bar_CRUD.add_command(
            label="Update",
            command=lambda: self.updateData(logicBd)
        )
        bar_CRUD.add_command(
            label="Delete",
            command=lambda: logicBd.deletee(self.id_text)
        )

        # ---- HELP ----

        bar_Help.add_command(
            label="Licence",
            command=lambda: clearCamp.licen()
        )
        bar_Help.add_command(
            label="About it",
            command=lambda: clearCamp.about()
        )

        self.root.config(menu=bar_menu)

    def datanMenu(self, frame):
        self.id_text = Entry(frame, width=15)
        self.name_text = Entry(frame, width=15)
        self.pass_text = Entry(frame, width=15)
        self.surname_text = Entry(frame, width=15)
        self.addres_text = Entry(frame, width=15)
        self.coment_text = Text(frame, height=10, width=20)

        idd = Label(frame, text="ID: ", background="#3B3B3B", fg="white")
        name = Label(frame, text="Name: ", background="#3B3B3B", fg="white")
        passs = Label(frame, text="Password :", background="#3B3B3B", fg="white")
        surname = Label(frame, text="Surname : ", background="#3B3B3B", fg="white")
        addres = Label(frame, text="Address : ", background="#3B3B3B", fg="white")
        coment = Label(frame, text="Comment : ", background="#3B3B3B", fg="white")

        idd.grid(row=0, column=0)
        self.id_text.grid(row=0, column=1, pady=5)
        name.grid(row=1, column=0)
        self.name_text.grid(row=1, column=1, pady=5)
        passs.grid(row=2, column=0)
        self.pass_text.grid(row=2, column=1, pady=5)
        surname.grid(row=3, column=0)
        self.surname_text.grid(row=3, column=1, pady=5)
        addres.grid(row=4, column=0)
        self.addres_text.grid(row=4, column=1, pady=5)
        coment.grid(row=5, column=0)
        self.coment_text.grid(row=5, column=1, pady=5, columnspan=4)

    def createUser(self):
        user = User(self.id_text.get(), self.name_text.get(), self.pass_text.get(), self.surname_text.get(),
                    self.addres_text.get(), self.coment_text.get(1.0, tk.END))
        if user is not None:
            self.id_text.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.pass_text.delete(0, tk.END)
            self.surname_text.delete(0, tk.END)
            self.addres_text.delete(0, tk.END)
            self.coment_text.delete(1.0, tk.END)
            return user
        else:
            return None

    def showData(self, logicBd):
        u = logicBd.getData(self.id_text.get())
        if u is not None:
            self.id_text.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.pass_text.delete(0, tk.END)
            self.surname_text.delete(0, tk.END)
            self.addres_text.delete(0, tk.END)
            self.coment_text.delete(1.0, tk.END)
            self.id_text.insert(0, str(u.getId()))
            self.name_text.insert(0, u.getName())
            self.pass_text.insert(0, u.getPas())
            self.surname_text.insert(0, u.getSurname())
            self.addres_text.insert(0, u.getAddres())
            self.coment_text.insert(1.0, u.getComent())

    def updateData(self, logicBd):
        user = User(self.id_text.get(), self.name_text.get(), self.pass_text.get(), self.surname_text.get(),
                    self.addres_text.get(), self.coment_text.get(1.0, tk.END))
        if user is not None:
            logicBd.update(user)
            self.id_text.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.pass_text.delete(0, tk.END)
            self.surname_text.delete(0, tk.END)
            self.addres_text.delete(0, tk.END)
            self.coment_text.delete(1.0, tk.END)
            messagebox.showinfo(message="Updated", title="Updated")

    def buttonsADD(self):
        mi_frame = Frame(self.root)
        mi_frame.place(anchor="c", relx=.5, rely=.9)
        mi_frame.config(background="#3B3B3B")
        logicBd = BDConnect()
        create = Button(mi_frame, text="Create", command=lambda: logicBd.save(self.createUser()))
        read = Button(mi_frame, text="Read", command=lambda: self.showData(logicBd))
        update = Button(mi_frame, text="Update", command=lambda: self.updateData(logicBd))
        delete = Button(mi_frame, text="Delete", command=lambda: logicBd.deletee(self.id_text))

        create.grid(row=6, column=0, pady=5, padx=5)
        read.grid(row=6, column=1, pady=5, padx=5)
        update.grid(row=6, column=2, pady=5, padx=5)
        delete.grid(row=6, column=5, pady=5, padx=5)
