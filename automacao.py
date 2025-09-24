import pyautogui as pa
import time
import pyperclip
# Adiciona pausa entre os comandos
pa.PAUSE = 1
# Abri o navegador Firefox e navega para o YouTube
pa.press('win')
pa.write("Firefox")
pa.press('ENTER')
pa.write("https://www.youtube.com")
pa.press('ENTER')
time.sleep(5)
# Click no campo de pesquisa do YouTube
pa.click(x=610, y=174)
# Pesquisa o conteúdo desejado
pyperclip.copy('water fall, mogli')
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
# Após localizar, abre o conteúdo
pa.click(x=630, y=528)
