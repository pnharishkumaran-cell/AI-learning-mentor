import time 
import sys

def loading(message="Generating"):
    animation=["!","/","-","\\"]
    print()

    for i in range(120):
        sys.stdout.write(f"\r🤖{message}{animation[i%4]}🤖")
        sys.stdout.flush()
        time.sleep(0.1)

    