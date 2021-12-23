import re
import sys
from fractions import Fraction


DICT_KV = re.compile("['\"]([^'\"]+)['\"][ ]*:[ ]*([0-9\/]+)")
TUPLE_KV = re.compile("\(['\"]([^'\"]+)['\"][ ]*,[ ]*([0-9\/]+)\)")
LIST_KV = re.compile("(\w)[ ]*=[ ]*([0-9\/]+)")


def score(word, weights):
    result = 0
    for letter in word:
        result += weights.get(letter, 0)
    return result


def get_winner(w1, w2, weights):
    s1 = score(w1, weights)
    s2 = score(w2, weights)

    if s1 == s2:
        return "-"
    elif s1 > s2:
        return w1
    else:
        return w2


def parse_weights_as_dict(weights_str):
    return { match.group(1): Fraction(match.group(2)) for match in DICT_KV.finditer(weights_str)}

def parse_weights_as_tuple_list(weights_str):
    return { match.group(1): Fraction(match.group(2)) for match in TUPLE_KV.finditer(weights_str)}

def parse_weights_as_key_value(weights_str):
    return { match.group(1): Fraction(match.group(2)) for match in LIST_KV.finditer(weights_str)}


N = int(sys.stdin.readline())

for i in range(0, N):
    line = sys.stdin.readline().replace("\n", "")

    words, raw_weights = line.split("|")

    w1, w2 = words.split("-")
    
    weights = {}

    if "=" in raw_weights:
        weights = parse_weights_as_key_value(raw_weights)
    elif "{" in raw_weights:
        weights = parse_weights_as_dict(raw_weights)
    else:
        weights = parse_weights_as_tuple_list(raw_weights)

    # print(w1, w2, raw_weights)
    #print(w1, w2, weights)

    result = get_winner(w1, w2, weights)

    print(f"Case #{i+1}: {result}")

