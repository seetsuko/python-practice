import random

# じゃんけん

def judge(x, y):
    score = (x - y + 3) % 3
    if score == 0:
        j = '引き分けです'
    elif score == 1:
        j = 'あなたの負けです'
    else:
        j = 'あなたの勝ちです'
    print(j)

hand = ['グー','チョキ','パー']

# プレイヤー
x = input('手を選んで下さい\n0:グー, 1:チョキ, 2:パー\n\n')

x = int(x)

# CPU
y = random.randint(0, 2)

# 双方の出した手を表示
print('\nあなたの手:{}'.format(hand[x]))
print('コンピュータの手:{}\n'.format(hand[y]))

judge(x, y)