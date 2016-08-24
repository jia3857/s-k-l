def show_desktop():
     click(Pattern("1471937352697.png").targetOffset(5,12))
def launch_rocket_bot():
    while not exists("1472013829687.png"):
        click(Pattern("1471937352697.png").targetOffset(5,12))

    doubleClick("1471937225910.png")
    for x in xrange(1,10):
        try:
            sleep(1)
            wait("1471937569324.png") 
        except:
            pass

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
        is_bot_dead_null_ref()
        ret = True
    return ret

def is_bot_dead_null_ref():
    danger=0
    for x in xrange(1, 3):
        if exists("1471940335321.png"):
            danger+=1
        sleep(5)
    if danger > 5:
       terminate_bot(danger)
            
def terminate_bot(danger):
    print("terminate_bot ... %s" %(danger))
    show_desktop()
    close_prog()
    
def main():
    import time, datetime
    max_retry = 60*6 # 60 minutes

    show_desktop()
    launch_rocket_bot()
    click_start()
  
    for x in xrange(1, max_retry):
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        if is_bot_dead():
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
            main()
        except Exception, err:
            print("EXCEPTION: %s -- err: %s" %(Exception, err))