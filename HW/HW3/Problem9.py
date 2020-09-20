
def Hanoi(n, left, middle, right):
    if n >= 1:
        Hanoi(n-1, left, right, middle)
        move(n, left, right)
        Hanoi(n-1, middle, left, right)

def move(x, pole1, pole2):
    print("Move ", x, " from", pole1, " to ", pole2)

Hanoi(3,"left", "middle", "right")
