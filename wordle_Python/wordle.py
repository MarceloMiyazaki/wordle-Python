import random

tamanho = int(input("Numero de letras na palavra -->"))

s = ""
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
palavras = []

with open("palavras.txt" ,"r") as file:
    s = file.read()

atual = ""
for char in s:
    if char == "\n":
        if atual[1:][0] not in maiusculas and len(atual[1:]) == tamanho:
            palavras.append(atual[1:])
        atual = ""
    atual += char

key = random.choice(palavras) 
end = False
tent = 0

print("*"*tamanho)

while True:
    if not end:
        dic = {}
        abs = []
        a = str()

        for i in key:
            abs.append(i)

        resp = input()

        for i in range(len(key)):
            dic[i] = "\033[91m"

        if resp == key:
            end = True

        if len(resp) != len(key):
            print("palavra incompativel")

        if len(resp) == len(key):
            tent += 1
            for i in range(len(key)):
                if resp[i] == key[i]:
                    dic[i] = ("\033[92m")
                    abs[i] = ("!")

            for i in range(len(key)):
                if resp[i] in abs and dic[i] != "\033[92m":
                    dic[i] = ("\033[93m")
                    abs.remove(resp[i])

            for i in range(len(key)):
                a = a + dic[i] + resp[i]
            print(a + "\033[0m")

    if end:
         print("============= \nPARABÉNS!!!!\n=============\nTentativas:", tent)
         print(key)
         key = input("Nova chave: ")
         tent = 0
         print("\n"*75)
         end = False