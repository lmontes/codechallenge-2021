
SURNAME = "MANDELA"


with open("Invictus.txt", "rb") as f:
    text = f.read().decode("utf-8")

# El texto tiene caracteres extraños que nos son ASCII
text = list(
    filter(
        lambda ch: ch > 127,
        map(ord, text)
    )
)

# print(text)

# Como los caracteres no son legibles, suponemos cifrado César
for i in range(len(text)-5):
    if text[i] == text[i+5]: # Distancia entre las A de MANDELA
        # print(i, text[i])

        despl = text[i] - ord("A")

        deciphered = "".join(list(map(lambda ch: chr(ch-despl), text)))

        if SURNAME in deciphered:
            print(deciphered)
