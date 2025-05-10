#key corresponde a palavra a ser adivinhada
key = ("audio")
end = False

while True:
    if not end:
        dic = []
        abs = []

        for i in key:
            abs.append(i)

        for i in range(len(key)):
            dic.append("X")

        resp = input()

        if resp == key:
            end = True
            continue

        if len(resp) != len(key):
            print("palavra incompativel")

        if len(resp) == len(key):
            for i in range(len(key)):
                if resp[i] == key[i]:
                    dic[i] = ("O")
                    abs[i] = ("!")

            for i in range(len(key)):
                if resp[i] in abs and dic[i] != "O":
                    dic[i] = ("!")
                    abs.remove(resp[i])

            print(dic)

    if end:
         print("parabens")
         key = input("Nova chave: ")
         print("\n"*75)
         end = False