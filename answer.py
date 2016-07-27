def answer(p):
    with open('answer.txt', encoding='utf8') as fp:
        ss = fp.readlines()
    ss = ss[ss.index('#%s\n'%p):]
    ss = ss[:ss.index('\n')]
    print(''.join(ss))
