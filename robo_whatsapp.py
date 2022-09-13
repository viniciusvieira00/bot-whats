import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

navegador = webdriver.Chrome("/usr/local/bin/chromedriver")
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Meu povo do Acre, me chamo Marlene, venho aqui hoje passar para vocês, para que nunca confiem em falsas pesquisas, a verdade nos sabemos, segue uma matéria mostrando aquilo que não é mostrado \n\n {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(5)
    pagina = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    pagina.click()
    time.sleep(5)