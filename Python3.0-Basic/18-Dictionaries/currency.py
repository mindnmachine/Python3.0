currency = {"India": "Rupee", "USA": "Dollar", "Russia": "Ruble", "Japan": "Yen","Germany": "Euro"}
def main():
    print("List of Countries")
    for key in currency.keys():
        print(key)
    print("List of Currencies in different Countries")
    for value in currency.values():
        print(value)
    for key, value in currency.items():
        print(f"'{key}' has a currency of type '{value}'")

if __name__ == "__main__":
    main()