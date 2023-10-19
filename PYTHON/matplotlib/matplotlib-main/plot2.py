#Default X-Points
#If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

#So, if we take the same example as above, and leave out the x-points, the diagram will look like this:


#Plotting without x-points:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()