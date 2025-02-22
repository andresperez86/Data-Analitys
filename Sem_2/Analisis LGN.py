# Re-run the necessary imports and code after execution state reset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set random seed for reproducibility
np.random.seed(42)

# Define parameters for the exponential distribution
lambda_param = 1  # Rate parameter
true_mean = 1 / lambda_param  # Theoretical mean of the exponential distribution

# Number of samples to simulate
n_samples = 3000
sample_sizes = np.arange(1, n_samples + 1)

# Generate i.i.d. exponential random variables
samples = np.random.exponential(scale=true_mean, size=n_samples)

# Compute the cumulative mean for each sample size
cumulative_means = np.cumsum(samples) / sample_sizes

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(1, n_samples)
ax.set_ylim(0, 2)
ax.set_xlabel("Número de muestras (n)")
ax.set_ylabel("Media muestral")
ax.set_title("Ley de los Grandes Números (LLN)")
ax.axhline(true_mean, color='red', linestyle='dashed', label=f"Media teórica = {true_mean:.2f}")
line, = ax.plot([], [], lw=2, label="Media muestral")

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def update(frame):
    line.set_data(sample_sizes[:frame], cumulative_means[:frame])
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(sample_sizes), init_func=init, blit=True, interval=1)

# Save as GIF
gif_path = "/mnt/data/LLN_animation.gif"
ani.save(gif_path, writer='pillow', fps=30)

# Display the generated GIF path
gif_path
