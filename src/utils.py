import json
from datetime import datetime


def working_file(fail_name):
    """"""
    with open(fail_name) as load_file:
        return json.load(load_file)


def examination(load_file):
    """"""
    load_item = list(filter(lambda x: len(x) and x["state"] == "EXECUTED", load_file))
    return load_item


def sort_by_date(it):
    """"""
    list_by_date = sorted(it, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return list_by_date


def change_date(d):
    """"""
    return f"{d[8:10]}.{d[5:7]}.{d[0:4]}"


def change_map(m):
    """"""
    number = m.split()
    if number[0] == "Счет":
        return 'Счет **' + m[-4:]
    else:
        card_name = " ".join(number[:-1])
        return card_name + ' ' + number[-1][:4] + ' ' + number[-1][4:6] + '** ****' + number[-1][-4:]


def valuda(operations):
    """"""
    return f"{operations["operationAmount"]["amount"]} {operations["operationAmount"]["currency"]["name"]}"


def get_main(number_operations=5):
    working = working_file("operations.json")
    executed = examination(working)
    date = sort_by_date(executed)
    for item in date:
        if number_operations == 0:
            break
        print(change_date(item["date"]), item["description"])
        if item["description"] != "Открытие вклада":
            print(change_map(item["from"]) + " -> ", end="")
        print(change_map(item["to"]))
        print(valuda(item))
        number_operations -= 1


get_main()
