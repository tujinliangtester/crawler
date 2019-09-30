import time




def t_clock():
    while True:
        s=time.asctime()
        print(s[11:19],end="")
        time.sleep(1)
        print("\r",end="",flush = True)

if __name__=='__main__':
    t_clock()