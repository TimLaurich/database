import csv

def import_zakaznici(filepath, repo):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            repo.create(row['jmeno'], row['email'], float(row['kredit']))
