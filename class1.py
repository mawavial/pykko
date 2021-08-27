# exercise 1 - Loops
def loops():
    """Some loops"""
    if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            print(i ** 2)

    if __name__ == '__main__':
        n = int(input())
        for i in range(0, n):
            print(i ** 2)


# exercise 2 -  List Comprehensions
def list_comprehension():
    """Takes 4 parameteres"""
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if n != (a + b + c)]
    print(list)

def runner_up():
    """takes an array of numbers"""
    n = int(input())
    arr = map(int, [2,3,45,6])
    rr = list(arr)
    rr.sort()
    first = rr.pop()
    while 1:
        result = rr.pop()
        if result != first:
            print(result)
            break

def word_counter():
    """ Count words"""
    n = int(input())
    dict = {}
    li = []
    for i in range(n):
        word = input()
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
            li.append(word)
    print(len(li))
    for i in li:
        print(dict[i], end=' ')

