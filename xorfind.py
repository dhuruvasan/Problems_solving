def encode(st):
    n = len(st)
    i = 0
    while i < n- 1:

        count = 1
        while (i < n - 1 and st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1

        print(st[i - 1] + f'{count}' ,end = "")


str='aaabbbcccdss'
encode(str)

