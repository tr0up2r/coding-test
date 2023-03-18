# 손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수 구하기

N = 1260
coin_count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    coin_count += N // coin
    N %= coin

print(coin_count)