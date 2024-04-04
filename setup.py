from setuptools import setup
import time

setup(
    name='antoine',
    version='0.1',
    packages=['antoine'],  # 'antoine' is the name of the package
    entry_points={
        'console_scripts': [
            'antoine=antoine.app:main',  # 'antoine' is the name of the package and 'app.py' contains a function 'main'
        ],
    },
    include_package_data=True,
    install_requires=[],
)

# Print a message after installation
print("Antoine is successfully installed!")
print("lets goooo !")
print("antoine is a good boy")

def draw_blinking_rectangle(width, height, email):
    while True:
        # Print rectangle with email in the middle
        print("╔" + "═" * (width - 2) + "╗")
        for _ in range((height - 3) // 2):
            print("║" + " " * (width - 2) + "║")
        middle_line = "║" + email.center(width - 2) + "║"
        print(middle_line)
        for _ in range((height - 2) // 2):
            print("║" + " " * (width - 2) + "║")
        print("╚" + "═" * (width - 2) + "╝")
        
        # Sleep for 0.5 seconds
        time.sleep(0.5)
        
        # Clear the screen
        print("\033[H\033[J", end="")
        
        # Sleep for 0.5 seconds
        time.sleep(0.5)

# Example usage
email = "your_email@example.com"
draw_blinking_rectangle(30, 10, email)
