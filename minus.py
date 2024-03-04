def solution(num1,num2):
    if not (-50000 <= num1 <= 50000) or not (-50000 <= num2 <= 50000):
        print("범위 안의 수를 넣어주세요(-50000~50000)")
        exit()
    answer = num1 - num2
    return answer