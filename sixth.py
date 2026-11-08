import sys
import requests
from bs4 import BeautifulSoup
#po hledání možných řešení jsem použil BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    response = requests.get(url)
    
    hrefs = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #html.parser převede response.content do čitelnější podoby

        anchor_element = soup.find_all('a')
        #find_all nalezne veškeré výskyty "a" neboli odkazy

        for element in anchor_element:
            href = element.get('href')
            #pomocí get jsem získal hodnotu href
            hrefs.append(href)
            #přidá veškeré odkazy ze stránky do seznamu
            #níže v komentáři je možnost, která přidává pouze webové stránky

            #if href and href.startswith('http'):
                #hrefs.append(href)
                #ze zadání mi přišlo že hledáme odkazy na jiné webové stránky, tak jsem dal podmínku aby začínali na http
                #jakmile splnily, tak byly přidány do seznamu
    else:
        print(f"Chyba pri stahovani URL: {response.status_code}")
        
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        seznam = download_url_and_get_all_hrefs(url)
        print(seznam)
    # osetrete potencialni chyby pomoci vetve except
    except IndexError:
        print("Chyba: Nebyla nalezena URL adresa")

    except requests.exceptions.RequestException as e:
        print(f"Chyba pri stahovani URL: {e}")
    
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
