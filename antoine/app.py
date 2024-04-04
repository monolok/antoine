import time

def draw_blinking_rectangle(width, height, email):
    for _ in range(10):  # Blink 5 times
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
        time.sleep(0.5)

def main():
    email = "your_email@example.com"
    draw_blinking_rectangle(30, 10, email)