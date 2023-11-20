class Animal:
    """Basic representation of an animal."""

    def __init__(self):
        """Initialize an animal with two eyes."""
        self.num_eyes = 2

    def breathe(self):
        """Simulate breathing of an animal."""
        print("Inhale, exhale.")


class Fish(Animal):
    """Represents a Fish, a subclass of Animal."""

    def __init__(self):
        """Initialize a Fish, inheriting from Animal."""
        super().__init__()

    def breathe(self):
        """Extend breathing method specific to Fish (underwater)."""
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        """Simulate fish swimming."""
        print("Moving in water.")


# Create an instance of Fish and demonstrate its capabilities
nemo = Fish()
nemo.swim()
nemo.breathe()

# Display number of eyes of the fish
print(nemo.num_eyes)
