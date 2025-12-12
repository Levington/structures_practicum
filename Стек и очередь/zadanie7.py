from dataclasses import dataclass
from typing import Any, Optional, List
import time

from zadanie5 import StackArray
priority = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
}

def to_rpn(expr: str) -> List[str]:
    output = []
    stack = StackArray()
    tokens = tokenize(expr)

    for tok in tokens:
        if tok.isdigit():
            output.append(tok)
        elif tok in "+-*/":
            while (not stack.empty() 
                   and stack.peek() in "+-*/"
                   and priority[stack.peek()] >= priority[tok]):
                output.append(stack.pop())
            stack.push(tok)
        elif tok == '(':
            stack.push(tok)
        elif tok == ')':
            while not stack.empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()

    while not stack.empty():
        output.append(stack.pop())

    return output


def eval_rpn(rpn: List[str]) -> float:
    st = StackArray()
    for tok in rpn:
        if tok.isdigit():
            st.push(int(tok))
        else:
            b = st.pop()
            a = st.pop()
            if tok == '+': st.push(a + b)
            elif tok == '-': st.push(a - b)
            elif tok == '*': st.push(a * b)
            elif tok == '/': st.push(a / b)
    return st.pop()


def tokenize(expr: str) -> List[str]:
    out = []
    num = ''
    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                out.append(num)
                num = ''
            if ch in '+-*/()':
                out.append(ch)
    if num:
        out.append(num)
    return out