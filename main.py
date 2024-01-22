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
    #--------------------------------------------------------------
    #horario do alarme:
    #--------------------------------------------------------------


    chegou([horas,minutos,segundos])


def chegou(horario):
    if horario == [20,59,50]:
        equacao()


def equacao():
    mixer.init() #inicia a funcao que toca o audio
    mixer.music.load("sons\\Som de alarme 1min.mp3")
    #mixer.music.load("sons\\Som de alarme [TubeRipper.com].mp3")
    
    tempo_reproducao = 5 #tempo que o audio toca em segundos
    tempo_reproducao_ms = int(tempo_reproducao * 1000) #tempo que o audio toca em milisegundos
    mixer.music.play()

    #mixer.music.set_endevent(mixer.USEREVENT + 1) #para o audio caso ele termine
    
    janelaprin.after(tempo_reproducao_ms, mixer.music.stop) #para o audio depois de um certo tempo em ms

    #fotonum = f"{randint(1,10)}.png"
    #foto = PhotoImage(file=f"print\\imagens\\{fotonum}")
    foto = PhotoImage(file=f"print\\imagens\\1.png")
    label_foto = Label(janelaprin,image=foto)
    label_foto.place(x=100,y=100)





janelaprin = Tk()
janelaprin.title("Equalarme")
rotulo_relogio = Label(janelaprin,font=("calibri",40,"bold"),background="black",foreground="white")


rotulo_relogio.pack(anchor='center')
atualizarrelogio()
janelaprin.geometry("500x500")
janelaprin.mainloop()