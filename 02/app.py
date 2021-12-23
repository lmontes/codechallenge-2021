import sys

N = int(sys.stdin.readline())

for i in range(0, N):
    line = sys.stdin.readline().replace("\n", "").split(" ")

    P, R, C = map(int, line)

    pokemon = set()
    for _ in range(0, P):
        pokemon.add(sys.stdin.readline().replace("\n", "").upper())

    mapa = []
    for _ in range(0, R):
        mapa.append(sys.stdin.readline().replace("\n", "").replace(" ", "").upper())
    mapa = "".join(mapa)

    while len(pokemon):
        to_remove = []
        for p in pokemon:
            replaced = mapa.replace(p, "")
            if len(replaced) < len(mapa):
                mapa = replaced
                to_remove.append(p)
            replaced = mapa.replace(p[::-1], "")
            if len(replaced) < len(mapa):
                mapa = replaced
                to_remove.append(p)
        for p in to_remove:
            pokemon.remove(p)

    print(f"Case #{i+1}: {mapa}")