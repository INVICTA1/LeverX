from concurrent.futures import ThreadPoolExecutor


def function(a, arg):
    for _ in range(arg):
        a += 1
    return a


def main():
    a = 0
    with ThreadPoolExecutor(5) as executor:
        a = executor.submit(function, a=a, arg=5000000)
    print("----------------------", a.result())


main()
