import time

def count_per_second():
    counter = 0
    try:
        while True:  # Zähle unbegrenzt
            time.sleep(1)
            counter += 1
            print("Counter:", counter)
    except KeyboardInterrupt:
        print("\nProgramm beendet.")
    return counter

if __name__ == "__main__":
    result = count_per_second()
    print("Final Counter Value:", result)