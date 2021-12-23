import sys
from typing import Dict, List
from collections import deque


def division(l, r):
    if l % r > 0:
        return False, None
    return True, l // r   

operators = {
    "+": lambda l, r: (True, l + r),
    "-": lambda l, r: (True, l - r),
    "*": lambda l, r: (True, l * r),
    "/": division,
    "=": lambda l, r: (True, l == r)
}

priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "=": 0
}


def infix_to_postfix(tokens: List[str]):
    stack = deque()
    postfix = []
    for t in tokens:
        if t in operators:
            if len(stack) == 0:
                stack.append(t)
            else:
                if priority[t] <= priority[stack[-1]]:
                    while len(stack) and priority[t] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    stack.append(t)
                else:
                    stack.append(t)
        else:
            postfix.append(t)
    while len(stack):
        postfix.append(stack.pop())
    return postfix


def eval_infix_expression(expression: List[str]):
    stack = deque()
    for token in expression:
        if token in operators:
            rval = stack.pop()
            lval = stack.pop()

            ok, result = operators[token](lval, rval)
            if not ok:
                return False, None
            # print(f"{lval} {token} {rval} -> {result}")
            stack.append(result)
        else:
            stack.append(token)
    return True, stack.pop()


def evaluate(assignation: str, infix_expression: List[str], original_expression: str):
    expression_str = original_expression
    expression = [token for token in infix_expression]
    for i,ch in enumerate(assignation):
        if ch != "_":
            expression = [token.replace(ch, str(i)) for token in expression]
            expression_str = expression_str.replace(ch, str(i))
    expression = [int(token) if token.isdigit() else token for token in expression]

    ok, result = eval_infix_expression(expression)
    #print(expression_str, result, ok)
    if not ok:
        return False, expression_str

    return result, expression_str


def search(options: Dict[str, List[int]], original_expression: str, infix_expression: List[str]) -> List[str]:
    results = []
    n_options = len(options)

    def recursive_search(assignation: List[str], n_assigned: int, max_digit):
        if n_assigned == n_options:
            # print(assignation)
            result, expression = evaluate(assignation, infix_expression, original_expression)
            if result:
                results.append(expression)
        else:
            for ch in options:
                if ch not in assignation:
                    for digit in options[ch]:
                        if assignation[digit] == "_" and digit > max_digit:
                            recursive_search(assignation[:digit] + ch + assignation[digit+1:], n_assigned + 1, digit)
    
    recursive_search("__________", 0, -1)

    return list(sorted(results))


def solve(expression):
    original_expression = expression
    expression = original_expression.replace(" ", "")

    # Tokenize the expression
    op_index = []
    for i, ch in enumerate(expression):
        if ch in operators:
            op_index.append(i)
    # print(op_index)

    last = 0
    tokens: List[str] = []
    for i in range(len(op_index)):
        tokens.append(expression[last:op_index[i]])
        tokens.append(expression[op_index[i]])
        last = op_index[i] + 1
    tokens.append(expression[last:])

    postfix_tokens = infix_to_postfix(tokens)
    # print("TOKENS:", tokens, postfix_tokens)

    # Compute different letters and possible values
    letters = set()
    letters_not_zeros = set()
    for tok in tokens:
        if not tok in operators and not tok.isdigit():
            for ch in tok:
                letters.add(ch)
            letters_not_zeros.add(tok[0])

    # print(letters, letters_not_zeros)

    options = {}
    for ch in letters:
        if ch in letters_not_zeros:
            options[ch] = list(range(1, 10))
        else:
            options[ch] = list(range(10))

    # print(options)
    return search(options, original_expression, postfix_tokens)


N = int(sys.stdin.readline())

for case in range(1, N + 1):
    original_expression = sys.stdin.readline().strip()

    result = solve(original_expression)

    result_str = "IMPOSSIBLE"
    if len(result):
        result_str = ";".join(result)       

    print(f"Case #{case}: {result_str}")
