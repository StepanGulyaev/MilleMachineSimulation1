def end_of_string(string,i):
    if (i >= len(string)):
        return True
    else:
        return False


A_id = []
A_cel = []

def S0(string, i):
    global A_id
    global A_cel
    A_id.clear()
    A_cel.clear()
    S1(string,i)

def S1(string,i):
    global A_id
    global A_cel

    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S7(string, i)

    elif string[i] == '0':
        S1(string, i)

    elif string[i].isdigit():
        S2(string, i)

    else:
        S0(string, i)


def S2(string,i):
    global A_id
    global A_cel

    A_cel.append(string[i])
    i+=1

    if end_of_string(string,i):
        S5(string, i)
        return

    elif string[i].isalpha():
        S17(string, i)

    elif string[i].isdigit():
        S2(string, i)

    else:
        S3(string, i)



def S3(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S4(string,i)
    else:
        S0(string, i)


def S4(string,i):
    global A_id
    global A_cel

    print(''.join(map(str, A_cel)), end=' ')

    S0(string, i)

def S5(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S6(string,i)
    else:
        return

def S6(string,i):
    global A_id
    global A_cel

    print(''.join(map(str, A_cel)), end=' ')

def S7(string,i):
    global A_id
    global A_cel

    A_id.append(string[i])
    i += 1

    if end_of_string(string,i):
        S10(string, i)
        return

    elif string[i].isalpha():
        S7(string, i)

    elif string[i] == '0':
        S7(string, i)

    elif string[i].isdigit():
        S8(string, i)

    else:
        S9(string, i)



def S8(string, i):
    global A_id
    global A_cel

    A_cel.append(string[i])
    A_id.append(string[i])
    i += 1

    if end_of_string(string, i):
        S13(string, i)
        return

    elif string[i].isalpha():
        S15(string, i)

    elif string[i] == '0':
        S8(string, i)

    elif string[i].isdigit():
        S8(string, i)

    else:
        S11(string, i)

def S9(string, i):
    global A_id
    global A_cel

    print(''.join(map(str, A_id)), end=' ')

    S0(string, i)

def S10(string, i):
    global A_id
    global A_cel

    print(''.join(map(str, A_id)), end=' ')

def S11(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S12(string,i)
    else:
        S9(string, i)

def S12(string,i):
    global A_id
    global A_cel

    print(''.join(map(str, A_id)), end=' ')
    print(''.join(map(str, A_cel)), end=' ')
    S0(string, i)

def S13(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S14(string,i)
    else:
        S10(string, i)

def S14(string,i):
    global A_id
    global A_cel

    print(''.join(map(str, A_id)), end=' ')
    print(''.join(map(str, A_cel)), end=' ')

def S15(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S16(string,i)
    else:
        S18(string, i)

def S16(string,i):
    global A_id
    global A_cel

    print(''.join(map(str, A_cel)), end=' ')
    A_cel.clear()
    S7(string, i)

def S17(string,i):
    global A_id
    global A_cel

    if (int(''.join(map(str, A_cel))) % 2 != 0 ):
        S16(string,i)
    else:
        S18(string, i)

def S18(string,i):
    global A_id
    global A_cel

    A_cel.clear()
    S7(string,i)








