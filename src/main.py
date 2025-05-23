from scraper import iegut_divanus
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

if __name__ == "__main__":
    preces = iegut_divanus()
    if preces:
        izvadit_preces(preces)
        saglabat_csv(preces)
    else:
        print("Netika atrastas nevienas preces.")
