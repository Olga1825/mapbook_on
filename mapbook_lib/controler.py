def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twoj znajomy {user['name']} z miejscowosci {user['location']} opublikowal post {user['posts'][-1]}")


def add_user(users_data: list) -> None:
    users_data.append({
        "name": input("Podaj imie uzytkownika: "),
        "location": input("Podaj swoja lokalizacje: "),
        "posts": ["Dołączono do znajomych"]
    })


def remove_user(users_data: list) -> None:
    user_to_remove = input("Podaj imie znajomego do usuniecia: ")

    for user in users_data:
        if user["name"] == user_to_remove:
            users_data.remove(user)
            break


def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do update: ")

    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową lokalizację: ")
            break


def update_user_post(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do update: ")

    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Napisz co słychać: "))
            break


def get_user_map(users_data: list) -> None:
    print("Mapa znajomych będzie dodana później.")
