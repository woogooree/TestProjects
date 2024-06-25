from collections import deque

callInfo = {
    '고장': 3,
    '사용': 9,
    '환불': 4,
    '기타': 1
}

MAX_QUEUE_SIZE = 10
queue = deque(maxlen=MAX_QUEUE_SIZE)


def calculate_wait_time(calls):
    wait_times = []
    time = 0
    
    for call in calls:
        subject, duration = call
        time += callInfo[subject]
        wait_times.append(time)
        queue.append(call)
    
    return wait_times

calls = [
    ('사용', 9),
    ('고장', 3),
    ('환불', 4),
    ('환불', 4),
    ('고장', 3)
]


wait_times = calculate_wait_time(calls)


for i, time in enumerate(wait_times):
    print("귀하의 대기 예상시간은 ", end='')
    print(f"{time} 분입니다.")
    print(f"현재 대기 콜 --> {list(queue)}")


# 다 검색함
