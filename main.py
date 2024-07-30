# Definice třídy pro pojištěnou osobu
class InsuredPerson:
    def __init__(self, first_name, last_name, age, phone_number):
        # Validace vstupu pro jméno a příjmení
        if not first_name or not last_name:
            raise ValueError("Jméno a příjmení nesmí být prázdné.")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    # Metoda pro převod objektu na řetězec
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Věk: {self.age}, Tel.: {self.phone_number}"


# Definice třídy pro správu pojištěných osob
class InsuranceManager:
    def __init__(self):
        # Inicializace prázdného seznamu pojištěných osob
        self.insured_persons = []

    # Metoda pro přidání nové pojištěné osoby
    def add_person(self, person):
        self.insured_persons.append(person)

    # Metoda pro získání seznamu všech pojištěných osob
    def get_all_persons(self):
        return self.insured_persons

    # Metoda pro vyhledání pojištěné osoby podle jména a příjmení
    def find_person(self, first_name, last_name):
        return [person for person in self.insured_persons if
                person.first_name.lower() == first_name.lower() and person.last_name.lower() == last_name.lower()]


# Funkce pro načtení uživatelského vstupu
def get_user_input(prompt):
    return input(prompt).strip()


# Funkce pro vytvoření nové pojištěné osoby
def create_person():
    first_name = get_user_input("Zadejte jméno: ")
    last_name = get_user_input("Zadejte příjmení: ")
    age = get_user_input("Zadejte věk: ")
    phone_number = get_user_input("Zadejte telefonní číslo: ")
    return InsuredPerson(first_name, last_name, age, phone_number)


# Hlavní funkce aplikace
def main():
    # Inicializace správce pojištěných osob
    manager = InsuranceManager()

    while True:
        # Hlavní menu aplikace
        print("\nEvidence pojištěných osob")
        print("1. Vytvořit pojištěného")
        print("2. Zobrazit všechny pojištěné")
        print("3. Vyhledat pojištěného podle jména a příjmení")
        print("4. Konec")

        # Načtení volby uživatele
        choice = get_user_input("Zadejte volbu: ")

        if choice == "1":
            # Přidání nové pojištěné osoby
            try:
                person = create_person()
                manager.add_person(person)
                print("Pojištěná osoba byla přidána.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Zobrazení seznamu všech pojištěných osob
            persons = manager.get_all_persons()
            if persons:
                for person in persons:
                    print(person)
            else:
                print("Žádné pojištěné osoby nejsou evidovány.")

        elif choice == "3":
            # Vyhledání pojištěné osoby podle jména a příjmení
            first_name = get_user_input("Zadejte jméno: ")
            last_name = get_user_input("Zadejte příjmení: ")
            found_persons = manager.find_person(first_name, last_name)
            if found_persons:
                for person in found_persons:
                    print(person)
            else:
                print("Pojištěná osoba nebyla nalezena.")

        elif choice == "4":
            # Ukončení aplikace
            print("Ukončuji aplikaci.")
            break

        else:
            # Neplatná volba
            print("Neplatná volba, zkuste to znovu.")


# Spuštění hlavní funkce, pokud je soubor spuštěn jako hlavní program
if __name__ == "__main__":
    main()
