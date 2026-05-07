# definicja prostej struktury danych obejmujących przykladowego uzytkownika
from os import remove

users = [{"name": "Artur", "location": "Łomża",
        "posts": ["Sprzedam mercedesa", "Kupię skrzynię biegów", "Ratunku co robić po wypadku", "Kto dzisiaj idzie biegac?"]},
         {"name": "Daniel", "location": "Legionowo",
        "posts": ["Moj kod nie dziala pomocy"]},
        {"name": "Kamil", "location": "Ciechanów",
        "posts": ["Czy ktos juz zrobil sprawozdanie z PPyth"]},

]

def read_users(users_data: list)->None:
    for user in users_data:
        print(f"Twoj znajomy {user['name']} z miejscowosci {user['location']} opublikowal post {user['posts'][-1]}")


def add_user(users_data: list)->None:
    users_data.append({"name": input("Podaj imie uzytkownika: "), "location": input("Podaj swoja lokalizacje: "),
        "posts": ["Dołączono do znajomych"]})




def remove_user(users_data: list)->None:
    user_to_remove = input("Podaj imie znajomego do usuniecia: ")
    for user in users_data:
        if user["name"] == user_to_remove:
                users.remove(user)



def update_user(users_data: list)->None:
    user_to_update = input("Podaj imie znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową lokalizację: ")

def update_user_post(users_data: list)->None:
    user_to_update = input("Podaj imie znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Napisz co słychać: "))

while True:
    print("=====MENU======")
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodanie znajomego")
    print("3 - usuwanie znajomego")
    print("4 - tworzenie posta")
    print("5 - update znajomego")
    choice=input("Wybierz opcję w menu: ")
    print(f"Wybrano opcję {choice}")
    if choice == "0":
        break


    if choice == "1":
        read_users(users)
    if choice == "2":
        add_user(users)
    if choice == "3":
        remove_user(users)
    if choice == "4":
        update_user(users)
    if choice == "5":
        update_user_post(users)
