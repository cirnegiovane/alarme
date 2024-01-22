import pyautogui
import time
# Obter as coordenadas atuais do mouse
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordenadas do Mouse - X: {x}, Y: {y}")

time.sleep(5)
x1, y1 = pyautogui.position()

# Exibir as coordenadas
print(f"Coordenadas do Mouse DEPOIS - X: {x1}, Y: {y1}")