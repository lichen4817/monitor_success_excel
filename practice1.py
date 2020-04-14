def circle_area(r):
    result_area=3.1415926*r**2
    return result_area
print(circle_area(2))

list = [1,1,1,6,6,7,3,9]
a = {}
for i in list:
  if list.count(i)>0:
    a[i] = list.count(i)  #a[i]是字典value的值

print (a)