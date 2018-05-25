def func(s,l):
    ns = ""
    for i in range(l):
        if s[i] == ' ':
            ns+="%20"
        else:
            ns+=s[i]
    return ns