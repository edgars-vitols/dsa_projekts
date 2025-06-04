from scraper import iegut_preces_no_adreses
import csv

def saglabat_csv(preces, fails="data/preces.csv"):
    with open(fails, mode='w', newline='', encoding='utf-8') as f:
        rakstitajs = csv.writer(f)
        rakstitajs.writerow(["Nosaukums", "Cena", "Saite"])
        for prece in preces:
            rakstitajs.writerow(prece.to_list())

def izvadit_preces(preces):
    for prece in preces:
        print(f"Nosaukums: {prece.nosaukums}")
        print(f"Cena: {prece.cena}")
        print(f"Saite: {prece.saite}")
        print("-" * 40)

def izveidot_faila_nosaukumu(adrese):
    dala = adrese.rstrip('/').split('/')[-1]
    return f"data/{dala}.csv" if dala else "data/preces.csv"

if __name__ == "__main__":
    adrese = input("Ievadi IKEA adresi: ").strip()
    preces = iegut_preces_no_adreses(adrese)
    if preces:
        izvadit_preces(preces)
        saglabat_csv(preces)
        print(f"Saglabāts: data/preces.csv")
    else:
        print("Netika atrastas nevienas preces.")
