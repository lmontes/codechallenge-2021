# pip install numpy
import sys
import numpy as np
from collections import deque


def compute_max_earning(G: np.array, start_node:int, end_node:int):
    max_earning = 1
    min_path_len = None
    queue = deque([[start_node]])

    while len(queue):
        path = queue.popleft()
        last_node = path[-1]

        if min_path_len is not None and len(path) == min_path_len and last_node == end_node:
            earning = compute_path_earning(G, path)
            if earning > max_earning:
                max_earning = earning

        if min_path_len is None:
            for dst in np.nonzero(G[last_node])[0]:
                if not dst in path[1:]:
                    new_path = path + [dst]
                    queue.append(new_path)
                    if dst == end_node:
                        min_path_len = len(new_path)
        elif len(path) < min_path_len:
            for dst in np.nonzero(G[last_node])[0]:
                if not dst in path[1:]:
                    new_path = path + [dst]
                    queue.append(new_path)

    return max_earning


def compute_path_earning(G: np.array, path: list):
    earning = 1
    for i in range(len(path) - 1):
        src, dst = path[i], path[i+1]
        earning *= G[src][dst]
        # print((src, dst), G[src][dst])
    return earning


N = int(sys.stdin.readline())

for case in range(1, N+1):
    nwebs = int(sys.stdin.readline())

    trades = []
    cryptos = set()
    name2id = {}
    for _ in range(nwebs):
        web, ntrades = sys.stdin.readline().strip().split(" ")
        ntrades = int(ntrades)

        for _ in range(ntrades):
            src, val, dst, = sys.stdin.readline().strip().split("-")

            val = int(val)

            cryptos.add(src.upper())
            cryptos.add(dst.upper())

            trades.append((src.upper(), dst.upper(), val))

    ncryptos = len(cryptos)

    # print(ncryptos, len(trades))

    if "BTC" in cryptos:
        # Asignamos un id a cada criptomoneda, BTC siempre será el 0
        name2id["BTC"] = 0
        cryptos.remove("BTC")
        for id, coin in enumerate(sorted(cryptos), start=1):
            name2id[coin] = id

        # Creamos el grafo
        graph = np.zeros((ncryptos, ncryptos), dtype=int)
        for (src, dst, val) in trades:
            # Si hay varios cambios entre dos tipos de criptomonedas
            # nos quedamos con el de mayor valor
            if val > graph[name2id[src]][name2id[dst]]:
                graph[name2id[src]][name2id[dst]] = val

        # print(graph)

        result = compute_max_earning(graph, 0, 0)
    else:
        result = 1

    print(f"Case #{case}: {result}")
