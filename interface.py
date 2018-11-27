#coding:utf-8
from tkinter import *
from tkinter import messagebox as ms
import time
#Créations des fonctions et test de connexion


def login():
    username = "odoo"
    password = "interface"
    #On teste les variables de controle pour se connecter
    if usernameInput.get() == username and passwordInput.get() == password:
        root = Tk()
        root.title("INTERFACE ODOO")
        root.geometry("1600x800+0+0")

        #Création des widgets
        Tops = Frame(root)
        Tops.pack(side=TOP)

        label1 = Label(Tops, text="Nom du fichier Excel : ")
        btn1 = Button(Tops, text="Choose File", command="")
        btn2 = Button(Tops, text="Extraction de données", command="function")
        btn3 = Button(Tops, text="Mise à jour", command="")
        btn4 = Button(Tops, text="Verifier la mise à jour", command="")
        btn5 = Button(Tops, text='QUITTER', command=root.quit)

        #Afficahge de tous les widgets et positionnements
        label1.grid(row=0, sticky=E)
        btn1.grid(row=0, column=1, padx=5, pady=20)
        btn2.grid(row=4, column=1, padx=5, pady=20)
        btn3.grid(row=5, column=1, padx=5, pady=20)
        btn4.grid(row=6, column=1, padx=5, pady=20)
        btn5.grid(row=7, column=1, padx=5, pady=20)
        root.mainloop()
    else:
        ms.showerror('Oops!', 'Username and/or Password Not Found.')


#Création de la fenêtre avant de se logger
#Création des fonctions
#Création et paramétrage de la fenêtre
root = Tk()
root.title("Interface Odoo Utilisateur")
root.geometry("1600x800+0+0")
#===========variables de controle ======================
usernameInput = StringVar()
passwordInput = StringVar()

#=======================Time=========================
localtime = time.asctime(time.localtime(time.time()))
#=======================Info===========================
#Créations des widgets
Tops = Frame(root, width=800, height=1000, bg="cyan", relief='solid')
Tops.pack(side=TOP)

lblInfo = Label(Tops, font=('arial', 50, 'bold'),
                text="Interface de Connexion Odoo", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

label1 = Label(Tops, font=('arial', 20, 'bold'), text="Username : ")
label1.grid(row=2, sticky=W, padx=5, pady=30)

label1 = Label(Tops, font=('arial', 20, 'bold'), text="Password : ")
label1.grid(row=3, sticky=W, padx=5, pady=30)

entre1 = Entry(Tops, textvariable=usernameInput, relief=RAISED, cursor="arrow")
entre1.grid(row=2, sticky=E, padx=5, pady=30)

entre2 = Entry(Tops, textvariable=passwordInput,
               show='*', relief=RAISED, cursor="arrow")
entre2.grid(row=3, sticky=E, padx=5, pady=30)

signupButton = Button(Tops, font=('arial', 20, 'bold'),
                      text='Signup', command=login)
signupButton.grid(columnspan=2, sticky=S, pady=30)

root.mainloop()
