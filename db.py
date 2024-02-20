import sqlite3

db = sqlite3.connect("data.db")


def add_user(login: str, password: str):
    db.execute("INSERT into Users (login, password) VALUES(?, ?)", [login, password])
    db.commit()


def get_user_by_login(login: str):
    select = db.execute("SELECT login, password FROM Users WHERE login = ?;", [login])
    for user in select:
        return user


def get_all_logins():
    select = db.execute("SELECT login FROM Users;")
    logins = []
    for login in select:
        logins.append(login[0])

    return logins

