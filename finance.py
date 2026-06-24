import json

def main():
    data = []
    try:
        f = open("data.json", "r")
        data = json.load(f)
        f.close()
    except:
        data = []

    while True:
        print("1. Доход")
        print("2. Расход")
        print("3. История")
        print("4. Баланс")
        print("5. Удалить")
        print("6. Выход")
        
        v = input("Что делаем? ")

        if v == "1":
            s = input("Сумма: ")
            k = input("Категория: ")
            d = {"type": "Доход", "amount": float(s), "category": k}
            data.append(d)
            f = open("data.json", "w")
            json.dump(data, f)
            f.close()

        elif v == "2":
            s = input("Сумма: ")
            k = input("Категория: ")
            d = {"type": "Расход", "amount": float(s), "category": k}
            data.append(d)
            f = open("data.json", "w")
            json.dump(data, f)
            f.close()

        elif v == "3":
            for i in data:
                print(i)

        elif v == "4":
            bal = 0
            for i in data:
                if i["type"] == "Доход":
                    bal = bal + i["amount"]
                else:
                    bal = bal - i["amount"]
            print("Баланс:", bal)

        elif v == "5":
            data.pop()
            f = open("data.json", "w")
            json.dump(data, f)
            f.close()

        elif v == "6":
            break

main()