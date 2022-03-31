# 가장 큰 수 (stack)
num, count = map(int, input().split())
number = list(map(int, str(num)))

stack = list()
for n in number:
    while stack and count > 0 and stack[-1] < n:
        stack.pop()
        count -= 1
    stack.append(n)
# count까지 도달해지 못했을 경우
if count != 0:
    stack = stack[:-count]

answer = "".join(map(str, stack))  # join으로 string 붙이는 함수
print(answer)

##################################################################

# 쇠막대기 (스텍)
it = input()
stack = list()
cnt = 0
for i in range(len(it)):
    if it[i] == "(":
        stack.append(it[i])
    else:
        stack.pop()
        if it[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)

# 후위 표기식 만들기(스택)
a = input()
stack = list()
res = ""
for x in a:
    if x.isdecimal():  # 십진수 숫자이면
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":  # 여는 괄호르 만나면 멈춰야함
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()  # 여는 괄호를 없애버리기

while stack:
    res += stack.pop()

print(res)

###################################################################

# 후위 연산(스택)

a = input()
stack = list()
for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        if x == "*":
            n3 = n1 * n2
        elif x == "/":
            n3 = n2 / n1
        elif x == "+":
            n3 = n1 + n2
        else:
            n3 = n2 - n1
        stack.append(n3)
print(stack[0])
