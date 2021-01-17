'''

의사코드

N = 보석 N개 4개
K = 가방 K개 3개

for 0-3:
    jewels = [ (2, 99), (1, 65), (5, 23), (4, 32) ]
for 0-2:
    bags = [[10, 0], [2, 0]]

jewels.sort(key=lambda x:x[1]) [ (4, 99, 0), (1, 65, 0), (2, 32, 0), (5, 23, 0) ] 가치 순으로 정렬
bags.sort 가방 무게로 정렬 [ [2, 0], [10, 0] ]
    bags를 for문 돌면서 -> 작은 가방부터 검사
        jewels도 for 돌면서
        만약 bags[i][0] >= jewels[j][0] 이고, jewel[j][2]가 0이라면,
            가지고 있는 값과 새로운 값 중 큰 값을 입력하고 jewel[j][2] = 1

    jewel[i][2]가 1인 보석의 가치의 합을 구하라

'''





N, K = map(int, input().split())
jewels = []
bags = []
for _ in range(N):
    jewels.append(list(map(int, input().split()))+[0])
max_weight = 0
for _ in range(K):
    temp = int(input())
    bags.append([temp, 0])
    if temp > max_weight:
        max_weight = temp


jewels.sort(key=lambda x:x[1], reverse=True)
bags.sort(key=lambda x:x[0])


for i in range(len(bags)):
    for j in range(len(jewels)):
        if bags[i][0] >= jewels[j][0] and jewels[j][2] == 0:
            bags[i][1] = jewels[j][1]
            jewels[j][2] = 1
            break

answer = 0
for i in range(K):
    answer += bags[i][1]
# print(jewels)
# print(bags)
print(answer)