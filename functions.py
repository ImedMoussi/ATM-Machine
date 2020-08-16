from __MiniProjet import dab_db as db
from datetime import datetime
import numpy as np


def client_code_request():
    """This function return a client name before it check the name already exist in my bdd or not"""
    codes = [i[0] for i in db.clients()]
    while True:
        code = input("- Donner le code client: ")
        if code not in codes:
            print(f"\t-> Le client -{code}- n'existe pas.\n")
            continue
        return code


def no_card_request():
    num_cartes = [i[2] for i in db.cards()]
    while True:
        num_carte = input("- Le numéro de carte: ")
        if num_carte not in num_cartes:
            print("\t-> Cette carte n'existe pas.\n")
            continue
        return num_carte


def generate_client_code():
    while True:
        code = str(np.random.randint(1, 99999)).ljust(5, "0")
        codes = [i[0] for i in db.clients()]
        if code in codes:
            continue
        return code


def generate_account_number():
    accounts = [int(i[0]) for i in db.accounts()]
    num_compte = 1
    while True:
        if num_compte in accounts:
            num_compte += 1
            continue
        return str(num_compte)


def generate_card_number():
    lst = list()
    while True:
        for i in range(4):
            s = str(np.random.randint(1, 9999)).ljust(4, '0')
            lst.append(s)
        num = '-'.join(lst)
        num_cartes = [i[2] for i in db.cards()]
        if num in num_cartes:
            continue
        return num


def generate_secret_code():
    while True:
        code = int(str(np.random.randint(1, 9999)).ljust(4, "0"))
        codes = [i[3] for i in db.cards()]
        if code in codes:
            continue
        return code


def exp_date():
    year = datetime.now().year + 4
    month = datetime.now().month
    day = datetime.now().day
    return datetime(year, month, day).date()
