from validators import proverka_fio, proverka_pochty, proverka_tel
from report import print_table, print_bad, print_stat
from storage import read_file, save_results

def main():
    file_in = "anketa.txt"
    lines = read_file(file_in)
    if lines is None:
        print("Файл", file_in, "не найден")
        return

    good = []
    bad = []
    stat = {}

    for i in range(len(lines)):
        line = lines[i].strip()
        if line == "":
            continue
        
        chasti = line.split(";")
        if len(chasti) != 4:
            bad.append((i + 1, line, "полей не 4, а " + str(len(chasti))))
            continue
        
        fio, oshibka1 = proverka_fio(chasti[0])
        pochta, oshibka2 = proverka_pochty(chasti[1])
        tel, oshibka3 = proverka_tel(chasti[2])
        gruppa = chasti[3].strip().lower()
        
        if gruppa == "":
            oshibka4 = "пустая группа"
        else:
            oshibka4 = None
            
        if oshibka1 or oshibka2 or oshibka3 or oshibka4:
            prichina = oshibka1 or oshibka2 or oshibka3 or oshibka4
            bad.append((i + 1, line, prichina))
        else:
            anketa = {"fio": fio, "mail": pochta, "phone": tel, "group": gruppa}
            good.append(anketa)
            if gruppa not in stat:
                stat[gruppa] = 1
            else:
                stat[gruppa] += 1

    good.sort(key=lambda a: a["fio"])
    print_table(good)
    print_bad(bad)
    print_stat(good, bad, len(lines), stat)
    save_results(good, bad)
    print("\nСохранено: ok.txt и errors.txt")
    print("Программа завершена")
if __name__ == "__main__":
    main()