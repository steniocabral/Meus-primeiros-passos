import time
import pyautogui
import pyperclip

usuarios = [    {'login': '', 'senha': ''},    {'login': '', 'senha': ''},    {'login': '', 'senha': ''},    {'login': '', 'senha': ''}]

competencia = input('Digite a competência: ')

for usuario in usuarios:
    # Abrindo o Google Chrome
    pyautogui.PAUSE = 2
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.click(x=1008, y=23)
    time.sleep(2)

    # Copiando a URL e colando no Chrome
    url = 'https://directa.natal.rn.gov.br/open.do?sys=DIR&a=wqf45tfes'
    pyperclip.copy(url)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    time.sleep(2)

    # Clicando nos campos de login e senha e preenchendo com as informações
    pyautogui.click(x=105, y=230)
    pyautogui.click(x=119, y=315)
    pyperclip.copy(usuario['login'])
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyperclip.copy(usuario['senha'])
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(2)

    # Clicando no menu DDS
    pyautogui.PAUSE = 2
    pyautogui.click(x=98, y=327)
    pyautogui.click(x=102, y=453)
    pyautogui.click(x=394, y=453)

    # Seleção e preenchimento da competência
    pyautogui.click(x=805, y=442)
    pyautogui.click(x=497, y=486)
    pyautogui.click(x=371, y=494)
    pyperclip.copy(competencia)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(x=340, y=556)
    pyautogui.click(x=1356, y=718)
    pyautogui.click(x=1356, y=718)
    pyautogui.click(x=681, y=703)
    pyautogui.click(x=681, y=703)

    # Confirmação e envio
    pyautogui.click(x=718, y=720)
    pyautogui.click(x=758, y=223)
    pyautogui.click(x=820, y=519)

    # Recibo de entrega
    pyautogui.click(x=482, y=468)
    pyautogui.click(x=409, y=515)
    pyautogui.click(x=872, y=552)
    time.sleep(3)

    # Salvando o recibo
    pyautogui.click(x=1239, y=83)
    pyautogui.click(x=90, y=200)
    pyautogui.click(x=502, y=445)
    pyautogui.click(x=1328, y=11)

    # Deslogando do portal
    pyautogui.click(x=1356, y=80)
    pyautogui.click(x=1356, y=80)
    pyautogui.click(x=1290, y=167)
    pyautogui.click(x=686, y=452)
    pyautogui.click(x=1337, y=14)

    # Esperando alguns segundos antes de começar com o próximo usuário
    time.sleep(10)