
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

fig, ax = plt.subplots()
ax.plot(x, B, marker='', color='blue', linewidth=4,
        linestyle='solid', label="Benefit")
ax.plot(x, C, marker='', color='red', linewidth=4,
        linestyle='solid', label="Cost")
ax.set_xlabel('Pollution abatement (thousand tons)')
ax.set_ylabel('Values (in millions of dollars per year)')
ax.set_title("Benefit & Cost ")
ax.legend()
plt.show()

x = np.arange(0, 15, 1)
B = 60 * x - 3 * x ** 2
C = 10 * x + 2 * x ** 2
MB = 60 - 6 * x
MC = 10 * 4 * x

# Stacking subplots in one direction
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
plt.setp(axs, xticks=np.arange(0, 15, 1), yticks=np.arange(0, 400, 50),
         xlim=(0, 15), ylim=(0, 400))
axs[0].plot(x, B, marker='', color='blue', linewidth=4,
            linestyle='solid', label="Benefit")
axs[0].plot(x, C, marker='', color='red', linewidth=4,
            linestyle='solid', label="Cost")
axs[1].plot(x, MB, marker='', color='xkcd:ocre', linewidth=4,
            linestyle='solid', label="Marginal Benefit")
axs[1].plot(x, MC, marker='', color='violet', linewidth=4,
            linestyle='solid', label="Marginal Cost")
fig.legend(loc="right", borderaxespad=0.1, title="Legend")
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.7)
plt.show()

# To obtain side-by-side subplots, pass parameters 1, 2 for one row and two columns.
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
plt.setp(axs, xticks=np.arange(0, 15, 1), yticks=np.arange(0, 400, 50),
         xlim=(0, 15), ylim=(0, 400))
(ax1, ax2) = axs
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x, B, marker='', color='blue', linewidth=4,
         linestyle='solid', label="Benefit")
ax1.plot(x, C, marker='', color='red', linewidth=4,
         linestyle='solid', label="Cost")
ax2.plot(x, MB, marker='', color='xkcd:ocre', linewidth=4,
         linestyle='solid', label="Marginal Benefit")
ax2.plot(x, MC, marker='', color='violet', linewidth=4,
         linestyle='solid', label="Marginal Cost")
ax1.legend()
ax2.legend()
#fig.legend(loc="right", borderaxespad=0.1, title="Legend")
#plt.subplots_adjust(left=0.1, bottom=0.1, right=0.7)
plt.show()

fig, axs = plt.subplots(2, 2, sharex='col', sharey='row',
                        gridspec_kw={'hspace': 0, 'wspace': 0})
(ax1, ax2), (ax3, ax4) = axs
fig.subtitle('Sharing x per column, y per row')
ax1.plot(x, B)
ax2.plot(x, C, 'tab:orange')
ax3.plot(x, MB, 'tab:green')
ax4.plot(x, MC, 'tab:red')
plt.show()
