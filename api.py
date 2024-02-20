import db
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_hashed_password(password):
    return pwd_context.hash(password)


def registration(login: str, password: str):
    print(db.get_all_logins())
    if login in db.get_all_logins():
        return "Такой логин уже существует"

    password_hash = get_hashed_password(password)

    db.add_user(login, password_hash)

    return "Регистрация прошла успешно"


def authorize(login: str, password: str):
    user = db.get_user_by_login(login)
    if user is None:
        return "Такого пользователя не существует"

    if login == user[0] and verify_password(password, user[1]):
        return "Вы успешно авторизовались"

    return "Неверный логин или пароль"

