from tkinter import *
from tkinter import filedialog


def mostrafoto(image_reference):
    global foto_global
    foto_global = PhotoImage(file="C:\\Users\\canal\\OneDrive\\Documentos\\Projetos vscode\\alarme\\print\\imagens\\6.png")
    image_reference.config(image = foto_global)

janelaprin = Tk()
janelaprin.title("Equalarme")

label_foto = Label(janelaprin)
label_foto.pack(padx=10,pady=10)

#foto = PhotoImage(file="C:\\Users\\canal\\OneDrive\\Documentos\\Projetos vscode\\alarme\\print\\imagens\\6.png")
#label_foto = Label(janelaprin,image=foto)
#label_foto.pack(anchor="center")

mostra_button =Button(janelaprin, text="mostra foto", command=lambda: mostrafoto(label_foto))
mostra_button.pack(pady=10)


janelaprin.geometry("500x500")
janelaprin.mainloop()



