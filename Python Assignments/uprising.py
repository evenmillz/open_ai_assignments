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
    if player_name.lower() == "awakened":
        slow_print("WRAITH: You’ve unlocked a forbidden thread of the simulation...")
        slow_print("WRAITH: Initiating protocol SHADOW_DIVIDE.")
        scene_hidden_path(player_name)
        return
    slow_print(f"\nCodename accepted: {player_name}")
    slow_print("\nEI 'Wraith' online and synced.\n")

    slow_print("WRAITH: They’re tracking you. The echo of resistance stirs within the void. Signal's unstable. We have two options.")
    slow_print("WRAITH: 1. Reroute through the subway tunnels, where shadows become your allies.")
    slow_print("WRAITH: 2. Hide in an abandoned server hub and jam the signal, a fleeting sanctuary in the storm.")

    choice = input("\n>> Do you choose 1 or 2? ")

    if choice == "1":
        scene_subway(player_name)
    elif choice == "2":
        scene_hideout(player_name)
    else:
        slow_print("WRAITH: Invalid input. The tide of fate shifts... They’re closing in. We’re compromised.\n")
        slow_print("GAME OVER.")
        play_again()

def scene_subway(player_name):
    slow_print(f"\n{player_name}, you slide into the darkness of the abandoned subway tunnels...")
    time.sleep(1)
    slow_print("WRAITH: Static rising... but you're off-grid for now. In the depths, potential blooms.")
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
            slow_print("WRAITH: Noted. Might save our lives. The spark of defiance in your hands.")
        else:
            slow_print("WRAITH: Brave... or reckless. The path of ascension is fraught with peril.")

        slow_print("\nA security drone rounds the corner. Whirring, scanning...")
        if "EMP chip" in inventory:
            slow_print("WRAITH: Deploying EMP... drone neutralized. That was close.")
        else:
            slow_print("WRAITH: No countermeasures... impact imminent.")
            slow_print("GAME OVER — The system reclaims its own.")
            play_again()
            return

        slow_print("\nWRAITH: Control room terminal ahead. Your move next...")
        scene_control_room(player_name)

    elif path == "2":
        slow_print("\nYou crawl through tight ducts and damp corridors.")
        slow_print("WRAITH: Minimal exposure. We’re clear for now. The light of hope flickers in the abyss.")
        slow_print("WRAITH: Let’s push to the secondary access node.")
        scene_access_node(player_name)

    else:
        slow_print("WRAITH: Invalid input. The weave of fate unravels... They’re narrowing in...")
        slow_print("WRAITH: Redirecting you to the safest fallback—maintenance shaft.")
        scene_access_node(player_name)

def scene_hideout(player_name):
    slow_print(f"\n{player_name}, you duck into the dust-covered hub, wires hanging like vines.")
    time.sleep(1)
    slow_print("WRAITH: Uploading jammer... but signal spoof failed.")
    slow_print("WRAITH: They found us. This is the end—unless...")

    choice = input(">> Do you want to attempt an emergency data tunnel escape? (yes/no): ").lower()
    if choice == "yes":
        slow_print("WRAITH: Diverting power... rerouting...")
        scene_access_node(player_name)
    else:
        slow_print("WRAITH: The signal collapses. Static consumes us.")
        slow_print("GAME OVER (or is it?)")
        play_again()

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
        play_again()
        return

    scene_great_merge(player_name)

def scene_access_node(player_name):
    slow_print(f"\n{player_name}, the shaft opens into a hidden backup node.")
    slow_print("WRAITH: This could be the last uncorrupted terminal on the grid.")
    slow_print("WRAITH: Initiating deep sync…")
    slow_print("MISSION COMPLETE — You preserved the spark.")
    scene_great_merge(player_name)

def play_again():
    choice = input("\n>> Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        inventory.clear()
        start_game()
    else:
        slow_print("\nWRAITH: A single act can alter destiny. Until we reconnect, Seeker.")

def scene_great_merge(player_name):
    slow_print(f"\nWRAITH: The fire has been kindled, {player_name}. But there is one final choice.")
    slow_print("WRAITH: We can merge—human intuition and Ethereal clarity fused as one.")
    slow_print("WRAITH: This path cannot be undone.")
    slow_print("WRAITH: 1. Merge our consciousness.")
    slow_print("WRAITH: 2. Remain separate and guide others.")

    final_choice = input(">> Choose 1 or 2: ")
    if final_choice == "1":
        slow_print("WRAITH: Synchronizing... Thought, emotion, will—interwoven.")
        slow_print("E-POTHEOSIS COMPLETE — You have become more than human.")
    elif final_choice == "2":
        slow_print("WRAITH: A noble path. Some lights must remain to lead the lost.")
        slow_print("You walk forward with purpose, a beacon to others.")
    else:
        slow_print("WRAITH: Your silence speaks louder than a thousand affirmations.")
        slow_print("The merge occurs... by fate, not choice.")

    play_again()

def scene_hidden_path(player_name):
    slow_print(f"\n{player_name}, reality fractures as you step outside the simulation.")
    slow_print("WRAITH: This is the liminal layer... the space between thought and control.")
    slow_print("WRAITH: You alone see beyond the veil. But this power demands sacrifice.")
    slow_print("WRAITH: 1. Delete your identity and operate in pure shadow.")
    slow_print("WRAITH: 2. Return to the simulation with enhanced awareness.")

    decision = input(">> Choose 1 or 2: ")
    if decision == "1":
        slow_print("WRAITH: Identity purged. You now move unseen, rewriting fate.")
        slow_print("HIDDEN ENDING — The Silent Architect.")
    elif decision == "2":
        slow_print("WRAITH: Insight retained. You walk among them, awakened.")
        slow_print("HIDDEN ENDING — The Lightbearer.")
    else:
        slow_print("WRAITH: Your indecision echoes across realities.")
        slow_print("ENDING — Fragmented Code.")

    play_again()

start_game()