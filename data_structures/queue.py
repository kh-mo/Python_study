'''
FIFO(First In First Out)
'''

q = []
def add(item):
    q.append(item)

def remove():
    if len(q) != 0:
        item = q.pop(0)
        return item

def print_q():
    print("front -> ", end="")
    for i in q:
        print("{!s:<8}".format(i), end='')
    print(' <- rear')

if __name__ == "__main__":
    add('apple')
    add('orange')
    add('cherry')
    add('pear')
    print("사과, 오렌지, 체리, 배 삽입 후: \t", end="")
    print_q()
    remove()
    print("remove한 후:\t\t", end="")
    print_q()
    remove()
    print("remove한 후:\t\t", end="")
    print_q()
    add('graph')
    print("포도 삽입 후:\t\t",end="")
    print_q()