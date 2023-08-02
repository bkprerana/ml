import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["strawbery","cherry","banana","dates"]
mycolors=["red", "black", "m", "violet"]
plt.pie(y,labels=mylabels,colors=mycolors)
plt.legend(title="four fruits:" )
plt.show()
