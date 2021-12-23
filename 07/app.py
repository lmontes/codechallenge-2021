import re
import socket
from collections import deque


def mrecv():
    global SOCK
    return SOCK.recv(256).decode("utf-8").strip()

def msend(message):
    global SOCK
    #print(">> ", message)
    SOCK.send(message.encode("utf-8"))
    response = mrecv()
    #print("<< ",response)
    return response

def parse_position(pos_str):
    global POS_RGX
    match = POS_RGX.search(pos_str)
    return (int(match.group(1)), int(match.group(2)))

def where():
    message = msend("where am I")
    return parse_position(message)

def is_exit():
    message = msend("is exit?")
    return message != "No. Sorry, traveller..."

def look():
    message = msend("look")
    opts = message.split(":")[-1]
    return list(filter(None, opts.split(" ")))

def move(direction):
    message = msend(direction)
    new_position = parse_position(message)
    return new_position

def goto(position):
    message = msend(f"go to {position[0]},{position[1]}")
    return parse_position(message)

def bye():
    msend("bye")


def explore_bfs(Q):
    global VISITED, EXIT, PREV

    if len(Q) == 0 or EXIT is not None:
        return
    
    position = Q.popleft()
    
    goto(position)

    if is_exit():
        EXIT = position
        return
    
    for direction in look():
        new_position = move(direction)
        if new_position not in VISITED:
            VISITED.add(new_position)
            PREV[new_position] = position
            Q.append(new_position)
        goto(position)
    
    explore_bfs(Q)
 

if __name__ == "__main__":
    global SOCK, EXIT, VISITED, POS_RGX, PREV
    
    HOST = "codechallenge-daemons.0x14.net"
    PORT = 4321
    
    POS_RGX = re.compile("\(([0-9]+)[, ]+([0-9]+)\)")
    
    PREV = {}
    VISITED = set()
    EXIT = None
    
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect((HOST, PORT))

    message = mrecv()
    #print(message)

    start = where()

    #print("START:", start)

    Q = deque()
    Q.append(start)
    explore_bfs(Q)
    #print("EXIT:", EXIT)

    # Reconstruir camino
    pr = PREV[EXIT]
    path = [EXIT]
    while pr != start:
        path.append(pr)
        pr = PREV[pr]
    path.append(start)

    path = list(reversed(path))

    print(str(path).replace("[", "").replace("]", ""))

    bye()
