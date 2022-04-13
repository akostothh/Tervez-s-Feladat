def iroda():
    eszkozok=[]
    for i in range(6):
        eszkozok.append(input("Kérem az eszköz nevét!"))

    for i in range(6):
        eszkozok.append(int(input("Kérem az eszköz árát!")))

    for i in range(6):
        eszkozok.append(int(input("Kérem az eszköz árát!")))
         
    print(eszkozok, end=" ")


iroda()         