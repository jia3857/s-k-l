def show_desktop():
     click(Pattern("1471937352697.png").targetOffset(5,12))
def launch_rocket_bot():
    while not exists("1472013829687.png"):
        click(Pattern("1471937352697.png").targetOffset(5,12))

    doubleClick("1471937225910.png")

    wait("1471937569324.png") 

def click_start():
    click("1471937975654.png")
    
def close_prog():
    if exists(Pattern("1471938037425.png").targetOffset(39,-21)):
        click(Pattern("1471938037425.png").targetOffset(39,-21))

def is_bot_dead():
    ret = False
    if exists("1471938545940.png"):
        ret = True
    elif exists("1471940335321.png"):
        detect_bot_dead_null_ref_repeated()
        ret = True
    return ret

def detect_bot_dead_null_ref_repeated():
    danger=0
    for x in xrange(1, 6):
        if exists("1471940335321.png"):
            danger+=1
        sleep(1)
    if danger >= 3:
       terminate_bot(danger)
            
def terminate_bot(danger):
    print("terminate_bot ... 'see Null Reference' %s times" %(danger))
    show_desktop()
    close_prog()
    
def play_n_minutes(N=30):
    import time, datetime
    max_retry = N*6 # 60 minutes
    time_start = time.time()
    time_end = time_start + 60*60
    show_desktop()
    launch_rocket_bot()
    click_start()
  
    for x in xrange(1, max_retry):
        if time.time() > time_end:
            print("played %s minutes" %(N))
            exit(0)
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if is_bot_dead():
            raise Exception("bot is dead... restart")
            close_prog()
            launch_rocket_bot()
            click_start()
        else:
            print("[%s] had checked %s out of %s" %(st, x, max_retry))
            sleep(10)
            pass
    print("finished")
    close_prog()

if __name__ == "__main__":
    params = {}
    interation = params.get("iteration", 10)
    for i in xrange(1, interation):
        try:
            play_n_minutes(N=60)
        except Exception, err:
            print("EXCEPTION: %s -- err: %s" %(Exception, err))