import random
import sys
from textwrap import dedent

RANGE = (0, 3)

def printEvent(eventId) -> None:
    match eventId:
        case 0:
            print("This is test 1")
        case 1:
            print("This is test 2")
        case 2:
            print("This is test 3")
        case 3:
            print("This is test 4")

def getChoice() -> int:
    while True:
        choice = input("Choose an action (1, 2, or 3): ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print(" Please enter 1, 2, or 3.")

def resolve(choice: int, eventId: int):
    if choice == 1:
        print("You lose!")
        return False
    elif choice == 2:
        print("You lose!")
        return False
    elif choice == 3:
        print("You continue onto the next day")
        return True

def main() -> None:
    print(dedent("""
        ================================
        WELCOME TO THY FOOT SHALL SLIP 
        Survive as long as you can…
        (Ctrl‑C to quit manually)
        ================================))
                 """))
    
    roundNumber = 1

    while True:
        print(f"\n--- Round {roundNumber} ---")
        eventId = random.randint(*RANGE)
        printEvent(eventId)

        choice = getChoice()
        if (resolve(choice, eventId)):
            roundNumber += 1
            continue
        else:
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for playing! Goodbye.")