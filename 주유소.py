'''

의사 코드

distance = [2, 3, 1]
station = [5, 2, 4, 1]

temp_dict = int, 현 시점에서 곱해질 거리
answer = 총 비용
min_num = 현 시점에서 최소 비용

for i in range(1, N):
    # 마지막 station을 체크하고 현재 저장되어있는 값으로 비용 계산해서 추가
    if i == N-1:
        temp_dict += distance[i-1]
        answer += temp_dict * min_num
        break
    현재 station의 비용이 min_num보다 크면
    if min_num < station[i]:
        temp_dict += distance[i-1] 거리만 더해주기
    else: 현재 비용이 새로운 min_num이라면
        temp_dict += distance[i-1]
        answer += temp_dict * min_num # 현재까지 저장해놓은 거리랑 기존의 min_num을 answer에 넣고
        min_num = station[i] # 최소비용 갱신
        tmep_dict = 0 # 현시점에서 거리 0

'''

N = int(input())
distance = list(map(int, input().split()))
station = list(map(int, input().split()))

temp_dict = 0
answer = 0
min_num = station[0]

for i in range(1, N):
    # 마지막 station을 체크하고 현재 저장되어있는 값으로 비용 계산해서 추가
    if i == N-1:
        temp_dict += distance[i-1]
        answer += temp_dict * min_num
        break
    # 현재 station의 비용이 min_num보다 크면
    if min_num < station[i]:
        temp_dict += distance[i-1]
    else: #현재 비용이 새로운 min_num이라면
        temp_dict += distance[i-1]
        answer += temp_dict * min_num # 현재까지 저장해놓은 거리랑 기존의 min_num을 answer에 넣고
        min_num = station[i] # 최소비용 갱신
        temp_dict = 0 # 현시점에서 거리 0
print(answer)