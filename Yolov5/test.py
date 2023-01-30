import sys

def getName (name, age):
    name = '이름은 {}이고, 나이는 {}입니다.'.format(name, age)
    return name

if __name__ == '__main__':
    getName(sys.argv[1], sys.argv[2])