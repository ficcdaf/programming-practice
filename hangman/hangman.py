import art

### HANGMAN Game
# Note: anywhere you see `pass`, like here:
pass
# This is us leaving a hint that you should put some code here!


# pick_word is a function that picks a random word
# from a big list of English words.
def pick_word():
    ## We read a list of words from a text file
    # (You can ignore the details)
    file = open("words.txt", "r")
    words = file.readlines()
    file.close()

    # Now, the variable `words` is a list of English words.
    # Each word is a separate string.
    ## Your task is to pick a random word from this list,
    ## and `return` it from this function.
    pass


# prompt is a function that asks the player
# for their guess.
def prompt():
    # Ask player for their guess!
    # You can also check if the guess is a letter here. (optional)
    # Don't forget to `return` the guess!
    pass


# This function prints the hangman art
# from a list of strings, where each
# string is a different "stage" of the
# hangman. The file is in `art.py`
# if you want to look at it.

## HINT: See the `import art` at the top? Doesn't that
## remind you of `import random`? So, if you wanted to access
## something called `PICTURES` from the `art` file in your code,
## how would you do it?


## HINT: We need to print the `hangman` with
# the right amount of limbs. Maybe we can
# pass an `argument` to this function?
def draw_hangman(stage):
    pass


def play_hangman():
    # Using the pick_word function, pick a random word
    # and store it in a variable called `secret`
    pass

    ## Initialize Game State
    # ^ fancy way to say: "create variables we will use to track progress"
    ## Game State:
    # Correct Guesses List: `correct`
    # Wrong Guesses List: `wrong`
    # Strikes Counter: `strikes`
    # Maximum "strikes and you're out": `max_strikes`
    pass

    ## Before we start, we should tell the player how long
    # the secret word is!
    pass

    ## Begin the main game loop here!
    running = True
    while running:
        # Ask the player for their guess using the `prompt` function!
        # Don't forget to store their guess in a variable.
        pass

        ## Update the Game State
        # Here, we check the player's guess, and update
        # our tracking variables
        pass

        ## Print the game state
        # Now that the game state is updated,
        # we should visually show the player what's going on.
        ## 1. Print the `strikes` counter and `wrong` guesses list.
        ## 2. Print the "covered" word:
        # EXAMPLE
        # secret = apple
        # guessed = ['a', 'l']
        # The covered word should be: `a__l_`
        ## Make sure to save the covered word in a variable!
        ## Who knows if we'll need it later? ;)
        pass

        ## Draw the Hangman
        # We're going to skip this step for now.
        # Don't worry, we'll get to it!
        # But usually, adding the flashy stuff is the last step.
        pass

        ## Win/Loss State Check
        # ^ Fancy way to say: check if the player won or lost!
        # If the player wins or loses, we should stop running the game!

        ## Use the covered word to check if the player has won the game!
        pass

        ## Use `strikes` and `max_strikes` to check if the player lost the game!
        pass

    ## Let's thank the player!
    print("Thanks for playing!")


def main():
    pass


if __name__ == "__main__":
    main()
