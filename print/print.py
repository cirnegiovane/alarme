import tkinter as tk
import pyautogui
from PIL import ImageGrab
from datetime import datetime


def capture_screen():
    # Captura a área específica da tela X: 462, Y: 494 width: 192 height: 50
    x, y, width, height = 462, 442, 192, 50
    screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))

    # Gera um nome de arquivo único usando a data e hora
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{varglobal}.png"
    attglobal()
    # Salva a captura de tela com o nome de arquivo gerado
    screenshot.save(f"print\\imagens\\{filename}")
    print(f"Screenshot salva como {filename}")
# Criar janela principal
root = tk.Tk()
root.title("Captura de Tela")
root.geometry("150x50")

def attglobal():
    global varglobal
    varglobal +=1

# Criar botão
varglobal = 11
capture_button = tk.Button(root, text="Capturar Tela", command=capture_screen)



capture_button.pack(pady=10)

# Executar o loop principal da interface gráfica
root.mainloop()