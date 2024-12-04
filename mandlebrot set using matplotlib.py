import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, max_iter):
    # Create complex plane
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    # Calculate mandelbrot set
    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def plot_mandelbrot(width=1000, height=1000, max_iter=100):
    # Generate the Mandelbrot set
    mandel = mandelbrot(height, width, max_iter)
    
    # Create figure and plot
    plt.figure(figsize=(12, 12))
    
    # Plot with custom colormap
    plt.imshow(mandel, cmap='hot', extent=[-2, 0.8, -1.4, 1.4])
    plt.title(f"Mandelbrot Set (max iterations: {max_iter})")
    plt.colorbar(label='Iteration count')
    
    # Add labels
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    
    plt.show()

# Generate and display the visualization
plot_mandelbrot(width=1000, height=1000, max_iter=100)


