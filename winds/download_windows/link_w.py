from winds.program_class import Program

class LinkWindow(Program):
    def __init__(self):
        pass

    def init_window(self):
        self.clear()
        print("Enter Link")
        self.line_breaker()

        user_input = input("Enter video link (no spaces): ")
        return user_input