def add(n1, n2, cb):
    cb(n1+n2)

def handle1(result):
    print("結果是: ", result)

def handle2(result):
    print("Result of Add is: ", result)

add(3, 4, handle1)
add(5, 6, handle1)
add(4, 2, handle2)
