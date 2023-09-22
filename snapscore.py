import os 
import time
import requests
import zipfile 



# URL van het te downloaden ChromeDriver-bestand
url = "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"

# Bestandsnaam om op te slaan
bestandsnaam = "chromedriver_linux64.zip"

# De map waarin je het ChromeDriver-bestand wilt opslaan
doelmap = "/workspaces/dev/snapscore/chromedriver_snapscore"  # Vervang dit door de gewenste doelmap op je systeem

# Controleer of de doelmap bestaat, anders maak deze aan
if not os.path.exists(doelmap):
    os.makedirs(doelmap)

# De volledige bestandspad voor het opgeslagen bestand
bestandspad = os.path.join(doelmap, bestandsnaam)

# Voer het daadwerkelijke downloaden uit
response = requests.get(url)

if response.status_code == 200:
    # Sla het bestand op
    with open(bestandspad, 'wb') as bestand:
        bestand.write(response.content)

    print(f"ChromeDriver-bestand is gedownload en opgeslagen op: {bestandspad}")
    
    # Uitpakken van het ZIP-archief
    with zipfile.ZipFile(bestandspad, 'r') as zip_ref:
        zip_ref.extractall(doelmap)

    print("Het ZIP-archief is uitgepakt.")

else:
    print("Fout bij het downloaden van het bestand.")





# De URL van het bestand dat je wilt downloaden
url = "https://imgs.search.brave.com/TvQwABfW_uz9-0t901CvVDqfmCden19LyyXOVg-aOEo/rs:fit:860:0:0/g:ce/aHR0cHM6Ly91cy10/dW5hLXNvdW5kcy1p/bWFnZXMudm9pY2Vt/b2QubmV0LzdmNTE0/N2IxLTVjNzEtNDY2/NC05Y2EwLTJjNzRk/ZGI0MzI2Yy0xNjk0/MDMwODAxNTMyLmpw/Zw"

# Stuur een HTTP-verzoek om het bestand te downloaden
response = requests.get(url)

# Controleer of het verzoek succesvol was (statuscode 200)
if response.status_code == 200:
    # De naam van het lokale bestand waarin je de inhoud wilt opslaan
    bestandsnaam = "img_to_send"  # Vervang dit door de gewenste bestandsnaam

    # Schrijf de inhoud van de response naar het lokale bestand
    with open(bestandsnaam, "wb") as bestand:
        bestand.write(response.content)
    
    print(f"Het bestand is succesvol gedownload als '{bestandsnaam}'")
else:
    print("Fout bij het downloaden van het bestand")






home = '''
 ____                   ____                       ____        _   
/ ___| _ __   __ _ _ __/ ___|  ___ ___  _ __ ___  | __ )  ___ | |_ 
\___ \| '_ \ / _` | '_ \___ \ / __/ _ \| '__/ _ \ |  _ \ / _ \| __|
 ___) | | | | (_| | |_) |__) | (_| (_) | | |  __/ | |_) | (_) | |_ 
|____/|_| |_|\__,_| .__/____/ \___\___/|_|  \___| |____/ \___/ \__| 
                  |_|                                  [Mad for Max]

[1] Spamming 
'''
selected_1 = '''
__   __                     _           _           _     _ 
\ \ / /__  _   _    ___  ___| | ___  ___| |_ ___  __| |  / |
 \ V / _ \| | | |  / __|/ _ \ |/ _ \/ __| __/ _ \/ _` |  | |
  | | (_) | |_| |  \__ \  __/ |  __/ (__| ||  __/ (_| |  | |
  |_|\___/ \__,_|  |___/\___|_|\___|\___|\__\___|\__,_|  |_|

[What is your snapchat username?]
'''

print(home)

select = input("SnapScore Bot> ")



if select == "1":
    print(selected_1)
    username = input("\n username> ")
    time.sleep(0.5)
    print('''
[What is your password?]        
''')
    passwd = input("\n password> ")
    print('''
          
[Who do you want to spam?]        
''')
    spam = input("\n spam> ")
    google_account_name = input("What is you full google account name?\n google_account_name> ")
    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Vervang deze waarden door je eigen Snapchat-accountgegevens
username = (username)
password = (passwd)

# De naam van de contactpersoon aan wie je een bericht wilt sturen
ontvanger = (spam)

# Voeg de 'headless' optie toe om Chrome in headless modus te starten
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Vervang 'path/to/chromedriver' door de daadwerkelijke locatie van de chromedriver op je systeem
driver = webdriver.Chrome('/workspaces/dev/snapscore/chromedriver_snapscore')

# Open de Snapchat-website
driver.get("https://accounts.snapchat.com/accounts/login")

# Wacht even om ervoor te zorgen dat de pagina is geladen
time.sleep(1)

# Zoek het gebruikersnaamveld en vul je gebruikersnaam in
username_field = driver.find_element_by_name("username")
username_field.send_keys(username)

# Zoek het wachtwoordveld en vul je wachtwoord in
password_field = driver.find_element_by_name("password")
password_field.send_keys(password)

# Druk op Enter om in te loggen
password_field.send_keys(Keys.RETURN)

# Wacht even om de inlogactie te voltooien
time.sleep(5)

# Ga naar de chatpagina
driver.get("https://www.snapchat.com/add/" + ontvanger)

# Wacht even om ervoor te zorgen dat de chatpagina is geladen
time.sleep(1)

# Vervang 'path/to/img_to_send.jpg' door de daadwerkelijke locatie van de afbeelding die je wilt verzenden
afbeelding_pad = 'path/to/img_to_send.jpg'

# Zoek de knop om een afbeelding te uploaden en klik erop
upload_knop = driver.find_element_by_css_selector(".icon-chat-file")
upload_knop.click()

# Wacht even om ervoor te zorgen dat het uploadvenster is geladen
time.sleep(2)

# Zoek het veld voor het uploaden van een afbeelding en geef het het pad naar de afbeelding
upload_veld = driver.find_element_by_css_selector("input[type='file']")
upload_veld.send_keys(afbeelding_pad)

# Wacht even om het uploaden van de afbeelding te voltooien
time.sleep(5)

# Sluit de browser
driver.quit()
