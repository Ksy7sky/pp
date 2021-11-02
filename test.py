slaves = {
    'student1' : {
        "Имя" : "Катя",
        "Возраст" : "15",
        "Средняя оценка" : "4.6"
    },
    'student2' : {
        "Имя" : "Коля",
        "Возраст" : "16",
        "Средняя оценка" : "3.2"
    },
    'student3' : {
        "Имя" : "Петр",
        "Возраст" : "15",
        "Средняя оценка" : "4.8"
    },
    'student4' : {
        "Имя" : "Маша",
        "Возраст" : "16",
        "Средняя оценка" : "4.9"
    },
}

# for key, value in slaves.items():
#     for key2, value2 in value.items():
#         print(key2, " - ", value2)

def getSlave(name):
    for key, value in slaves.items():
        if value["Имя"] == name:
            for key2, value2 in value.items():
                print(key2, " - ", value2)

getSlave("Коля")