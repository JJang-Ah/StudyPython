class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

    
if __name__ == "__main__": # 이쪽 파일에서 실행하면 이런거 호출
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()

else: #다른 파일에서 불러와서 실행되면 이거 호출
    print("Thailand 외부에서 모듛 호출")

