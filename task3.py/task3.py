import matplotlib.pyplot as plt
import numpy as np

class Robot:
    def __init__(self):
        self.x=0.000
        self.y=0.000
        self.theta=0.000
        self.trajectory=[(self.x, self.y, self.theta)]

    def execute_command(self,command):
        initial_pose=(self.x,self.y,self.theta)
        action,val=command.split()
        val=float(val)

        if action.lower()=="forward":
            self.x+=val*np.cos(self.theta)
            self.y+=val*np.sin(self.theta)
        elif action.lower()=="left":
            self.theta+=np.deg2rad(val)
        elif action.lower()=="right":
            self.theta-=np.deg2rad(val)
        else:
            print(f"Unknown command:{command}")
            return

        final_pose=(self.x,self.y,self.theta)
        self.trajectory.append(final_pose)

        print(f"Initial Pos:{initial_pose}|Executing: {command} | Final Pos:{final_pose}")

    def plot_trajectory(self):
        xs=[p[0] for p in self.trajectory]
        ys=[p[1] for p in self.trajectory]
        thetas=[p[2] for p in self.trajectory]

        plt.figure(figsize=(8,8))
        plt.plot(xs,ys,'b-',label="Trajectory")
        plt.scatter(xs[0],ys[0],c='green',marker='o',label="Start")
        plt.scatter(xs[-1],ys[-1],c='red',marker='x',label="End")

        dx=np.cos(thetas)
        dy=np.sin(thetas)
        plt.quiver(xs,ys,dx,dy,angles='xy',scale_units='xy',scale=5,color='orange')

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Discrete Motion Model Trajectory")
        plt.legend()
        plt.axis("equal")
        plt.grid(True)
        plt.show()

if __name__=="__main__":
    robot=Robot()
    commands=["forward 10", "left 90", "forward 5", "right 45", "forward 7"]

    for cmd in commands:
        robot.execute_command(cmd)

    robot.plot_trajectory()
