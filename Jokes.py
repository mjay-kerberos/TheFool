import time
import random
import argparse

#Local Script
def print_random_words(word_bank, count, lag_duration):
    for _ in range(count):
        word = random.choice(word_bank)
        print(word)
        time.sleep(random.randint(1, 240))  # Random interval between 1 and 240 seconds
    #print("Introducing lag...")
    time.sleep(lag_duration)  # Introduce a lag

joker = [
    "What doesn't kill you simply makes you stranger!", 
    "This is going to hurt you a lot more than it does me.", 
    "The only sensible way to live in this world is without rules.", 
    "Their morals, their code—it's a bad joke.", 
    "Wait 'til they get a load of me.",
    "You have nothing, nothing to threaten me with. Nothing to do with all your strength.",
    "Is it just me or is it getting crazier out there?",
    "It's not about the money, it's about sending a message. Everything burns!",
    "Don't test the monster in me!",
    "I'm crazy enough to take on Batman, but the IRS? Nooo, thank you!",
    "It'd be funny if it weren’t so pathetic.",
    "Why don't you just give me a call when you start taking things a little more seriously?",
    "Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos.",
    "The real joke is your stubborn, bone deep conviction that somehow, somewhere, all of this makes sense! That's what cracks me up each time!",
    "I feel like I know you. I've been watching you forever.",
    "You look good. Been working out? You could probably use a little sun. Then again, who am I to talk?",
    "Lady, you're harder to kill than a cockroach on steroids!",
    "You can't win anyway... You see, I hold the winning card!",
    "Very neat! That ugly head of yours does have a brain!",
    "This is what happens when an unstoppable force meets an immovable object.",
    "C'mon Bats, get crazy. It's the only way to beat me!",
    "Over?! Why, my dear, delusional Dark Knight, it hasn't even begun!",
    "I can't wait to show you my toys.",
    "You see, I'm not a monster. I'm just ahead of the curve.",
    "If I weren't insane, I couldn't be so brilliant!"
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prints random Joker quotes with a configurable lag.")
    parser.add_argument("--lag", type=int, default=300, help="Lag duration in seconds after printing quotes (default: 300)")
    parser.add_argument("--count", type=int, default=5, help="Number of quotes to print (default: 5)")
    args = parser.parse_args()

    print_random_words(joker, args.count, args.lag)
