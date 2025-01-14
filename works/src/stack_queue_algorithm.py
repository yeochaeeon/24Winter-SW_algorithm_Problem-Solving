## programmers - 올바른 괄호 문제 : C++로 풀기 
def is_valid_parentheses(input_lst):
    mapping = {")":"(","}":"{","]":"["} 
    stack = []
    for s in input_lst:
        if s in mapping: # 닫힌 괄호인 경우 
            if stack and (stack[-1] == mapping[s]):
                stack.pop()
            else:
                return False
        else: # 열린 괄호인 경우 
            stack.append(s)
    return not stack

# print(is_valid_parentheses(["(",")"])) # True
# print(is_valid_parentheses(["(","[",")","]"])) # False
# -------------------------------------------------------



# 전위 : prefex , 중위 : infix , 후위 : postfix
# 중위 전위 / 후위 : 1 + 1 => + 1 1 
    # 최단거리 중 휴게소를 최소한으로 들르는 방법
    # 운전자의 피로도를 k이상 유지하기 위해 들려야 하는 휴게소 방문 횟수

def infix_to_prefix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    tokens = []
    token = ""
    i = 0
    while i < len(expression):
        if expression[i].isalnum():
            token = ""
            while i < len(expression) and expression[i].isalnum():
                token += expression[i]
                i += 1
            tokens.append(token)
        elif expression[i] in precedence or expression[i] in "()":
            tokens.append(expression[i])
            i += 1
        else:
            i += 1

    operators = []
    output = []
    for token in reversed(tokens):
        if token.isalnum():
            output.append(token)
        elif token == ")":
            operators.append(token)
        elif token == "(":
            while operators and operators[-1] != ")":
                output.append(operators.pop())
            operators.pop()
        else:
            while (
                operators
                and operators[-1] != ")"
                and precedence.get(token, 0) < precedence.get(operators[-1], 0)
            ):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return " ".join(reversed(output))