import sys
sys.stdin = open("input_1225.txt")

for tc in range(1, 11):
    _ = int(input())
    lst = list(map(int, input().split()))

    while True:
        success = False
        for i in range(1, 6):
            num = lst.pop(0)
            lst.append(num - i)
            if lst[-1] <= 0:
                success = True
                lst[-1] = 0
                break
        if success:
            break

    print(f"#{tc}", *lst)