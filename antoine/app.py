import time
import sys

def construct_rectangle(width, height, email, personal_text_1, personal_text_boom, personal_text_2, personal_text_2_1, search, personal_text_finish):
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

    def reveal_text(text, delay):
        for line in text.split('\n'):
            revealed_text = ""
            for char in line:
                revealed_text += char
                sys.stdout.write("\r" + revealed_text)
                sys.stdout.flush()
                time.sleep(delay)
            print()

    reveal_text(personal_text_1, 0.05)
    reveal_text(personal_text_boom, 0.5)
    reveal_text(personal_text_2, 0.05)
    reveal_text(search, 0.5)
    reveal_text(personal_text_2_1, 0.05)
    reveal_text(search, 0.5)
    reveal_text(personal_text_finish, 0.05)

def main():
    email = "https://www.linkedin.com/in/antoinebertin35/"
    width = 60
    height = 10
    personal_text_1 = """
    Hey there! 👋 Antoine 2.5 here. 
    Sold my restaurant after 12 years and jumped into coding for about the same time. 
    I Recently graduated from the top data scientist school in Europe! 🎓 
    There, I honed my skills in crafting, deploying, and monitoring ML & deep learning models. 
    So If you dont hire me, your computer will explode in:"""
    personal_text_boom = "5 4 3"
    personal_text_2 = """
    Just Kidding, I would not dare.
    I'm a computer tinkerer who enjoys slapping on 6 GPUs for securing blockchain networks, 
    and making AI apps for fun to help my friends.
    Data's my jam, and I'm passionate about wine, blockchain, gymnastics, kitesurfing and """
    personal_text_2_1 = """okay, enough passions.
    I am on the lookout for a company 🕵️ searching 🕵️...."""
    search = "....." 
    personal_text_finish = """
    A company that needs a reliable ally to grow their business.
    I am ready to settle down and build a long-term career while making meaningful contributions."""

    construct_rectangle(width, height, email, personal_text_1, personal_text_boom, personal_text_2, personal_text_2_1, search, personal_text_finish)

main()