import Contatto
import Rubrica

class StartProgram:
    def __init__(self):
        self.__rubrica= Rubrica.Rubrica()
        self.scelta()

    def menu(self):
        print("""
        Rubrica
        1) Aggiungere un contatto
        2) Cancellare un contatto
        3) Cercare un contatto per cognome
        4) Modificare un contatto
        5) Stampare rubrica
        6) Salvare su file
        7) Chiusura programma
        """)

    def scelta(self):
        op= 0
        while(op!=7):
            self.menu()
            op= int(input("Operazione: "))
            if(op==1):
                try:
                    nome= input("Nome: ")
                    cognome= input("Cognome: ")
                    email= input("Email: ")
                    numeroTelefono= int(input("Numero: "))
                    p= Contatto.Persona(nome, cognome, email, numeroTelefono)
                    self.__rubrica.addContatto(p)
                except ValueError:
                    print("Numero di telefono non valido")
                except:
                    print("Errore in input")
            elif(op==2):
                cognome= input("Cognome: ")
                self.__rubrica.remContatto(cognome)
            elif(op==3):
                cognome= input("Cognome: ")
                self.__rubrica.cerContatto(cognome)
            elif(op==4):
                cognome= input("Cognome: ")
                self.__rubrica.modContatto(cognome)
            elif(op==5):
                self.__rubrica.stampRubrica()
            elif(op==6):
                self.__rubrica.writeRubrica()
            elif(op==7):
                print("Chiusura in corso")

#Avvio

s= StartProgram()
