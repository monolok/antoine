def construct_rectangle(width, height, email):
    rectangle_code = ""

    # Construct the top line of the rectangle
    rectangle_code += "╔" + "═" * (width - 2) + "╗\n"

    # Construct the middle part of the rectangle
    for _ in range((height - 3) // 2):
        rectangle_code += "║" + " " * (width - 2) + "║\n"
    middle_line = "║" + email.center(width - 2) + "║\n"
    rectangle_code += middle_line

    # Construct the bottom part of the rectangle
    for _ in range((height - 2) // 2):
        rectangle_code += "║" + " " * (width - 2) + "║\n"
    rectangle_code += "╚" + "═" * (width - 2) + "╝\n"

    return rectangle_code

def main():
    email = "https://www.linkedin.com/in/antoinebertin35/"
    width = 30
    height = 10
    rectangle_code = construct_rectangle(width, height, email)
    print(rectangle_code)