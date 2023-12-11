class Utility:

    def get_command(self):
        while True:
            try:
                command = int(input("Option: "))
                assert command in [1, 2, 3, 4]
                return command

            except (ValueError, AssertionError):
                self.enter("Invalid Command")


    def get_text_input(self, msg=""):
        return input(msg)


    def get_numerical_input(self, msg=""):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("Valoarea introdusa nu este un numar, incercati alta valoare")


    def enter(self, msg=""):
        input(f"{msg}\nPress Enter to continue")
