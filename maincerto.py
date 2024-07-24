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
    segundos = int(partes_tempo[2])

    horario_atual = [horas,minutos,segundos]
#--------------------------------------------------------------#--------------------------------------------------------------#--------------------------------------------------------------
    if horario_atual == horario_alarme:
#--------------------------------------------------------------#--------------------------------------------------------------#--------------------------------------------------------------
        tocar_alarme()


def tocar_alarme():
    equacao()
    mixer.init()
    mixer.music.load("sons\\Som de alarme 1min.mp3")
    mixer.music.play(loops=-1)


def equacao():
    """mostrafoto(imagem_label)
    mostraaviso(texto_aviso)
    mostrabotao()"""
    num1 = randint(-15, 80)  
    num2 = randint(-15, 80)  
    num3 = randint(1, 10)
    operacao = choice(['+', '-', '*'])  
    equacao_texto = f"{num1} {operacao} {num2} = ?"
    
    resposta_correta = eval(f"{num1} {operacao} {num2}")
    print(resposta_correta)
    #janelaprin.after(tempo_reproducao_ms, mixer.music.stop) #para o audio depois de um certo tempo em ms
    def verifica_resposta():
        resposta_usuario = entrada_resposta.get()  # Obtém a resposta do usuário
        if resposta_usuario.isdigit() and int(resposta_usuario) == resposta_correta:  # Verifica se a resposta é correta
            mixer.music.stop()  # Para o som do alarme
            aviso["text"] = "Alarme Desativado!"  # Atualiza o aviso para "Alarme Desativado!"
        else:
            aviso["text"] = "Resposta Incorreta. Tente Novamente."

    
    aviso["text"] = "RESOLVA A EQUAÇÃO PARA PARAR O ALARME!"  # Atualiza o aviso para instruir o usuário
    equacao_label["text"] = equacao_texto  # Mostra a equação na interface
    botao_verificar.config(command=verifica_resposta)  # Configura o botão para verificar a resposta
    entrada_resposta.delete(0, 'end')
    

def solve_linear_equation(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero em uma equação de primeiro grau.")
    return (c - b) / a



def definir_horario_alarme():
    global horario_alarme 
    horas = int(entrada_horas.get()) 
    minutos = int(entrada_minutos.get())
    segundos = int(entrada_segundos.get()) 
    horario_alarme = [horas, minutos, segundos] 
    aviso["text"] = f"Alarme definido para {horas:02d}:{minutos:02d}:{segundos:02d}"  


janelaprin = Tk()

janelaprin.title("Equalarme")
janelaprin.geometry("700x500")


# Cria e posiciona o rótulo do relógio
rotulo_relogio = Label(janelaprin, font=("calibri", 40, "bold"), background="black", foreground="white")
rotulo_relogio.pack(anchor='center', pady=10)

"""global texto_aviso
texto_aviso = Label(janelaprin,font=("Times New Roman",20,"bold"),foreground="black")
texto_aviso.pack(pady=5)

global imagem_label
imagem_label = Label(janelaprin)
imagem_label.pack(side=LEFT,pady=5,padx=95,expand=YES)

global botao_geraroutra
botao_geraroutra = Button(janelaprin)"""

# Cria e posiciona o aviso
aviso = Label(janelaprin, font=("Times New Roman", 20, "bold"), foreground="black")
aviso.pack(pady=5)


frame_horario = Frame(janelaprin)
frame_horario.pack(pady=5)


# Cria e posiciona as entradas para definir o horário do alarme dentro do frame
entrada_horas = Entry(frame_horario, font=("Times New Roman", 20, "bold"), width=3)  # Entrada para horas
entrada_horas.pack(side='left', padx=5)
entrada_minutos = Entry(frame_horario, font=("Times New Roman", 20, "bold"), width=3)  # Entrada para minutos
entrada_minutos.pack(side='left', padx=5)
entrada_segundos = Entry(frame_horario, font=("Times New Roman", 20, "bold"), width=3)  # Entrada para segundos
entrada_segundos.pack(side='left', padx=5)


# Cria e posiciona o rótulo da equação
equacao_label = Label(janelaprin, font=("Times New Roman", 20, "bold"), foreground="black")
equacao_label.pack(pady=5)


# Botão para definir o horário do alarme
botao_definir_alarme = Button(janelaprin, text="Definir Alarme", font=("Times New Roman", 20, "bold"), command=definir_horario_alarme)
botao_definir_alarme.pack(pady=5)


# Entrada para a resposta da equação
entrada_resposta = Entry(janelaprin, font=("Times New Roman", 20, "bold"), foreground="black")
entrada_resposta.pack(pady=5)



horario_alarme = [0, 0, 0]  # Horário inicial do alarme



# Botão para verificar a resposta da equação
botao_verificar = Button(janelaprin, text="Verificar Resposta", font=("Times New Roman", 20, "bold"))
botao_verificar.pack(pady=5)

atualizarrelogio()
janelaprin.mainloop()
