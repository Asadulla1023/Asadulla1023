x = "HA"
with open('log.txt',"a") as log:
    while x == "HA":
        name = input("Login kiriting:\n ")
        input("Parol kiriting:\n ")
        print("Salom", name.title())
        from datetime import datetime
        log.write(f'{name} tizimga {datetime.now()} vaqtda kirdi\n')
        x = input("Davom etasizmi?\nKiriting(ha/yo'q)>>> ").upper()
