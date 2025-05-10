import random

palavras = [
    "amigo", "bravo", "campo", "dedal", "escol", "folha", "grato", "haste", "ideal", "jovem",
    "lugar", "manta", "navio", "olhos", "prazo", "quero", "rumor", "sabor", "tarde", "unido",
    "vulto", "xampu", "zebra", "abalo", "broto", "clube", "drama", "etapa", "feira", "globo",
    "horta", "inicio", "jarra", "lente", "macro", "nuvem", "ovulo", "primo", "quase", "raiva",
    "sinal", "trama", "utilo", "vazio", "vento", "xingo", "zumbi", "banco", "corpo", "doido",
    "exato", "fardo", "genio", "humor", "indio", "junta", "linha", "midia", "nariz", "optico",
    "pardo", "quero", "resto", "serie", "tenso", "unico", "vacuo", "xisto", "zelar", "brisa",
    "cinto", "danca", "elite", "forca", "gruta"
]

key = random.choice(palavras) 
end = False
tent = 0

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