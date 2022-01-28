import monkdata as m
import dtree as d

t1 = d.buildTree(m.monk1, m.attributes)
t2 = d.buildTree(m.monk2, m.attributes)
t3 = d.buildTree(m.monk3, m.attributes)

condition = False

while not condition:
    p1 = d.allPruned(t1)
    p1check = d.check(p1, m.monk1test)
    for tree in p1:
        if p1check < d.check(tree, m.monk1test):  #fortsätt här :)
            p1check = d.check(tree, m.monk1test)
            p1 = tree

    p2 = d.allPruned(t2)

    p3 = d.allPruned(t3)
