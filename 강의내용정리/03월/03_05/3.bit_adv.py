# 상태를 나타내는 플래그 ( 각 상태가 하나의 비트를 활용)
WALK = 1 << 1
ATTACK = 1 << 2
JUMP = 1 << 3

Character_state = 0

# 상태 설정 함수
def set_state(state, flag):
    return state | flag