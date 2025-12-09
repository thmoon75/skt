while True:
    sentence = input("문장을 입력하세요 (종료하려면 EXIT 입력): ")

    # 사용자가 EXIT을 입력하면 반복 종료
    if sentence == "EXIT":
        print("프로그램을 종료합니다.")
        break

    # 입력한 문장을 그대로 출력
    print(sentence)
