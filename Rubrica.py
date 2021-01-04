import Contatto

class Rubrica:
    __lista= []
    
    def addContatto(self, obj): 
        self.__lista.append(obj)

    def remContatto(self, cognome):     #scansiona la lista, quando trova una corrispondenza
        for i in self.__lista:                                  #chiede se è quello giusto, se lo è cancella
            if i.getSurname()== cognome:    #sennò continua la scansione
                print(i)
                scelta= input("È questo il contatto? Y/N").upper()
                if(scelta=="Y"):
                    self.__lista.remove(i)
                    print("Contatto eliminato")
                    break
                elif(scelta=="N"):
                    continue
                else:
                    print("Opzione non valida")
                    break
        else:
            print("Contatto non trovato")

    def modContatto(self, cognome):
        for i in self.__lista: #scansiona in cerca del cognome
            if i.getSurname()== cognome:
                scelta= input("È questo il contatto? Y/N").upper()
                if(scelta=="Y"): #se trovato chiede i nuovi dati
                    try: 
                        print("Immettere i nuovi dati")
                        nome= input("Nome: ")
                        cognome= input("Cognome: ")
                        email= input("Email: ")
                        numeroTelefono= int(input("Numero: "))
                        p= Contatto.Persona(nome, cognome, email, numeroTelefono)
                        self.__lista.append(p) #inserimento in lista del nuovo elemento
                        self.__lista.remove(i) #rimozione dalla lista del vecchio elemento
                        break
                    except ValueError:
                        print("Numero di telefono non valido")
                    except:
                        print("Errore in input")
                elif(scelta=="N"):
                    continue
                else:
                    print("Opzione non valida")
                    break
        else:
            print("Contatto non trovato")

    def cerContatto(self, cognome):
        t= 0 #flag per il controllo
        for i in self.__lista:
            if i.getSurname()== cognome:
                print(i)
                t= 1 #attiva flag
        if(t==0): #se flag non attivo stampa il seguente messaggio
            print("Contatto non trovato")
            
    def stampRubrica(self):
        for i in self.__lista:
            print(i)

    def writeRubrica(self):
        file= open("rubrica.txt", "w")
        for i in self.__lista:
            file.write(str(i))
            file.write("\n")
        file.close()
        print("Backup completato")
