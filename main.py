from matplotlib.pyplot import plot, show, gca, xlim, ylim, Circle

def main():
   # Make it show a circle properly and remove background
   ax = gca()
   ax.axis("equal")
   xlim(-1, 1)
   ylim(-1, 1)
   ax.axis("off")

   # Add the background circle
   mainCircle = Circle((0, 0), 1)
   ax.add_patch(mainCircle)
   show()

if __name__ == "__main__":
   main()