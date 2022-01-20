#Importar bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
#Definir contatos/grupos e mensagem a ser enviada

contatos_txt = open("contatos.txt", "r") # Possibilita o uso de arquivo de texto para que o cliente possa alterar quantas vezes quiser os destinatarios
contatos = []

for linha in contatos_txt:
    linha = linha.strip()
    contatos.append(linha)
contatos_txt.close()   

mensagem_txt = open("mensagem.txt", "r")
mensagem = []
for letra in mensagem_txt:
    mensagem.append(letra)
mensagem_txt.close()

#buscar contatos/grupos

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:   
    buscar_contato(contato)
    enviar_mensagem(mensagem)
#Campo de pesquisa "copyable-text selectable-text"
#Campo de mensagem "copyable-text selectable-text"
#Mandar mensagens para contatos/grupos

