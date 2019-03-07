def generate_s(k):
    # Task A.1:
    #----------your code below----------#
    if k == 0:
        return "moo"
    os = "oo" + ("o" * k)
    return generate_s(k-1) + "m" + os + generate_s(k-1) # comment this line and write your solution

    #----------end of your code----------#
print(generate_s(2))


def find_k_check_N(N):
    # Task A.2: find k
    #----------your code below----------#
    k = 0
    moos = generate_s(k)
    while N > len(moos):
        k += 1
        moos = generate_s(k)
    #----------end of your code----------#
    # check N
    answer = generate_s(k)[N - 1]
    return k, answer


print(find_k_check_N(12))
if __name__ == '__main__':
    N = int(input())
    k, answer = find_k_check_N(N)
    print("According to n, the k is %d" % k)
    print("The nth character in it is '%c' " % answer)
