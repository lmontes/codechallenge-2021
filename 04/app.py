import sys

NOTES = [
    ["A"],
    ["A#", "Bb"],
    ["B", "Cb"],
    ["C", "B#"],
    ["C#", "Db"],
    ["D"],
    ["D#", "Eb"],
    ["E", "Fb"],
    ["F", "E#"],
    ["F#", "Gb"],
    ["G"],
    ["G#", "Ab"],
]

LETTERS = list("ABCDEFG")

N = int(sys.stdin.readline())

for i in range(0, N):
    root = sys.stdin.readline().replace("\n", "")
    steps = sys.stdin.readline().replace("\n", "")

    # print(root, steps)

    # Buscamos nota de inicio
    index = 0
    for note in NOTES:
        if root in note:
            break
        index += 1

    # Buscamos letra de inicio
    lindex = LETTERS.index(root[0])

    # Añadimos primera nota
    scale = [root]

    # Vamos añadiendo las siguientes notas
    for st in steps[:-1]:
        if st == "s":
            index += 1
        else:
            index += 2
        if index >= len(NOTES):
            index = index % len(NOTES)

        lindex +=1
        if lindex >= len(LETTERS):
            lindex = lindex % len(LETTERS)

        if len(NOTES[index]) == 1:
            scale.append(NOTES[index][0])
        else:
            if NOTES[index][0][0] == LETTERS[lindex]:
                scale.append(NOTES[index][0])
            else:
                scale.append(NOTES[index][1])
    scale.append(root)

    scale = "".join(scale)

    print(f"Case #{i+1}: {scale}")
