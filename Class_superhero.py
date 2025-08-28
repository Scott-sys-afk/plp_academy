class Superhero:
    def __init__(self, name, secret_identity, origin_story, power_level):
        self.name = name
        self.secret_identity = secret_identity
        self.origin_story = origin_story
        self.power_level = power_level
        self._secret_hideout = "Unknown"  # Encapsulated attribute
    
    def introduce(self):
        return f"I am {self.name}, also known as {self.secret_identity}! {self.origin_story}"
    
    def move(self):
        return "I'm moving in a generic superhero way!"
    
    def use_power(self):
        return f"{self.name} uses a generic power at level {self.power_level}!"
    
    # Getter and setter for encapsulated attribute
    def get_secret_hideout(self):
        return self._secret_hideout
    
    def set_secret_hideout(self, location):
        self._secret_hideout = location
        return f"Hideout location updated to: {location}"
    
    def __str__(self):
        return f"Superhero: {self.name} (Power Level: {self.power_level})"


# Subclasses demonstrating polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, origin_story, power_level, max_speed):
        super().__init__(name, secret_identity, origin_story, power_level)
        self.max_speed = max_speed  # in mph
    
    def move(self):
        return f"🦸♂️ {self.name} is flying through the air at up to {self.max_speed} mph!"
    
    def use_power(self):
        return f"✈️ {self.name} soars through the sky with aerial superiority!"


class SpeedsterHero(Superhero):
    def __init__(self, name, secret_identity, origin_story, power_level, max_speed):
        super().__init__(name, secret_identity, origin_story, power_level)
        self.max_speed = max_speed  # in mph
    
    def move(self):
        return f"⚡ {self.name} is running at incredible speed ({self.max_speed} mph)!"
    
    def use_power(self):
        return f"🏃♂️ {self.name} creates a vortex of wind while running!"


class TeleportingHero(Superhero):
    def __init__(self, name, secret_identity, origin_story, power_level, max_distance):
        super().__init__(name, secret_identity, origin_story, power_level)
        self.max_distance = max_distance  # in miles
    
    def move(self):
        return f"🌀 {self.name} teleports instantly up to {self.max_distance} miles!"
    
    def use_power(self):
        return f"💫 {self.name} disappears and reappears in a blink of an eye!"


class AquaticHero(Superhero):
    def __init__(self, name, secret_identity, origin_story, power_level, max_depth):
        super().__init__(name, secret_identity, origin_story, power_level)
        self.max_depth = max_depth  # in feet
    
    def move(self):
        return f"🌊 {self.name} is swimming powerfully through the water (max depth: {self.max_depth} ft)!"
    
    def use_power(self):
        return f"🐠 {self.name} commands the creatures of the deep!"


# Demonstration
if __name__ == "__main__":
    # Create superheroes with different movement abilities
    superman = FlyingHero("Superman", "Clark Kent", 
                         "Last son of Krypton, protector of Earth.", 
                         95, 2000)
    
    flash = SpeedsterHero("The Flash", "Barry Allen", 
                         "Struck by lightning, doused in chemicals.", 
                         90, 670000000)
    
    nightcrawler = TeleportingHero("Nightcrawler", "Kurt Wagner", 
                                  "Mutant with the ability to teleport.", 
                                  85, 2)
    
    aquaman = AquaticHero("Aquaman", "Arthur Curry", 
                         "Half-human, half-Atlantean ruler of the seas.", 
                         88, 36000)
    
    # Create a list of superheroes
    justice_league = [superman, flash, nightcrawler, aquaman]
    
    # Demonstrate polymorphism - same method, different behaviors
    print("=== SUPERHERO MOVEMENT DEMONSTRATION ===")
    for hero in justice_league:
        print(hero.move())
    
    print("\n=== SUPERHERO POWER USAGE ===")
    for hero in justice_league:
        print(hero.use_power())
    
    # Demonstrate encapsulation
    print("\n=== ENCAPSULATION DEMONSTRATION ===")
    print(f"Superman's current hideout: {superman.get_secret_hideout()}")
    print(superman.set_secret_hideout("Fortress of Solitude"))
    print(f"Superman's updated hideout: {superman.get_secret_hideout()}")
    
    # Show all superhero details
    print("\n=== SUPERHERO PROFILES ===")
    for hero in justice_league:
        print(hero)
        print(f"  Secret Identity: {hero.secret_identity}")
        print(f"  Introduction: {hero.introduce()}\n")