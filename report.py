def mask_tel(cifry):
    return "+7 (" + cifry[1:4] + ") ***-**-" + cifry[9:]

def print_table(good):
    print(f"{'№':<3} {'ФИО':<25} {'Почта':<25} {'Телефон':<20} {'Группа':<10}")
    print("-" * 85)
    for i in range(len(good)):
        a = good[i]
        tel_mask = mask_tel(a["phone"])
        print(f"{i+1:<3} {a['fio']:<25} {a['mail']:<25} {tel_mask:<20} {a['group']:<10}")
    print("-" * 85)

def print_bad(bad):
    print("\nОтклонено строк:", len(bad))
    for b in bad:
        print(" строка", b[0], ":", b[1])
        print("   причина:", b[2])

def print_stat(good, bad, total_lines, stat):
    print("\nВсего строк в файле:", total_lines)
    print("Принято:", len(good), "| Отклонено:", len(bad))
    print("\nпо группам:")
    for g in stat:
        print(" ", g, "-", stat[g])

if __name__ == "__main__":
    pass