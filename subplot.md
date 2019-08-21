## To create a single plot

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 15, 1)
B = 60 * x - 3 * x ** 2
C = 10 * x + 2 * x ** 2

plt.plot(x, B, marker='', color='blue', linewidth=4,
         linestyle='solid', label="Benefit")
plt.plot(x, C, marker='', color='red', linewidth=4,
         linestyle='solid', label="Cost")
# Set the limits of x,y axis
plt.xlim(0, 15)
plt.ylim(0, 400)
# Add the lables for x, y axis and plot title
plt.xlabel('Pollution abatement (thousand tons)')
plt.ylabel('Values (in millions of dollars per year)')
plt.title('Benefit & Cost')
# Display the legend
plt.legend()
```

![1566344555552](C:\Users\langzx\AppData\Roaming\Typora\typora-user-images\1566344555552.png)



An alternative way is to use plt.subplot

```python
fig, ax = plt.subplots()
ax.plot(x, B, marker='', color='blue', linewidth=4, linestyle = 'solid', label="Benefit")
ax.plot(x, C, marker='', color='red', linewidth=4, linestyle='solid', label="Cost")
ax.set_xlabel('Pollution abatement (thousand tons)')
ax.set_ylabel('Values (in millions of dollars per year)')
ax.set_title("Benefit & Cost ")
ax.legend()
plt.show()

```

![1566344570430](C:\Users\langzx\AppData\Roaming\Typora\typora-user-images\1566344570430.png)





## Creating multiple subplots using plt.subplot

Original tutorials from [Matplotlib](https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html)

### 