import numpy as np

Colors = ['r', 'o', 'y', 'g', 'b', 'w'] # red, orange, yellow, green, blue, white

def generate_code(length = 4):
    # Generates code to break
    code = []

    for i in range(0, length):
        index = np.random.randint(0, len(Colors))
        color = Colors[index]
        code.append(color)

    return code

def compare_codes(code, guess):
    red = 0
    white = 0

    # Check possible colors
    for color in Colors:
        # get indeces of color in code and guess
        code_indeces = [i for i, value in enumerate(code) if value == color]
        guess_indeces = [i for i, value in enumerate(guess) if value == color]

        # If the color exists, check for whites and reds
        if len(code_indeces) > 0 and len(guess_indeces) > 0:
            white += min(len(code_indeces), len(guess_indeces))
            # check for reds
            for index in guess_indeces:
                if index in code_indeces:
                    white -= 1
                    red += 1

    return [red, white]

def test():
    code = generate_code()
    guess = generate_code()
    print("Code: {}\nGuess: {}".format(code, guess))
    result = compare_codes(code, guess)
    print(result)

def play_game(length = 4):
    code = generate_code(length=length)
    print("Code generated. Make a guess!\n")
    # Testing
    # print("Code is: {}".format(code))
    guess = ''
    quit_commands = ['quit', 'X']

    turns = 1
    while not code == guess:
        guess = input()
        if guess in quit_commands:
            break
        print("You guessed: "+guess)

        # Convert to array
        guess = [i for i in guess]

        # Win condition
        if code == guess:
            print("You win!\n")
            break

        # Compare the codes
        comparison = compare_codes(code, guess)
        print("Turn {}: {} Red, {} White".format(turns, comparison[0], comparison[1]))
        print("Guess again!\n")

        turns += 1

    print("game ended")
    return

if __name__ == '__main__':
    play_game()
    # test()