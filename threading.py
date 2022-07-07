from threading import Thread

def threaded_function():
        print("hello word")


if __name__ == "__main__":
    thread = Thread(target = threaded_function)
    thread.start()
    thread.join()
    print("thread finished...exiting")