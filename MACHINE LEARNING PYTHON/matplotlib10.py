import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels=["apples","bananas","strawberry","dates"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show() 
