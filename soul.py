import random


# приветствие
HELLO = "Привет 🤗, я ЛитлБотик! Маленький, но частино живой"
with open("files/photo.jpg", "rb") as ph:
    photo = ph.read()


def miss_msg():
    """Если сообщение не опознанно"""
    lst_msg = [
        "Что-то не так.. Не понял немного 😳😬☹, попробуй еще написать",
        "Упс 🥺 не верно, еще разочек",
        "Я еще многово в этой жизни не понимаю 🙂 но это точно не то 🥺. Напиши еще раз но по другому 😇"
    ]
    return random.choice(lst_msg)


def file_to_list(file):
    """Преобразование содержимое файла в список"""
    lst = list()
    with open(file, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if "=" not in line:
                lst.append(line[line.index("*") + 1: line.index(";")].strip().split(", "))
    return lst


def file_to_gen(file):
    """Преобразование содержимое файла в генератор"""
    with open(file, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if "=" not in line:
                yield line[line.index("*") + 1: line.index(";")].strip()


def out_gen(gen):
    """Обработка генератора"""
    return next(gen)


def check(lst, msg):
    """Проверка наличия ответа"""
    if len(lst) < 1:
        return False
    for i in lst[0]:
        if i in msg:
            lst.pop(0)
            return True


def msg_to_file(user_id, msg):
    """Сохраняет входяшие сообщения в файле (на память)"""
    with open(f"files/users/{user_id}_massage.txt", "a", encoding="UTF-8") as f:
        f.write(f"{'='*10}\n{msg}\n")


answer = file_to_gen("files/answer.txt")
coincidence = file_to_list("files/coincidence.txt")
