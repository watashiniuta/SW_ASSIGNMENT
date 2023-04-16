학점 = {
    'A+' : 4.5, 
    'A' : 4.0, 
    'B+' : 3.5, 
    'B' : 3.0, 
    'C+' : 2.5, 
    'C' : 2.0, 
    'D+' : 1.5, 
    'D' : 1.0, 
    'F' : 0.0
    }

과목 = dict({})

수강목록 = []

number = 1
number2 = 0
def work():
    과목명 = input('과목명을 입력하세요:')
    학점1 = int(input('학점을 입력하세요:'))
    평점1 = input('평점을 입력하세요:')

    과목['%d'%number] = 과목명
    수강목록.append((과목['%d'%number], 학점1, 평점1))
    
    print("입력되었습니다.")
    return

def calculate():
    
    summation_value = 0
    F학점수 = 0
    제출용학점 = 0
    열람용학점=  0

    for i, j, k in 수강목록:
        summation_value += j * 학점['%s'%k]
        열람용학점 += j
        if '%s'%k == 'F':
            F학점수 += j

    제출용학점 = 열람용학점 - F학점수

    print('제출용: {}학점 (GPA: {:.2f})'.format(제출용학점, summation_value/제출용학점))
    print('열람용: {}학점 (GPA: {:.2f})'.format(열람용학점, summation_value/열람용학점))
    return

def display():
    for i in 수강목록:
        print("[%s] %d학점: %s"%('%s'%i[0], i[1], i[2]))

def main():
    value = 0 #변수 선언후 초기화
    running = True
    while running:
        print("\n작업을 선택하세요.")
        print("1. 입력")
        print("2. 계산")
        print("3. 출력")

        value = int(input('해당 번호 입력:'))

        if value == 1:
            work()
        elif value == 2:
            calculate()
            running = False
        elif value == 3:
            display()

if __name__ == '__main__': #메인함수 실행
    main()