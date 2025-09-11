T = int(input())

for t_c in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    cnt = -1
    start_ind = 0
    
    while start_ind + k < n :
        moved = False

        for i in range(start_ind+k, start_ind, -1) :
            if i in charge:
                start_ind = i
                cnt += 1
                moved = True
                break

        if moved == False:
            cnt = 0
            break
                
    print(f'#{t_c} {cnt}')