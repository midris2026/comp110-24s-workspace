"""Practice writing a class."""

class Profile:
    username: str
    private: bool

    def __init__(self, user_input: str):
        """Create a new profile object."""
        self.username = user_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If profile is public, print msg."""
        if self.private is False:
            print(msg) 