from art import *
from colorama import *
from playsound import *

init(autoreset=True)

class Program:
    def _init_(self):
        self.user_name = ""

    def welcome(self):
        self.user_name = input("Enter your name: ")
        print(f"Welcome, {Fore.GREEN}{self.user_name}{Fore.RESET}!")
        print(Fore.YELLOW + text2art("Welcome to the Program"))

    def print_options(self):
        options = [
            f"{Fore.YELLOW}happy",
            f"{Fore.BLUE}sad",
            f"{Fore.RED}angry",
            f"{Fore.CYAN}exhausted",
            f"{Fore.MAGENTA}anxious"
        ]
        print("How are you feeling today?")
        for i, option in enumerate(options, start=1):
            print(f"{Fore.WHITE}{i}. {option}")
        print(Fore.YELLOW + text2art("How are you feeling today?"))

    def handle_happy(self):
        print(Fore.WHITE + text2art("Oh, that's good!"))
        print("Have a nice day.")

    def handle_sad(self):
        print(text2art("Try talking to your friends."))
        print(text2art("Do some sports."))
        print(text2art("Watch your favorite program."))

    def handle_angry(self):
        print(text2art("Take a deep breath."))
        print(text2art("Listen to calm music."))
        print(text2art("Walk in a quiet place."))

    def handle_exhausted(self):
        print(text2art("Make sure to balance your diet."))
        print(text2art("Avoid stress."))
        print(text2art("Get a good sleep."))

    def handle_anxious(self):
        print(text2art("Relax."))
        print(text2art("Do an activity you love."))
        print(text2art("Play sports."))

    def ask_feeling(self):
        self.print_options()
        choice = input("Enter your choice (1-5): ")
        options = {
            "1": self.handle_happy,
            "2": self.handle_sad,
            "3": self.handle_angry,
            "4": self.handle_exhausted,
            "5": self.handle_anxious
        }
        options.get(choice, lambda: print("Invalid choice."))()

    def feel_better(self):
        response = input("Do you feel better after doing these tips? (yes/no): ")
        if response.lower() == "yes":
            print(text2art("Great!"))
            print("Have a wonderful day!")
            return True
        elif response.lower() == "no":
            print(text2art("You may consider seeking advice from a psychiatrist."))
            return True
        else:
            print("Invalid choice.")
            return self.feel_better()

    def run(self):
        try:
            self.welcome()
            while True:
                self.ask_feeling()
                if self.feel_better():
                    break
        except KeyboardInterrupt:
            print(f"\n\nProgram terminated by {Fore.RED}the user{Fore.RESET}.")
        finally:
            print(Fore.YELLOW + text2art("Thank You!"))
            print("See you soon.")


if __name__ == "__main__":
    program = Program()
    program.run()
