# import pyautogui
# from time import sleep

# # 1. Clicar e digitar meu usuário
# pyautogui.click(1276,542, duration=2)
# pyautogui.write('thiago')

# # 2. Clicar e digitar minha senha
# pyautogui.click(1272,568, duration=2)
# pyautogui.write('1234')
 
# # 3. Clicar em "Entrar"
# pyautogui.click(1189,596, duration=2)

# # 4. Extrair cada produto
# with open('produtos.txt', 'r') as arquivo:
#     for linha in arquivo:
#         produto = linha.split(',')[0]
#         quantidade = linha.split(',')[1]
#         preco = linha.split(',')[2]
        
#         # 	4.1. Clicar e digitar o produto
#         pyautogui.click(991,529, duration=2)
#         pyautogui.write(produto)
        
#         # 	4.2. Clicar e digitar a quantidade
#         pyautogui.click(991,554, duration=2)
#         pyautogui.write(quantidade)
        
#         # 	4.3. Clicar e digitar o preço
#         pyautogui.click(989,582, duration=2)
#         pyautogui.write(preco)
        
#         #   4.4. Clicar em "Registrar"
#         pyautogui.click(914,740, duration=2)
#         sleep(1)

import pyautogui
from time import sleep

# 1. Clicar e digitar meu usuário
pyautogui.click(1276,542)
pyautogui.write('thiago')

# 2. Clicar e digitar minha senha
pyautogui.click(1272,568)
pyautogui.write('1234')
 
# 3. Clicar em "Entrar"
pyautogui.click(1189,596)

# 4. Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        # 	4.1. Clicar e digitar o produto
        pyautogui.click(991,529)
        pyautogui.write(produto)
        
        # 	4.2. Clicar e digitar a quantidade
        pyautogui.click(991,554)
        pyautogui.write(quantidade)
        
        # 	4.3. Clicar e digitar o preço
        pyautogui.click(989,582)
        pyautogui.write(preco)
        
        #   4.4. Clicar em "Registrar"
        pyautogui.click(914,740)
        sleep(1)