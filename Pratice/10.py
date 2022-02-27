#예외 처리


try:
        
    print("나누기 전용 계싼기 입니다.")
    nums = []
    
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))


    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: #숫자대신에 글넣으면 
    print("에러! 잘못된 값을 입력하셨습니다.")

except ZeroDivisionError as err: # 나누기를 0으로 하면
    print(err)
    
except Exception as err: #코드를 잘못짜면 나옴
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

