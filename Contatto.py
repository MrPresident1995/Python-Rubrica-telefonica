class Persona:
        def __init__(self, name, surname, email, numeroTelefono):
                self.__name= name
                self.__surname= surname
                self.__email= email
                self.__numeroTelefono= numeroTelefono

        def getName(self):
            return self.__name
        
        def getSurname(self):
            return self.__surname

        def getEmail(self):
            return self.__email

        def getNumero(self):
            return self.__numeroTelefono

        def __str__(self):
            return "Name: " + self.__name + " Surname: " + self.__surname + " Email: " + self.__email + " Numero: " + str(self.__numeroTelefono)
