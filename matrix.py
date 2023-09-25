import random
import string
import time


#fade = "10101%#*+=-:. "
fade = "TIJMEN%=-. "
width = 100
rows = [-1 for _ in range(width)]


def generate_str(idx: int):
    if idx > len(fade)-1 or idx == -1:
        return " "
    return fade[idx]


def main():

    while True:
        result = ""
        for i, row in enumerate(rows):
            if row == -1:
                if random.randint(0, 10) == 1:
                    rows[i] = 0

            elif row > len(fade) + 5:
                rows[i] = -1
            
            else:
                rows[i] += 1

            result += " " + generate_str(row)

        print(f"\033[92m{result}\033[0m")
        time.sleep(0.05)


if __name__ == "__main__":
    main()