
evszam = int (input("Melyik évben születél?"))
print(evszam)
kor = 2026 - evszam
print(kor, "éves vagy!")

if 18 < kor:
    print("Felnőt vagy!")

elif 18 == kor:
    print("Pont 18 éves vagy!")

else :
    print("Gyerek vagy!")










