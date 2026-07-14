import time
def type_text(text,delay=0.005):
    for char in text:
        print(char,end="",flush=True)
        time.sleep(delay)
    print()