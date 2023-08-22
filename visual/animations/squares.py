import matplotlib.animation as a
import matplotlib.pyplot as plt


boxes = []
fig, ax = plt.subplots()

def init():
    boxes.append({"x": [-1, 1, 1, -1, -1], "y": [1, 1, -1, -1, 1]})
    boxes.append({"x": [-2, 2, 2, -2, -2], "y": [-2, -2, 2, 2, -2]})
    boxes.append({"x": [-4, 4, 4, -4, -4], "y": [4, 4, -4, -4, 4]})

def animate(f):
    ax.cla()
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.plot(boxes[f%3]["x"], boxes[f%3]["y"], "b^-")

def run():
    garry = a.FuncAnimation(fig, animate, frames=500, interval=1000, init_func=init)
    plt.show()

run()
