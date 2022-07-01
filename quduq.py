
import random

print("Quduq qaychi qog'oz oyiniga xush kelibsiz!")
d=0
pc=0
f=0

for n in range(5):
        
        tanlov = int(input("1.quduq 2.qaychi 3.qog'ozdan birini tanlang: "))
        kompyuter = random.randint(1,3)
        
        if kompyuter == 1 and tanlov == 2 or kompyuter == 2 and tanlov == 3 or kompyuter == 3 and tanlov == 1:
            print('Kompyuter yutdi!')
            print(f"kompyuter tanlovi: {kompyuter} - foydalanuvchi tanlovi: {tanlov}")
            pc += 1
        elif kompyuter == tanlov:
            print('durrang!')
            print(f"kompyuter tanlovi: {kompyuter} - foydalanuvchi tanlovi: {tanlov}")
            d += 1
        else:
            print("Siz yutdingiz!")
            print(f"kompyuter tanlovi: {kompyuter} - foydalanuvchi tanlovi: {tanlov}")
            f += 1
print(f"kompyuter {pc} - {f} foydalanuvchi.\n durranglar soni: {d}")







