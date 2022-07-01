import random
import os



# bu yerda yangi kodlar yozildi


# yana yangi kod qo'shildi



def menu():
    ishora = True
    while True:
        if ishora:
            print("\n\n MATEMATIKA o'yin dasturi \n bu dasturda siz o'z bilingizni sinab ko'rasiz."
            "\ndasturni ishga tushirirsh uchun quyidagi nebu'dan kerakli darajani tanlang.")
            tanlov = input ("""\nkerakli bo'limni tanlang
1. OSON,
2. O'RTA,
3. QIYIN,
4. ORTGA...
1 va 4 oralig'idagi son kiriting.
Kiriting: """)
            ishora = False
        else:
            tanlov = input("Xato, 1 va 4 oralig'idagi son kiriting.")

        if tanlov.isdigit() and int(tanlov) in range(1,5):
            return int(tanlov)

def play(daraja):
    takror = 5
    user_ball = 0 
    for i in range(takror):
        amallar = random.choice(['+','-','*','/'])
        masala = None
        javob = None
        for son in range(daraja + 1):
            a = random.randint(1,25)
            if son == 0:
                masala = str(a)
                javob = a
            else:
                masala += f"{amallar} {a}"
                if amallar == '+':
                    javob += a
                elif amallar == '-':
                    javob -= a
                elif amallar == '*':
                    javob *= a
                if amallar == "/":
                    javob = round(javob / a, 2)
        natija = input(f"Misolni javobini yozing: {masala} = ")
        if float(natija) == javob:
            print("Javob to'g'ri!")
            user_ball += 1
        else:
            print(f"Xato, to'gri javob: {javob}\n")
    print(f"Siz {takror} savoldan {user_ball}-ta to'g'ri javob topdingiz")

while True:
    os.system('cls')
    tanlov = menu()
    if tanlov == 1:
        print("\nHurmatli o'yinchi siz menudan <<OSON>> bo'limini tanlading:")
        play(daraja=1)
    elif tanlov == 2:
        print("\nHurmatli o'yinchi siz menudan <<O'RTA>> bo'limini tanlading:")
        play(daraja=2)
    elif tanlov == 3:
        print("\nHurmatli o'yinchi siz menudan <<QIYIN>> bo'limini tanlading:")
        play(daraja=3)
    elif tanlov == 4:
        print("Siz dasturdan chiqdingiz!")
        break

    savol = input("Yana o'yin o'ynaysizmi? | ha/yoq: ")
    if savol == "ha":
        continue
    else:
        print("o'yin tugadi!")
        break


