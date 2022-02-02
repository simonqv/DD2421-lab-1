import random

import monkdata as m
import dtree as d


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

# monk1train, monk1val = partition(m.monk1, 0.6)
# 
# 
# t1 = d.buildTree(m.monk1, m.attributes)
# t2 = d.buildTree(m.monk2, m.attributes)
# t3 = d.buildTree(m.monk3, m.attributes)
# 
# condition = False
# 
# while not condition:
#     p1 = d.allPruned(t1)
#     p1check = d.check(p1, m.monk1test)
#     for tree in p1:
#         if p1check < d.check(tree, m.monk1test):  #fortsätt här :)
#             p1check = d.check(tree, m.monk1test)
#             p1 = tree
# 
# 
#     p2 = d.allPruned(t2)
# 
#     p3 = d.allPruned(t3)


def prune(tree, val_set):
    prev_best = tree
    while True:
        best_pruned = max(d.allPruned(prev_best), key=lambda t: d.check(t, val_set)) 
        if d.check(best_pruned, val_set) > d.check(prev_best, val_set):
            prev_best = best_pruned
        else:
            break
    return prev_best


if __name__ == '__main__':
    fractions = list(map(lambda i: i/10, range(3,9)))
    scores = []
    iterations = 100
    # tree = t1
    dataset = m.monk1
    testset = m.monk1test

    for frac in fractions:
        scores.append([])
        for i in range(iterations):
            train, val = partition(dataset, frac)
            tree = d.buildTree(train, m.attributes)
            tree = prune(tree, val)
            scores[-1].append(d.check(tree, testset))

    print(scores)
    print(list(map(lambda s: len(s), scores)))
    print(fractions)

