import monkdata as m
import dtree as d
import drawtree_qt5 as dqt

t = d.buildTree(m.monk1, m.attributes)
t2 = d.buildTree(m.monk2, m.attributes)
t3 = d.buildTree(m.monk3, m.attributes)
#print(d.check(t, m.monk1test))
#print(type(t))

#dqt.drawTree(t)
#dqt.drawTreet(t2)
#dqt.drawTree(t3)

print(1)
print("test")
print(d.check(t, m.monk1test))
print("vanlig")
print(d.check(t, m.monk1))

print(2)
print("test")
print(d.check(t2, m.monk2test))
print("vanlig")
print(d.check(t2, m.monk2))

print(3)
print("test")
print(d.check(t3, m.monk3test))
print("vanlig")
print(d.check(t3, m.monk3))
