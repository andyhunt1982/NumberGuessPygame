import pygame
import random

# Initialize pygame
pygame.init()

# Set window size and title
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Number Guessing Game")

# Set font and text colors
font = pygame.font.Font(None, 30)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (128, 128, 128)
blue = (0, 0, 255)

# Generate random number to guess
number_to_guess = random.randint(1, 100)

# Initialize game variables
game_over = False
guessed_correct = False
number_of_guesses = 0


# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Draw the grid of numbers
        for i in range(0, 100):
            number_text = font.render(str(i + 1), True, grey)
            screen.blit(number_text, [(i % 10 * (size[0] // 10)) + 20, (i // 10 * (size[1] // 10)) + 20])

        # Check if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the click
            pos = pygame.mouse.get_pos()

            # Get the column and row of the click
            column = pos[0] // (size[0] // 10)
            row = pos[1] // (size[1] // 10)

            # Get the number that was clicked
            number = column + row * 10 + 1

            # Increment the number of guesses
            number_of_guesses += 1

            # Update the title to display the number of guesses
            pygame.display.set_caption("Number Guessing Game - Number of guesses: " + str(number_of_guesses))

            # Check if the number is the correct guess
            if number == number_to_guess:
                guessed_correct = True
                message = font.render("Congratulations! You guessed the correct number!", True, blue)
                screen.blit(message, (50, 250))
                pygame.display.flip()
            # Check if the number is too high
            elif number > number_to_guess:
                for i in range(number, 101):
                    pygame.draw.rect(screen, grey, [i % 10 * (size[0] // 10), i // 10 * (size[1] // 10), size[0] // 10, size[1] // 10])
                pygame.display.flip()
            # Check if the number is too low
            elif number < number_to_guess:
                for i in range(0, number):
                    pygame.draw.rect(screen, grey, [i % 10 * (size[0] // 10), i // 10 * (size[1] // 10), size[0] // 10, size[1] // 10])
                pygame.display.flip()

            # Draw the grid of numbers
            for i in range(0, 100):
                if i+1 == number_to_guess and guessed_correct:
                    pygame.draw.rect(screen, green, [i % 10 * (size[0] // 10), i // 10 * (size[1] // 10), size[0] // 10,
                                                     size[1] // 10])
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    game_over = True
                elif i+1 == number:
                    pygame.draw.rect(screen, red, [i % 10 * (size[0] // 10), i // 10 * (size[1] // 10), size[0] // 10,
                                                   size[1] // 10])

        # Update the display
        pygame.display.flip()

# closing animation here
for i in range(0, 100):
    pygame.draw.rect(screen, green, [i % 10 * (size[0] // 10), i // 10 * (size[1] // 10), size[0] // 10,
                                     size[1] // 10])
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()

