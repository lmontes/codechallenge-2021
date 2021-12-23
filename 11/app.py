import sys

T = int(sys.stdin.readline())

for case in range(1, T+1):
    nfuncs, funcs_by_file = map(int, sys.stdin.readline().split(" "))
    functions = [sys.stdin.readline().strip() for _ in range(nfuncs)]

    tree_count = {}
    for f in functions:
        for i in range(len(f)):
            prefix = f[0:i+1]
            if prefix not in tree_count:
                tree_count[prefix] = 0
            tree_count[prefix] += 1

    # print(tree_count)

    score = 0

    while True:
        # Calculamos prefijo maximo
        max_prefix = ""
        for prefix in tree_count:
            if tree_count[prefix] >= funcs_by_file:
                if len(prefix) > len(max_prefix):
                    max_prefix = prefix

        # print(max_prefix)
        if max_prefix == "":
            break

        # Eliminamos (restamos) en entradas que sean subprefijos del prefijo maximo
        for i in range(len(max_prefix)):
            subprefix = max_prefix[0:i+1]
            tree_count[subprefix] -= funcs_by_file

            # Todos los conjuntos que se queden vacios se eliminan
            if tree_count[subprefix] == 0:
                del tree_count[subprefix]

        score += len(max_prefix)

        # print(tree_count)

    print(f"Case #{case}: {score}")

