# roulette_picker.py
import random
import time

def roulette(items):
    print("룰렛을 돌리는 중입니다...")
    time.sleep(2)  # 룰렛 효과를 위해 잠시 대기
    chosen_item = random.choice(items)
    print(f"선택된 항목은: {chosen_item}")
    return chosen_item

if __name__ == "__main__":
    print("룰렛에 추가할 항목을 입력하세요. 항목 추가를 완료하려면 빈 줄(Enter)을 입력하세요.")
    items = []
    while True:
        item = input("항목 입력: ")
        if item.strip() == "":
            break
        items.append(item)

    if not items:
        print("항목이 없습니다. 프로그램을 종료합니다.")
    else:
        roulette(items)

