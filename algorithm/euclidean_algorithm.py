a, b = int(input('Введіть перше число: ')), int(input('Введіть друге число: ')) 
aa, bb = a, b
while a != b:
    if a > b: a = a - b 
    else: b = b - a            
print(f"НСД({aa}, {bb}) = {a}")
input()