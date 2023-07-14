# 계산기 프로그램

#계산기는 먼저 두 숫자를 입력받는다.
#그 뒤에 연산자를 입력받는다.   => 계산을 하지 않고 메세지를 출력
#결과를 출력

#주의할 점  : 나눗셈은 0으로 나누기가 불가능

# 한번 계산이 끝나고 또 계산을 할 수 있도록 반복문을 사용해서 만들어 보자

# 계산기를 끝내는 조건
# 두 숫자 모두 0을 입력하면 종료  

#반복문 while / for
#반복이 언제 끝날지 예상이 좀 어렵다 ==> while
#반복이 언제 끝날지 확실히 예상이 된다 ==> for(여러개가 들어있는 구조를 반복)

#계산기 반복 시작
#input() 으로 입력한 값은 모두 문자열로 취급
#int() 함수로 문자열을 숫자(정수)로 바꿈
print('-----------------')
while True:
    print()
    a = (input('a입력 : '))
    b = (input('b입력 : '))
    c = input('연산자 입력 : ')
    
    if a.isdigit() and b.isdigit():
        a=int(a)
        b=int(b)

        if a == b and a==0:
            break 

        if c == '+':
            print('a + b = ',a+b)
        elif c == '-':
            print('a - b = ',a-b)
        elif c == '*':
            print('a * b = ',a*b)
        elif c == '/':
            if b == 0:
                print('계산할 수 없습니다')
            else:
                print('a / b = ',a/b)
        elif c == '%':
            print('a % b = ',a%b)
        elif c == '//':
            print('a // b = ',a//b)
        else:
            print('인식할 수 없는 연산자입니다.')
    
    else:
        print('문자열이 아닙니다')

    


    #더 생각해 볼 수 있는 것들
    #글자를 계산할 수는 없다 ==> 사용자가 잘못 입력했을 경우 에러 처리
    #계산할  수 없는 연산자 입력 ...

