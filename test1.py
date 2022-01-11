a = (2, 3, 5, 9, 12, 14, 25)
b = (1, 4, 5, 7, 12, 21, 22, 23, 25, 27)

c_corr = [1, 2, 3, 4, 5, 7, 9, 12, 14, 21, 22, 23, 25, 27]
c = []
for i in range(len(a)):
    c.append(a[i])

k = 0

k_max = len(c)
for i, value in enumerate(b):
    while c[k] < value and k < k_max:
        k += 1
        ck_val = c[k]
    # end while
    if c[k] > value:
        c.append(value)
    # end if c[k] > value
    if a[k_max-1] < value:
        c.append(value)
    # end if a[k_max-1] < value:
# end for i, value in enumerate(cc_t1)
c.sort()
print("c = ", c)
print("c_= ", c_corr)
print("length c=", len(c), "length c_corr=", len(c_corr))

        #     equality = False
        # if value == c[k]:
        #     equality = True