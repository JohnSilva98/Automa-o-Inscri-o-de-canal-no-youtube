from tkinter import messagebox
from PIL import ImageGrab
from pytesseract import Output
import pyautogui
import time




#abrir chrome
tes = pyautogui.locateCenterOnScreen(r'chrome.png', confidence=0.9)
print("coord chrome: ",tes)
pyautogui.moveTo(tes, duration=0.3)
pyautogui.click()
#caixa de pesquisa
pesquisar = pyautogui.prompt(text="", title="Digite o nome do canal")
# abrir nova guia
time.sleep(1)
pyautogui.moveTo(1585, 16)
pyautogui.click()
pyautogui.hotkey('ctrl', 't')

#pesquisar youtube
pyautogui.write("www.youtube.com", interval=0.050)
pyautogui.press('enter')
time.sleep(3.5)
btn_pesquisar = pyautogui.locateCenterOnScreen(r"pesquisar.png", confidence=0.9)
print("coord barra: ",btn_pesquisar)
pyautogui.moveTo(btn_pesquisar, duration=0.3)
pyautogui.click()
pyautogui.write(pesquisar, interval=0.025)
pyautogui.press('enter')
time.sleep(2)

#acessar canal
logo = pyautogui.locateCenterOnScreen(r"logocanaldark.png", confidence=0.9)
print("coord logo:",logo)
pyautogui.moveTo(logo, duration=0.3)
pyautogui.click()
time.sleep(3)

#se inscrever
btn_inscrever = pyautogui.locateCenterOnScreen(r"inscrever.png", confidence=0.9)
print("coord inscrever:",btn_inscrever)
pyautogui.moveTo(btn_inscrever, duration=0.3)
pyautogui.click()
time.sleep(1)
pyautogui.alert(text='Inscrito com Sucesso!', title='Inscrição Concluída', button='OK')

