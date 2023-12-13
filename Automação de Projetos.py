import yfinance


codigo = input("Digite o codigo da ação: ")
email = input("Digite o(s) email(s):(separados por virgula) ")
dados = yfinance.Ticker(codigo).history("6mo")

fechamento = dados.Close

maxima = round(fechamento.max(),2)
minimo = round(fechamento.min(),2)
atual = round(fechamento[-1], 2)


import pyautogui
import pyperclip

# Utilizar o position do pyautogui para informar as coordenadas corretas

pyautogui.PAUSE = 3

# Clicar no app edge e abrir uma nova aba
pyautogui.click(x=652, y=1185)
pyautogui.hotkey("ctrl","t")

# Colar o endereço do google e acessar
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")

# clicar escrever e preencher o(s) destinatarios, assunto e corpo do email
pyautogui.click(x=120, y=218)
pyperclip.copy(email)
pyautogui.hotkey("ctrl","v")
pyautogui.press('tab')

pyperclip.copy("Análises de fechamento")
pyautogui.hotkey("ctrl","v")
pyautogui.press('tab')

mensagem = f'''Prezado,

Seguem as análises da ação {codigo}!

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minimo}
Cotação atual: R$ {atual}

Qualquer dúvida estou à disposição!

Atenciosamente,
Davi 
 '''

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# Enviar mensagem
pyautogui.click(x=1125, y=1108)

