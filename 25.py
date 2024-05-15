import matplotlib.pyplot as plt

X=["karthik","naveen","moses"]
Y=[70,72,80,]

plt.title("student marks pie chart")

plt.pie(Y,labels=X,autopct='%d')

plt.show()
