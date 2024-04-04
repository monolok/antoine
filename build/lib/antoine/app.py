import time

def construct_rectangle(width, height, email):
    rectangle_code = ""

    # Construct the top line of the rectangle
    top_line = "╔" + "═" * (width - 2) + "╗\n"
    rectangle_code += top_line
    print(top_line, end="")
    time.sleep(0.5)  # Delay for 0.5 seconds

    # Construct the middle part of the rectangle
    for _ in range((height - 3) // 2):
        middle_part = "║" + " " * (width - 2) + "║\n"
        rectangle_code += middle_part
        print(middle_part, end="")
        time.sleep(0.5)  # Delay for 0.5 seconds
    
    # Construct the middle line with the email
    middle_line = "║" + email.center(width - 2) + "║\n"
    rectangle_code += middle_line
    print(middle_line, end="")
    time.sleep(0.5)  # Delay for 0.5 seconds

    # Construct the bottom part of the rectangle
    for _ in range((height - 2) // 2):
        bottom_part = "║" + " " * (width - 2) + "║\n"
        rectangle_code += bottom_part
        print(bottom_part, end="")
        time.sleep(0.5)  # Delay for 0.5 seconds
    
    # Construct the bottom line of the rectangle
    bottom_line = "╚" + "═" * (width - 2) + "╝\n"
    rectangle_code += bottom_line
    print(bottom_line, end="")
    time.sleep(0.5)  # Delay for 0.5 seconds

    return rectangle_code

def main():
    email = "https://www.linkedin.com/in/antoinebertin35/"
    width = 60
    height = 10
    construct_rectangle(width, height, email)