import time

def count_down(n):
    # 打印倒计时
    for x in range(n, -1, -1):
        mystr = "count down:" + str(x) + "s"
        print("\r倒计时%s" % mystr, end="")
        time.sleep(1)
def c2():
    for i in range(1,61):
        time.sleep(1)
        last_time = 60 - i
        print("\r倒计时%s秒开始，请稍等！" % last_time, end="")
if __name__=='__main__':
    count_down(10)
    # c2()