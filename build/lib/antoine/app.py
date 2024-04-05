import time
import sys

def construct_rectangle(width, height, email, personal_text):
    # Construct the rectangle bit by bit
    rectangle_code = ""
    for i in range(height):
        if i == 0:
            top_line = "╔" + "═" * (width - 2) + "╗\n"
            rectangle_code += top_line
            print(top_line, end="")
        elif i == height // 2:
            middle_line = "║" + email.center(width - 2) + "║\n"
            rectangle_code += middle_line
            print(middle_line, end="")
        elif i == height - 1:
            bottom_line = "╚" + "═" * (width - 2) + "╝\n"
            rectangle_code += bottom_line
            print(bottom_line, end="")
        else:
            line = "║" + " " * (width - 2) + "║\n"
            rectangle_code += line
            print(line, end="")
        time.sleep(0.5)  # Delay for 0.5 seconds

    # Delay before revealing personal text
    time.sleep(0.5)

    # Reveal the personal text bit by bit
    for line in personal_text.split('\n'):
        revealed_text = ""
        for char in line:
            revealed_text += char
            sys.stdout.write("\r" + revealed_text)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the speed of revealing text
        print()  # Print a newline after fully revealing a line

def main():
    email = "https://www.linkedin.com/in/antoinebertin35/"
    width = 60
    height = 10
    personal_text = """
    Hey there! 👋 Antoine 2.3 here. 
    Sold my restaurant after 12 years and jumped into coding for about the same time. 
    Recently graduated from the top data scientist BootCamp in Europe! 🎓 
    There, I honed my skills in crafting, deploying, and monitoring ML/deep learning models. 
    I'm a computer tinkerer who enjoys slapping on 6 GPUs for fun, securing blockchain networks, 
    and crafting apps leveraging vector databases to help my lawyer friends with the civil code.
    Data's my jam, and I'm passionate about wine, blockchain, gymnastics, and kitesurfing. 
    On the lookout for a company 🕵️ that needs a reliable ally to grow their business. 
    Ready to settle down and build a long-term career while making meaningful contributions.
    If you dont hire me, your computer will explode in:
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Boom!
    """
    construct_rectangle(width, height, email, personal_text)

main()
