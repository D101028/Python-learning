data = input(">>>")
try:
    number=int(data)
except Exception:
    number = 0

number=number*2
print(number)