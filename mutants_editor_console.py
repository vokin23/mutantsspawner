def receiving_mutants():
    mutabts_day = ["day", "night", "evening", "morning"]
    classname = input("������� ��������� ���������.\n")
    counts = input("������� ���������� ���������.\n")
    cords = input("������� ���������� ���������.\n")
    cords = cords[cords.find("<") + 1:cords.find(">")].replace(",", "").split(" ")
    cords[1] = "0"
    for item in mutabts_day:
        with open(f'{item}.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{classname}|{" ".join(cords)}|{counts}|3600')
            print(f'������� {classname} ��������� � ���� {item}!')


k = 0
while 1:
    receiving_mutants()
    k += 1
    print(f"{k} ���� ��������!")
