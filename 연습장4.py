def merge(left, right):
    # 결과를 담을 빈 리스트 (0으로 채워둠)
    result = [0] * (len(left) + len(right))
    l = 0  # 왼쪽 팀의 화살표(인덱스)
    r = 0  # 오른쪽 팀의 화살표(인덱스)

    print(f"🏁 병합 시작! \n왼쪽 팀: {left} \n오른쪽 팀: {right}")
    print("-" * 30)

    # 두 팀 모두 비교할 사람이 남아있을 때까지 반복
    while l < len(left) and r < len(right):
        print(f"👀 현재 비교: 왼쪽 {left[l]} vs 오른쪽 {right[r]}")
        
        if left[l] < right[r]:
            print(f"   -> {left[l]}가 더 작네요! 결과 리스트에 추가.")
            result[l + r] = left[l]
            l += 1
        else:
            print(f"   -> {right[r]}가 더 작거나 같네요! 결과 리스트에 추가.")
            result[l + r] = right[r]
            r += 1
        print(f"   ✅ 현재까지 합쳐진 모습: {result}")

    # 한쪽 팀이 먼저 다 들어갔다면, 남은 팀 친구들을 그대로 뒤에 붙여줌
    while l < len(left):
        print(f"🏃 왼쪽 팀에 {left[l]}가 남았어요. 그대로 뒤에 붙입니다.")
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        print(f"🏃 오른쪽 팀에 {right[r]}가 남았어요. 그대로 뒤에 붙입니다.")
        result[l + r] = right[r]
        r += 1

    print("-" * 30)
    print(f"✨ 최종 합체 결과: {result}\n")
    return result

# 실행 예시 (이미 정렬된 두 팀이 만나는 상황)
team_a = [10, 69]
team_b = [2, 30]

final_team = merge(team_a, team_b)