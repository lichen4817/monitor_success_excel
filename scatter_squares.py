import matplotlib.pyplot as plt

x_values=list(range(1,50))
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,s=40,c=y_values,cmap=plt.cm.Blues)
plt.axis([0,50,0,2500])
plt.savefig('test_matploglib.png')