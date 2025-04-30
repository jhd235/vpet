import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.alive = True

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")

    def feed(self):
        self.hunger = max(0, self.hunger - 25)
        self.energy = min(100, self.energy + 10)
        print(f"\nYou fed {self.name}!")

    def play(self):
        self.happiness = min(100, self.happiness + 25)
        self.hunger = min(100, self.hunger + 15)
        self.energy = max(0, self.energy - 20)
        print(f"\nYou played with {self.name}!")

    def rest(self):
        self.energy = min(100, self.energy + 30)
        self.happiness = max(0, self.happiness - 10)
        print(f"\n{self.name} took a nap!")

    def time_pass(self):
        self.hunger = min(100, self.hunger + 10)
        self.happiness = max(0, self.happiness - 5)
        self.energy = max(0, self.energy - 5)

        if self.hunger == 100 or self.happiness == 0 or self.energy == 0:
            self.alive = False

def game_loop():
    pet_name = input("Name your virtual pet: ")
    pet = VirtualPet(pet_name)
    
    while pet.alive:
        pet.status()
        print("\nOptions:")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Do nothing")
        print("5. Quit")
        
        choice = input("\nWhat will you do? ")
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            print("\nYou watch TV while your pet stares at you...")
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice!")
        
        pet.time_pass()
        time.sleep(1)
    
    if not pet.alive:
        print(f"\nOh no! {pet.name} has... crossed the rainbow bridge. 💔")

if __name__ == "__main__":
    game_loop()