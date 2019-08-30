def guess_n(st, en, c):
    """
    It will take range and guess_count as parameters and performs binary search algorith to find the number"
    """
    m = (st + en) // 2  # middle number in range
    c += 1
    if en-1 == st+1:
        print("Your number is %s" % m )
        print("It took me %s guesses" % c)
        return c
    g = input("%s?" % (m))
    if g == "c":
        print("Your number is %s" % m )
        print("It took me %s guesses" % c)
        return c
    elif g == "h":
        en = m # moving range to (st,m)
    else:
        st = m # moving range to (m, en)
    return guess_n(st, en, c)


n = int(input("Please enter a number: "))
l = 1 # game count
t = 0 # total points

while True:
    t += guess_n(1, n, 0)
    print("I averaged %s guesses per game for %s game(s)" % (t/l, l))
    l += 1
    if input("Play again(y/n)?").lower() == "n":
        break
    
