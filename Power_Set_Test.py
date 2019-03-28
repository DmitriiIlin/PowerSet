import Power_Set, unittest, random, string

def string_generator(size=10):
    chars=string.digits
    return ''.join(random.choice(chars) for _ in range(size))







if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()