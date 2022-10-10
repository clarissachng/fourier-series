#Task 1
 
import numpy as np
import matplotlib.pyplot as plt

# n = fourier series terms
# numpy array x for x values [-5:5]
# return numpy array f(x) or y

def Coefficient (n,x):
  # tuple that has only 0s
  y = np.zeros(len(x)) # depending on how we represent the graph
  
  for i in range(1,2*n, 2):
    y = y + np.sin(i*x)/i 

  return y

# Task 2
# plotting 4 figures subplots for n =1, n = 4, n = 20, n = 100
# use diff colours for each subplots, lable x and y axis
# [-pi, 0, pi]

# define x for the subplots 
x = np.arange(-5, 5, 0.1)

labels = ['-$\pi$', '0', '$\pi$'] 

# Creation of subplots
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1) 
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

y1 = Coefficient(1, x)     # n = 1
ax1.plot(x, y1, 'r', label ='n=1')
ax1.legend()
ax1.grid()
ax1.set_xticks([-3.14, 0, 3.14])
ax1.set_xticklabels(labels)
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("Fourier series with one term")

y2 = Coefficient(4, x)     # n = 4
ax2.plot(x, y2, 'b', label ='n=4')
ax2.legend()
ax2.grid()
ax2.set_xticks([-3.14, 0, 3.14])
ax2.set_xticklabels(labels)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_title("Fourier series with four terms")

y3 = Coefficient(20, x)    # n = 20
ax3.plot(x, y3, 'k', label ='n=20')
ax3.legend()
ax3.grid()
ax3.set_xticks([-3.14, 0, 3.14])
ax3.set_xticklabels(labels)
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_title("Fourier series with twenty terms")

y4 = Coefficient(100, x)   # n = 100
ax4.plot(x, y4, 'g', label ='n=100')
ax4.legend()
ax4.grid()
ax4.set_xticks([-3.14, 0, 3.14])
ax4.set_xticklabels(labels)
ax4.set_xlabel("X")
ax4.set_ylabel("Y")
ax4.set_title("Fourier series with hundred terms")

plt.tight_layout()
plt.show()

# Task 3
# Find the range = max-min

print('Range when x =1;' , str(np.amax(y1)-np.amin(y1)))
print('Range when x =4;' , str(np.amax(y2)-np.amin(y2)))
print('Range when x =20;' , str(np.amax(y3)-np.amin(y3)))
print('Range when x =100;' , str(np.amax(y4)-np.amin(y4)))