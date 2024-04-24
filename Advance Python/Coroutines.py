import time
def searcher():
    time.sleep(5)
    while True:
        text = (yield)
        if len(text) > 5:
            print(text)
            
        else:
            print("text is shorter")
            
search = searcher()
print(search,"starting coroutine now")
next(search)
search.send("maje lelo")
time.sleep(0.9)
search.send("lelo lelo")
time.sleep(0.9)
search.send("maje lelo")
time.sleep(0.9)
search.send("lelo lelo")
