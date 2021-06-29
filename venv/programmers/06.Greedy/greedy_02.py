#문제 ㅄ임
def solution(name):
    answer = 0
    tmp = [min(ord(i) - ord('A'), ord('Z') + 1 - ord(i)) for i in name]
    name = tmp
    pos = 0
    move = 0

    #오른쪽 방향 우선 그리디탐색
    while sum(name) != 0:
        answer += name[pos]
        name[pos] = 0
        move += 1

        if name[(pos+move) % len(name)] != 0:
            pos = (pos+move) % len(name)
            answer += move
            move = 0
            continue
        elif name[(pos-move) % len(name)] != 0:
            pos = (pos-move) % len(name)
            answer += move
            move = 0
            continue

    return answer

def solution2(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]

    answer = 0
    where = 0

    while True:
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer


a = solution("JAN")
a2 = solution2("JAN")
b = solution("BBABAAAB")
b2 = solution2("BBABAAAB")
print(a, a2)
print(b, b2)
