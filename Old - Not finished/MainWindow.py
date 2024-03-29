from tkinter import Tk, Frame, Canvas
from Ball import Ball
from Obstacle import Obstacle


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Save the master window and change the title
        self.master = master
        self.master.title("Color Switch")

        # Set the frame to full the entire window
        self.pack(fill="both", expand=True)

        # Create the main canvas and add it to
        self.canvas = Canvas(self, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Create the ball and add it to the window
        self.obs = Obstacle(self.canvas)
        
        # Create the ball and add it to the window
        self.ball = Ball(self.canvas, self)

        # Start the check collision timer when the onload event is called
        self.canvas.bind("<Map>", self.checkCollision, add="+")

    def checkCollision(self, event=None):
        if self.obs.image is not None:
            self.obs.is_obstacle_collide_with_ball(self.ball)

        self.after(100, self.checkCollision)

    def move_obstacles(self, delta):
        self.obs.move_obstacle(delta)

# Create root window and create the main window and start the main loop
root = Tk()
root.geometry("500x500")

app = MainWindow(master=root)
app.mainloop()