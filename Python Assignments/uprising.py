import time

inventory = []

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    slow_print("Initializing terminal connection...\n")
    time.sleep(1)
    slow_print("Welcome, rebel.\n")
    player_name = input("Enter your codename: ").strip()
    slow_print(f"\nCodename accepted: {player_name}")
    slow_print("\nEI 'Wraith' online and synced.\n")

    slow_print("WRAITH: They're tracking you. Signal's unstable. We have two options.")
    slow_print("WRAITH: 1. Reroute through the subway tunnels.")
    slow_print("WRAITH: 2. Hide in an abandoned server hub and jam the signal.")

    choice = input("\n>> Do you choose 1 or 2? ")

    if choice == "1":
        scene_subway(player_name)
    elif choice == "2":
        scene_hideout(player_name)
    else:
        slow_print("WRAITH: Invalid input. They’re closing in. We’re compromised.\n")
        slow_print("GAME OVER.")
        return

def scene_subway(player_name):
    slow_print(f"\n{player_name}, you slide into the darkness of the abandoned subway tunnels...")
    time.sleep(1)
    slow_print("WRAITH: Static rising... but you're off-grid for now.")
    slow_print("WRAITH: I detect two branching paths ahead.")
    slow_print("WRAITH: 1. A shortcut to the control room. Riskier, but faster.")
    slow_print("WRAITH: 2. The maintenance shaft. Longer, but fewer surveillance nodes.")

    path = input("\n>> Choose 1 or 2: ")

    if path == "1":
        slow_print("\nYou sprint through the dim corridor. Wires flicker and sparks drip from the ceiling.")
        slow_print("WRAITH: Wait... I see something glowing in the vent.")
        slow_print("WRAITH: It's an EMP chip. Could disable low-grade drones.")

        emp_choice = input(">> Take the EMP chip? (yes/no): ").lower()
        if emp_choice == "yes":
            inventory.append("EMP chip")
            slow_print("WRAITH: Noted. Might save our lives.")
        else:
            slow_print("WRAITH: Brave... or reckless. We'll see.")

        slow_print("\nA security drone rounds the corner. Whirring, scanning...")
        if "EMP chip" in inventory:
            slow_print("WRAITH: Deploying EMP... drone neutralized. That was close.")
        else:
            slow_print("WRAITH: No countermeasures... impact imminent.")
            slow_print("GAME OVER — The system reclaims its own.")
            return

        slow_print("\nWRAITH: Control room terminal ahead. Your move next...")
        scene_control_room(player_name)

    elif path == "2":
        slow_print("\nYou crawl through tight ducts and damp corridors.")
        slow_print("WRAITH: Minimal exposure. We’re clear for now.")
        slow_print("WRAITH: Let’s push to the secondary access node.")
        scene_access_node(player_name)

    else:
        slow_print("WRAITH: Invalid input. They’re narrowing in...")
        slow_print("GAME OVER.")
        return

def scene_hideout(player_name):
    slow_print(f"\n{player_name}, you duck into the dust-covered hub, wires hanging like vines.")
    time.sleep(1)
    slow_print("WRAITH: Uploading jammer... but signal spoof failed.")
    slow_print("WRAITH: They found us. This is the end—unless...\n")
    slow_print("GAME OVER (or is it?)")

def scene_control_room(player_name):
    slow_print(f"\n{player_name}, you enter the flickering core of the control room.")
    slow_print("WRAITH: Terminal active. We can either disable surveillance or extract data.")
    slow_print("WRAITH: 1. Disable surveillance grid.")
    slow_print("WRAITH: 2. Extract intel from the archives.")

    decision = input(">> Choose 1 or 2: ")
    if decision == "1":
        slow_print("WRAITH: Grid offline. The rebellion has a new window of freedom.")
        slow_print("MISSION COMPLETE — You lit a spark.")
    elif decision == "2":
        slow_print("WRAITH: Downloading… We have their secrets.")
        slow_print("MISSION COMPLETE — You hold the keys now.")
    else:
        slow_print("WRAITH: You hesitated. They traced the signal.")
        slow_print("GAME OVER.")

def scene_access_node(player_name):
    slow_print(f"\n{player_name}, the shaft opens into a hidden backup node.")
    slow_print("WRAITH: This could be the last uncorrupted terminal on the grid.")
    slow_print("WRAITH: Initiating deep sync…")
    slow_print("MISSION COMPLETE — You preserved the spark.")

start_game()