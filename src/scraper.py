import requests
from bs4 import BeautifulSoup
from product import Product

def iegut_divanus():
    adrese = "https://www.ikea.lv/lv/products/dzivojama-istaba/divani"
    preces = []

    atbilde = requests.get(adrese)
    if atbilde.status_code != 200:
        print("Neizdevās ielādēt lapu:", atbilde.status_code)
        return preces

    soup = BeautifulSoup(atbilde.content, "html.parser")
    blokiem = soup.find_all(class_="itemBlock")

    for bloks in blokiem:
        try:
            kermenis = bloks.find(class_="card-body")
            nosaukums_bloks = kermenis.find("h3")
            nosaukums = nosaukums_bloks.get_text(strip=True)

            # Apraksts (ja ir)
            # apraksts_bloks = bloks.find("h4", class_="itemFacts")
            # apraksts = apraksts_bloks.get_text(strip=True) if apraksts_bloks else ""

            # Cena
            cenas_bloks = bloks.find(class_="itemPriceBox").find("p").find("span")
            if "data-price" in cenas_bloks.attrs:
                cena = cenas_bloks["data-price"]
            elif "data-pricefamily" in cenas_bloks.attrs:
                cena = cenas_bloks["data-pricefamily"]
            else:
                vesela = cenas_bloks.find(class_="price__integer")
                komata = cenas_bloks.find(class_="price__decimals")
                cena = f"{vesela.get_text(strip=True)}.{komata.get_text(strip=True)}" if vesela and komata else "0.00"

            # Pilns nosaukums
            pilns_nosaukums = nosaukums #if not apraksts else f"{nosaukums} – {apraksts}"

            # Saite uz preci
            link_tags = bloks.find_all("a", href=True)
            saite = ""
            for tag in link_tags:
                if tag["href"].startswith("/lv/products/"):
                    saite = "https://www.ikea.lv" + tag["href"]
                    break

            prece = Product(pilns_nosaukums, cena + " €", saite)
            preces.append(prece)

        except Exception as e:
            print("Kļūda, apstrādājot preci:", e)
            continue

    return preces
