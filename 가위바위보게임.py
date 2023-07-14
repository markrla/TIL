
## com = 컴퓨터가 낼 가위바위보중 하나 (할때마다 바뀐다)
#조건문을 사용해서 누가 이겼는지 판별한 후에 승자를 출력, 게임의 결과도 출력
import random

user = input("가위바위보 게임 시작 : ")
a= ['가위','바위','보']
com=random.choice(a)

print('내가 {}를 내고 컴퓨터가 {}를 내서'.format(user,com),end=' ')

if user == '가위':
    if com == '가위':
        print( '비겼습니다' )
    elif com == '바위':
        print( '졌습니다.' )
    else :
        print( '이겼습니다' )

elif user == '바위':
    if com == '가위':
        print( '이겼습니다' )
    elif com == '바위':
        print( '비겼습니다.' )
    else :
        print( '졌습니다' )

if user == '보':
    if com == '가위':
        print( '졌습니다' )
    elif com == '바위':
        print( '이겼습니다.' )
    else :
        print( '비겼습니다' )






