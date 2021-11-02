d = {"Один" : "Питон", "Два" : "C++", "Три" : "Java", "Четыре" : "C#"}

t = d.copy()
d.clear()
t.pop("Три")

t.update({"Новое" : "Kotlin"})
print(t)