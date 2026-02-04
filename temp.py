class SmartThermometer:
    def __init__(self, celsius):
        self._celsius = celsius  # Note the underscore (private-ish convention)

    @property
    def celsius(self):
        print("Fetching value...")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        print("Setting value...")
        self._celsius = value

# Usage
temp = SmartThermometer(20)
print(temp.celsius)    # Triggers the getter
temp.celsius = 35      # Triggers the setter
# temp.celsius = -300  # This would raise a ValueError