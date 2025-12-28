class ObjednavkaService:

    def __init__(self, conn, zak_repo, prod_repo, sklad_repo, pol_repo, obj_repo):
        self.conn = conn
        self.zak_repo = zak_repo
        self.prod_repo = prod_repo
        self.sklad_repo = sklad_repo
        self.pol_repo = pol_repo
        self.obj_repo = obj_repo

    def create_order(self, zakaznik_id, produkty):
        try:
            self.conn.start_transaction()

            objednavka_id = self.obj_repo.create(zakaznik_id)

            total = 0
            for produkt_id, mnozstvi in produkty:
                produkt = self.prod_repo.get(produkt_id)
                sklad = self.sklad_repo.get(produkt_id)

                if sklad[1] < mnozstvi:
                    raise Exception("Nedostatek zboží")

                self.pol_repo.add(objednavka_id, produkt_id, mnozstvi)
                self.sklad_repo.update(produkt_id, sklad[1] - mnozstvi)

                total += produkt[2] * mnozstvi

            zak = self.zak_repo.get(zakaznik_id)
            if zak[4] < total:
                raise Exception("Nedostatek kreditu")

            self.zak_repo.update_kredit(zakaznik_id, zak[4] - total)

            self.conn.commit()
            return objednavka_id

        except Exception as e:
            self.conn.rollback()
            raise e
