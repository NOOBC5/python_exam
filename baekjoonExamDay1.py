print("Hello World!") # 1차 Hello word

a, b = map(int, input().split()) # 2차 A + B
print(a + b)

a, b = map(int, input().split()) # 3차 A * B
print(a * b)

a, b = map(int, input().split()) # 4차 A - B
print(a - b)

a, b = map(int, input().split()) # 5차 A / B
print(a / b)

a,b = input().split() # 6차  사칙연산
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

A,B,C = map(int,input().split()) # 7차 나머지
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

a= int(input()) # 8차 A + B - 2
b= int(input())
print(a+b)