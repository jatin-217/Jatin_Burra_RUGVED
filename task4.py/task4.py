import matplotlib.pyplot as plt
import numpy as np

class Robot:
    def __init__(self, dt=0.05):
        # Initial pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0  # radians
        self.dt = dt
        self.trajectory = [(self.x, self.y, self.theta)]

    def execute_velocity_command(self, v, omega, duration):
        initial_pose = (self.x, self.y, self.theta)
        steps = int(duration / self.dt)

        for _ in range(steps):
            # Forward Euler integration
            self.x += v * np.cos(self.theta) * self.dt
            self.y += v * np.sin(self.theta) * self.dt
            self.theta += omega * self.dt
            self.trajectory.append((self.x, self.y, self.theta))

        final_pose = (self.x, self.y, self.theta)
        print(f"Initial Pos: {initial_pose} | Executing: v={v}, ω={omega}, duration={duration} | Final Pos: {final_pose}")

    def plot_trajectory(self):
        xs = [p[0] for p in self.trajectory]
        ys = [p[1] for p in self.trajectory]
        thetas = [p[2] for p in self.trajectory]

        plt.figure(figsize=(8, 8))
        plt.plot(xs, ys, 'b-', label="Trajectory")
        plt.scatter(xs[0], ys[0], c='green', marker='o', label="Start")
        plt.scatter(xs[-1], ys[-1], c='red', marker='x', label="End")

        # Orientation arrows (sampled to reduce clutter)
        skip = max(1, len(xs)//25)
        dx = np.cos(thetas[::skip])
        dy = np.sin(thetas[::skip])
        plt.quiver(xs[::skip], ys[::skip], dx, dy, angles='xy', scale_units='xy', scale=5, color='orange')

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Continuous Unicycle Model Trajectory")
        plt.legend()
        plt.axis("equal")
        plt.grid(True)
        plt.show()


# Example usage
if __name__ == "__main__":
    robot = Robot(dt=0.05)

    # Commands: (linear velocity v, angular velocity ω, duration)
    commands = [
        (1.0, 0.0, 5.0),       # straight line
        (1.0, np.pi/8, 5.0),   # gentle left curve
        (1.0, -np.pi/6, 4.0),  # sharper right curve
        (0.5, 0.0, 3.0)        # slower straight
    ]

    for v, omega, duration in commands:
        robot.execute_velocity_command(v, omega, duration)

    robot.plot_trajectory()


