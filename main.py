import mysql.connector

from repositories.zakaznik_repository import ZakaznikRepository
from repositories.produkt_repository import ProduktRepository
from repositories.sklad_repository import SkladRepository
from repositories.polozka_repository import PolozkaRepository
from repositories.objednavka_repository import ObjednavkaRepository
from services.objednavka_service import ObjednavkaService
from services.report_service import ReportService

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TVOJE_HESLO",
    database="projekt_d1_db"
)

zak_repo = ZakaznikRepository(conn)
prod_repo = ProduktRepository(conn)
sklad_repo = SkladRepository(conn)
pol_repo = PolozkaRepository(conn)
obj_repo = ObjednavkaRepository(conn)

service = ObjednavkaService(
    conn, zak_repo, prod_repo, sklad_repo, pol_repo, obj_repo
)

report = ReportService(conn)

while True:
    print("1=Nový zákazník | 2=Objednávka | 3=Report | q=Konec")
    cmd = input("> ")

    if cmd == "1":
        j = input("Jméno: ")
        e = input("Email: ")
        k = float(input("Kredit: "))
        print("ID:", zak_repo.create(j, e, k))

    elif cmd == "2":
        zak = int(input("ID zákazníka: "))
        produkty = []

        while True:
            p = input("Produkt ID (enter = konec): ")
            if not p:
                break
            m = int(input("Množství: "))
            produkty.append((int(p), m))

        try:
            print("Objednávka ID:", service.create_order(zak, produkty))
        except Exception as e:
            print("CHYBA:", e)

    elif cmd == "3":
        for r in report.objednavky():
            print(r)

    elif cmd == "q":
        break
