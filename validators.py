def proverka_fio(fio):
    slova = fio.split()
    if len(slova) < 2:
        return None, "в ФИО меньше двух слов"
    return " ".join(slova).title(), None

def proverka_pochty(pochta):
    pochta = pochta.strip().lower()
    if pochta.count("@") != 1:
        return None, "почта неверная: нет @ или их несколько"
    chasti = pochta.split("@")
    if len(chasti[0]) == 0 or len(chasti[1]) == 0:
        return None, "почта неверная: пустая часть"
    domen = chasti[1]
    if "." not in domen or domen.startswith(".") or domen.endswith("."):
        return None, "почта неверная: ошибка в домене"
    return pochta, None

def proverka_tel(telefon):
    cifry = ""
    for c in telefon:
        if c.isdigit():
            cifry += c
    if len(cifry) != 11:
        return None, "телефон неверный: не 11 цифр"
    if cifry[0] not in "78":
        return None, "телефон неверный: не начинается на 7 или 8"
    if cifry[0] == "8":
        cifry = "7" + cifry[1:]
    return cifry, None

if __name__ == "__main__":
    pass