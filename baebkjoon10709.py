'''

'''


print("온도를 입력하세요")
'''
파이썬은 모든 입력값을 문자로 인식하기 때문에, 숫자형으로 바꿔주셔야 해요.
대표적인 함수로를 int()나 float()가 있어요

반대로 숫자형을 문자형으로 바꿔주는 것은 string() 이 있어요
'''
f = float(input())

c = (5/9) * (f -32)


'''
위랑 아래를 비교하시면, 숫자도 조금 바꿔보면서 소수점 포맷팅을 이해해보세요.
'''

print('f : %0.1f // c: %0.1f'%(f, c))
print('f : %f // c: %f'%(f, c))