# 단어 찾기(해쉬)
n = int(input())
poem = dict()
for _ in range(n):
    word = input()
    poem[word] = 0

for _ in range(n - 1):
    word = input()
    poem[word] += 1

for k, v in poem.items():
    if v == 0:
        print(k)
        break

########################################################################

# Anagram(아나그램: 구글 인터뷰 문제)
n1 = input()
n2 = input()
first = dict()
second = dict()
for w in n1:
    if w in first:
        first[w] += 1
    else:
        first[w] = 1
# 혹은 first[w] = first.get(w, 0) + 1

for w in n2:
    if w in second:
        second[w] += 1
    else:
        second[w] = 1

if first == second:
    print("YES")
else:
    print("NO")

########################################################################

# Anagram(리스트 해쉬)
# ASCII로 풀기
n1 = input()
n2 = input()
str1 = [0] * 52
str2 = [0] * 52
for w in n1:
    if w.isupper():
        str1[ord(w) - 65] += 1  # 대문자면 -65
    else:
        str1[ord(w) - 71] += 1  # 소문자면 -71

for w in n2:
    if w.isupper():
        str2[ord(w) - 65] += 1
    else:
        str2[ord(2) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
