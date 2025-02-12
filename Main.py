import random
import time

def print_slow(text, delay=0.05):
    """Prints text one character at a time for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline after finishing

def intro():
    print_slow("Welcome, brave adventurer, to the Mystic Maze!")
    print_slow("You find yourself in an enchanted labyrinth, filled with mysteries and dangers.")
    print_slow("Your quest is to find the hidden exit of this maze and escape with your life.")
    print_slow("Beware: monsters, traps, and unexpected treasures await you...\n")
    time.sleep(1)

def get_direction():
    """Prompts the player for a valid direction (n, s, e, w)."""
    direction = input("Which direction will you choose? (n/s/e/w): ").strip().lower()
    while direction not in ['n', 's', 'e', 'w']:
        direction = input("Invalid choice. Please enter 'n', 's', 'e', or 'w': ").strip().lower()
    return direction

def move(position, direction):
    """Returns a new position based on the current position and the chosen direction."""
    x, y = position
    if direction == 'n':
        y += 1
    elif direction == 's':
        y -= 1
    elif direction == 'e':
        x += 1
    elif direction == 'w':
        x -= 1
    return (x, y)

def in_bounds(position, size):
    """Checks if the new position is within the maze boundaries."""
    x, y = position
    return 0 <= x < size and 0 <= y < size

def random_event():
    """Randomly selects an event for an unexplored cell."""
    return random.choice(["nothing", "monster", "trap", "treasure"])

def encounter_monster(health):
    print_slow("A menacing monster appears from the shadows!")
    action = input("Do you fight (f) or run (r)? ").strip().lower()
    while action not in ['f', 'r']:
        action = input("Invalid choice. Choose 'f' to fight or 'r' to run: ").strip().lower()
    if action == 'f':
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print_slow("You bravely fight and defeat the monster!")
        else:
            damage = random.randint(10, 30)
            health -= damage
            print_slow(f"The monster overpowers you! You lose {damage} health.")
    else:
        damage = random.randint(5, 15)
        health -= damage
        print_slow(f"You try to run away but trip, losing {damage} health in the process.")
    return health

def trigger_trap(health):
    damage = random.randint(5, 20)
    health -= damage
    print_slow(f"You stepped on a hidden trap and lose {damage} health!")
    return health

def find_treasure(inventory):
    print_slow("You discover a hidden chest glimmering in the darkness!")
    print_slow("Inside, you find a shiny gold coin which you add to your inventory.")
    inventory.append("Gold Coin")
    return inventory

def main():
    maze_size = 5
    # Starting position is fixed at (0,0)
    position = (0, 0)
    # Randomly assign the exit somewhere in the maze (but not at the start)
    exit_position = (random.randint(0, maze_size - 1), random.randint(0, maze_size - 1))
    while exit_position == position:
        exit_position = (random.randint(0, maze_size - 1), random.randint(0, maze_size - 1))
    
    health = 100
    inventory = []
    visited = set()

    intro()
    
    print_slow(f"Your starting position is {position}.")
    print_slow("The maze is a 5x5 grid. Find your way to the exit, hidden somewhere within.\n")
    
    while health > 0:
        print_slow(f"\nCurrent position: {position} | Health: {health} | Inventory: {inventory}")
        if position == exit_position:
            print_slow("A radiant light beckons you... You've found the exit of the Mystic Maze!")
            print_slow("Congratulations, you have completed your quest!")
            if "Gold Coin" in inventory:
                print_slow("And you escape with a treasure in hand. Well done!")
            else:
                print_slow("Though you found the exit, you might have wished for a bit more loot.")
            return
        
        direction = get_direction()
        new_position = move(position, direction)
        
        if not in_bounds(new_position, maze_size):
            print_slow("A mystical barrier prevents you from moving in that direction.")
            continue
        
        position = new_position
        
        if position not in visited:
            visited.add(position)
            event = random_event()
            if event == "monster":
                health = encounter_monster(health)
            elif event == "trap":
                health = trigger_trap(health)
            elif event == "treasure":
                inventory = find_treasure(inventory)
            else:
                print_slow("The area is eerily quiet... nothing happens here.")
        else:
            print_slow("You've already explored this area. Nothing new happens here.")
    
    print_slow("Your journey has ended as your injuries have taken their toll. Game Over.")

if __name__ == "__main__":
    main()
