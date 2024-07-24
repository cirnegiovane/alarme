from time import *
from tkinter import *
from pygame import mixer
from random import *

def atualizarrelogio():
    tempo_atual = strftime('%H:%M:%S')
    rotulo_relogio["text"] = tempo_atual
    janelaprin.after(1000, atualizarrelogio)

    partes_tempo = tempo_atual.split(":")

    horas = int(partes_tempo[0])
    minutos = int(partes_tempo[1])
    segundos = int(partes_tempo[2].split()[0])

    horario = [horas,minutos,segundos]
#--------------------------------------------------------------#--------------------------------------------------------------#--------------------------------------------------------------
    if horario == [19,52,10]:
#--------------------------------------------------------------#--------------------------------------------------------------#--------------------------------------------------------------
        equacao()


def equacao():
    mostrafoto(imagem_label)
    mostraaviso(texto_aviso)
    mostrabotao()
    mostrapergunta()
    mostraresposta()
    mixer.init() #inicia a funcao que toca o audio
    mixer.music.load("sons\\Som de alarme 1min.mp3")
    tempo_reproducao = 1 #tempo que o audio toca em segundos
    tempo_reproducao_ms = int(tempo_reproducao * 1000) #tempo que o audio toca em milisegundos
    mixer.music.play()
    janelaprin.after(tempo_reproducao_ms, mixer.music.stop) #para o audio depois de um certo tempo em ms
    

def mostrafoto(image_reference):
    global foto_global
    img = randint(4,15)
    foto_global = PhotoImage(file=f"C:\\Users\\canal\\OneDrive\\Documentos\\Projetos vscode\\alarme\\print\\imagens\\{img}.png")
    image_reference.config(image = foto_global)


def mostraaviso(texto):
    texto_aviso["text"] = "RESOLVA A EQUAÇÃO PARA PARAR O ALARME!"

def mostrabotao():
    botao_geraroutra = Button(janelaprin,text="Gerar outra equação",command = lambda:mostrafoto(imagem_label))
    botao_geraroutra.pack(side=RIGHT,padx=95,pady=15)


def mostrapergunta():
    pergunta["text"] = "Qual o valor de x?"
    


def mostraresposta():
    caixaresposta = Entry(janelaprin,font=("Times New Roman",15),foreground="black",background="white")


janelaprin = Tk()

janelaprin.title("Equalarme")

rotulo_relogio = Label(janelaprin,font=("calibri",40,"bold"),background="black",foreground="white")
rotulo_relogio.pack(anchor='center',pady=30)


global texto_aviso
texto_aviso = Label(janelaprin,font=("Times New Roman",20,"bold"),foreground="black")
texto_aviso.pack(pady=15,anchor=CENTER)

global imagem_label
imagem_label = Label(janelaprin)
imagem_label.pack(side=LEFT,pady=30,padx=95,expand=YES)

global botao_geraroutra
botao_geraroutra = Button(janelaprin)

global pergunta
pergunta = Label(janelaprin)
pergunta.pack(side=LEFT,anchor=N,padx=10)


global caixaresposta
caixaresposta = Entry(janelaprin)
caixaresposta.pack(side=RIGHT,anchor=N,padx=10)


#equacao()

atualizarrelogio()
janelaprin.geometry("700x500")
janelaprin.mainloop()