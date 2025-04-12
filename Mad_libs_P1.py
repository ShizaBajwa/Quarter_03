import time

def madlibs():
    print("Welcome to the Mad Libs Adventure! A brand-new magical story is on the way...\n")

    # Pre-filled inputs
    name = "Shiza"
    age = "21"
    city = "Karachi"
    profession = "space engineer"
    magical_creature = "griffin"
    adjective1 = "fearless"
    adjective2 = "glowing"
    object1 = "golden compass"
    object2 = "laser gauntlet"
    superpower = "mind control"
    villain_name = "Shadowclaw"
    verb = "disarm"

    # Story with inserted values
    story = f"""
    In the distant city of {city}, nestled between the stars and clouds, lived a {adjective1} {profession} named {name}.
    At just {age} years old, {name} had already invented dozens of powerful machines and was admired for their unique power of {superpower}.

    One evening, while testing a secret project, {name} discovered a hidden chamber containing a {object1}.
    As soon as they picked it up, a portal opened and out flew a majestic {magical_creature} with sparkling wings.

    The {magical_creature} revealed that {name} was destined to stop the rise of the dark sorcerer, {villain_name},
    who was gathering forces to conquer {city} and erase all memories of joy.

    With a {adjective2} {object2} on their arm and the courage of a thousand stars, {name} soared across galaxies,
    facing asteroid storms, code-breaking robots, and ancient cosmic puzzles.

    At the final showdown, {villain_name} tried to unleash a wave of darkness,
    but {name} used their {superpower} to {verb} the sorcerer before the spell was complete.

    The stars aligned, peace returned to {city}, and the {magical_creature} crowned {name} as the Guardian of the Cosmos.
    From that day forward, tales of {name}'s bravery echoed across time and space... 🚀✨

    THE END.
    """

    print("Generating your story...\n")
    time.sleep(2)
    print(story)

# Run the Mad Libs Game
if __name__ == "__main__":
    madlibs()
