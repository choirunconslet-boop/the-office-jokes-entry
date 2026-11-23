"""One-line office joke entry for the make.fun 'Make the AI Judge Laugh' bounty.

Writes a single one-line joke about office life to /output/entry.txt.
"""

import os

JOKE = "I replied-all asking everyone to stop replying all, and 47 people have now replied-all to agree."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
