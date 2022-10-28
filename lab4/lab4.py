# Character range function
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


def zap():
    mas = []
    mas.insert(0, " ")

    i = 1
    for character in range_char("a", "z"):
        mas.insert(i, character)
        i = i + 1

    for j in range(0, 10):
        mas.insert(i, j)
        i = i + 1

    mas.insert(i, ".")
    i = i + 1
    mas.insert(i, ",")
    i = i + 1
    mas.insert(i, "<")
    i = i + 1
    mas.insert(i, ">")
    i = i + 1
    mas.insert(i, "?")
    i = i + 1
    mas.insert(i, "'")
    i = i + 1
    mas.insert(i, ":")
    i = i + 1
    mas.insert(i, ";")
    i = i + 1
    mas.insert(i, "{")
    i = i + 1
    mas.insert(i, "}")
    i = i + 1
    mas.insert(i, "[")
    i = i + 1
    mas.insert(i, "]")
    i = i + 1
    mas.insert(i, "!")
    i = i + 1
    mas.insert(i, "@")
    i = i + 1
    mas.insert(i, "#")
    i = i + 1
    mas.insert(i, "№")
    i = i + 1
    mas.insert(i, "^")
    i = i + 1
    mas.insert(i, "&")
    i = i + 1
    return mas


def encrypt():
    # p = 5, q = 11,  n = p * q = 55,
    d = 3
    e = 27

    ABC = zap()

    # print(ABC)
    # print(len(ABC))
    print("Enter text =>", end=' ')

    line = input()
    line = line.lower()
    # print(line)
    result = []
    j = 0
    for char in line:
        for i in range(0, len(ABC)):
            if str(ABC[i]) == str(char):
                # print(char)
                result.insert(j, (i ** e) % 55)
                j = j + 1

    print(result)
    return q_exit()


def decipher():
    # p = 5, q = 11,  n = p * q = 55,
    d = 3
    e = 27

    ABC = zap()

    print("Enter code(through a space) =>")
    code = input()
    code = code
    mas = []
    j = 0
    for i in range(0, len(code) - 1):
        if code[i + 1] == ' ':
            if i == 0:
                mas.insert(j, int(f"{code[0]}"))
                j = j + 1
            elif i == 1:
                mas.insert(j, int(f"{code[0]}{code[1]}"))
                j = j + 1
            elif code[i - 2] == ' ':
                mas.insert(j, int(f"{code[i - 1]}{code[i]}"))
                j = j + 1
            elif code[i - 1]:
                mas.insert(j, int(f"{code[i]}"))
                j = j + 1
    if code[len(code) - 3] == ' ':
        mas.insert(j, int(f"{code[len(code) - 2]}{code[len(code) - 1]}"))
        j = j + 1
    if code[len(code) - 2] == ' ':
        mas.insert(j, int(f"{code[len(code) - 1]}"))
        j = j + 1
    # print(mas)
    result = []
    j = 0
    for record in mas:
        result.insert(j, ABC[((record ** d) % 55)])
        j = j + 1
    # print(result)
    transform_result = ""
    for record in result:
        transform_result = str(transform_result) + str(record)
    print(transform_result)
    return  q_exit()


def q_exit():
    print('Continue work with DB? Y/N =>', end=' ')
    while 1:
        c = input()
        if c == 'Y' or c == 'y':
            return 1
        elif c == 'N' or c == 'n':
            return 0
        else:
            print("The wrong value was entered, it will be entered again. Y/N =>", end=' ')


def main():
    flag = 1
    while flag:
        print("Select the action you want to perform:")
        print("1. Encrypt data")
        print("2. Decrypt the data")
        print("3. Exit")
        print("Make your choice =>", end=' ')

        num = input()
        num = int(num)
        if num == 1:
            flag = encrypt()
        if num == 2:
            flag = decipher()
        if num == 3:
            return 0



main()
