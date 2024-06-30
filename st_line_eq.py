import matplotlib.pyplot as plt
import numpy as np

def plot_st_line():
    print("straight line equation of the form y = mx + c.")
    
    #user input
    try:
        m = float(input("Enter the slope (m) in radian: "))
        c = float(input("Enter the y-intercept (c): "))
    except ValueError:
        print("Invalid input, Please enter numerical values.")
        return
    
    print(f"The equation of the line is: y = {m}x + {c}")
    
    x = np.linspace(-10, 10, 200)
    y = m * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {m}x + {c}')

    plt.title('Straight Line graph')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xlabel('x')
    plt.xlabel('y')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_st_line()
    