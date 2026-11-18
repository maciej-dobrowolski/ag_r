import csv
import time
from datetime import timedelta

from wreq.blocking import Client

client = Client(timeout=timedelta(seconds=15))

with open("sets_export.csv", encoding="utf-8") as f:
    numery = [wiersz["set_number"] for wiersz in csv.DictReader(f)]

# 2. Dla każdego numeru zapytaj API i zapisz wynik
with open("ceny_promoklocki.csv", "w", encoding="utf-8", newline="") as f:
    save = csv.writer(f)
    save.writerow(["set_number", "price_promoklocki"])

    for numer in numery:
        a = client.get(f"https://api.promoklocki.pl/price/{numer}")

        if a.status.as_int() == 200:
            cena = a.json()["price"]
        else:
            cena = ""

        save.writerow([numer, cena])
        time.sleep(0.1)