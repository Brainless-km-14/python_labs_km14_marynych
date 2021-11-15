
def cons(head,tail=[]):
    if len(tail) == 0:
        tail.append(head)
    else :
        tail.insert(0,head)
    return tail

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')
assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')