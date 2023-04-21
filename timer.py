from time import sleep
from threading import Thread

# print('3秒後に星が出ます。')
# # sleep()は与えられた秒数の間、プログラム（正確にはスレッド）の実行を停止する。引数には秒を取る
# sleep(3)
# print('ミ☆ミ☆ミ☆')


target_time = 10

def up_timer(secs):
    # for文は指定回数まで繰り返す
    # range()で回数分実行する。今回は0~secs回まで
    # 1秒待機する
    for i in range(0,secs):
        print(i)
        sleep(1)
    # 指定時間後に"時間です！"と表示する
    print('カウントアップ終了！')

# up_timer(target_time)

# ★カウントダウン型の場合

def down_timer(secs):
    # range()で回数分実行する。今回は0~secs回まで
    # カウントダウンの場合は、secs~第2引数まで。第3引数ずつ引く
    # 今回は0まで表示したいので、第2引数は-1に指定
    for i in range(secs,-1,-1):
        print(i)
        sleep(1)
    # 指定時間後に"時間です！"と表示する
    print('カウントダウン終了！')

# down_timer(target_time)

# ★同時起動させる

# Threadインスタンスをタイマーごとに生成する
thread_1 = Thread(target=up_timer,args=(target_time,))
thread_2 = Thread(target=down_timer,args=(target_time,))

thread_1.start()
thread_2.start()