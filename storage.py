def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return None

def save_results(good, bad):
    with open("ok.txt", "w", encoding="utf-8") as f:
        for a in good:
            f.write(a["fio"] + ";" + a["mail"] + ";" + a["phone"] + ";" + a["group"] + "\n")
    with open("errors.txt", "w", encoding="utf-8") as f:
        for b in bad:
            f.write("Строка " + str(b[0]) + ": " + b[1] + "\n")
            f.write("Причина: " + b[2] + "\n\n")

if __name__ == "__main__":
    pass