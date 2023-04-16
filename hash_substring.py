def rabin(pattern, text):
    l = []
    v1, v2, d, q = 0, 0, 26, 11
    small = len(pattern)
    big = len(text)
    var = pow(d, small-1)%q
    for i in range(small):
        v1 = (d*v1 + ord(pattern[i]))%q
        v2 = (d*v2 + ord(text[i])) % q
    for i in range(big-small+1):
        if v1 == v2:
            if text[i:i+small] == pattern:
                l.append(i)
        if i < big-small:
            v2 = (d*(v2-ord(text[i])*var)+ord(text[i+small]))%q
    return(l)


def main():
    first_input = input()
    if first_input.__contains__('I'):
        pattern = input().rstrip()
        text = input().rstrip()
        assert len(pattern) <= len(text)
        arr = rabin(pattern, text)
        print(' '.join(map(str, arr)))
    elif first_input.__contains__('F'):
        file_name = input()
        if file_name.__contains__('a'):
            print("INPUT-OUTPUT ERROR")
            return
        with open("./tests/" + file_name) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            assert len(pattern) <= len(text)
            arr = rabin(pattern, text)
            print(' '.join(map(str, arr)))
    else:
        print("INPUT-OUTPUT ERROR")
        return


main()
