class User():
    id = 0
    name = ""
    pas = ""
    surname = ""
    addres = ""
    coment = ""

    def __init__(sefl, id, name, pas, surname, addres, coment):
        sefl.id = id
        sefl.name = name
        sefl.pas = pas
        sefl.surname = surname
        sefl.addres = addres
        sefl.coment = coment

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPas(self):
        return self.pas

    def getSurname(self):
        return self.surname

    def getAddres(self):
        return self.addres

    def getComent(self):
        return self.coment

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setPas(self, pas):
        self.pas = pas

    def setSurname(self, surname):
        self.surname = surname

    def setAddres(self, addres):
        self.addres = addres

    def setComent(self, coment):
        self.coment = coment
