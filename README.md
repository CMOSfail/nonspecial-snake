# Very Non-Special Snake Game!!!1!
(Heading Level 1)

## Overview
(Heading Level 2)

The Very Non-Special Snake Game!!!1! is a classic snake game developed in Python using the pygame library. This project is designed both for fun and as a learning tool for those interested in game development with Python. The game includes various features such as bombs, golden apples, and customizable settings to enhance the gameplay experience.
(Paragraph)

## Features
(Heading Level 2)

- **Classic Snake Gameplay**: Control the snake to eat apples and grow longer.

- **Golden Apples**: Occasionally appear and grant extra points and length.

- **Bombs**: Randomly appear; colliding with them either ends the game or cuts the snake's length in half (configurable).

- **Pause Functionality**: Pause and resume the game with the space bar.

- **Customizable Settings**: Adjust game parameters via a settings.json file.

- **Learning-Oriented Code**: Well-documented code to facilitate learning and understanding.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your system. You can download it from the official website.

- **Pygame**: Install the pygame library using pip:

```
pip install pygame
```

### Download the Game

1. **Clone the Repository**

```
git clone https://github.com/CMOSfail/nonspecial-snake.git
```

2. **Navigate to the Game Directory**

```
cd nonspecial-snake
```

## How to Play

### Starting the Game

Run the game using the following command:

```
python snake.py
```

### Controls

- **Start the Game**: Press the Enter key on the start screen.

- **Move the Snake**:

  - Left: Arrow Left or 'A'

  - Right: Arrow Right or 'D'

  - Up: Arrow Up or 'W'

  - Down: Arrow Down or 'S'

- **Pause/Resume Game**: Press the Space Bar.

- **Exit to Start Screen**: Press the Esc Key during gameplay.

### Objective

Control the snake to eat apples and grow longer. Avoid colliding with the snake's own body and bombs. Try to achieve the highest score possible!

### Special Items

- **Golden Apples**:

  - Grant extra points and length.

  - Appear occasionally and have a limited duration.

  - If not eaten within a specified time, they disappear.

- **Bombs**:

  - Avoid them! Depending on settings, they can either end the game or cut your length in half.

  - Appear randomly and disappear after a short time.

## Customization

You can customize various game settings by editing the settings.json file:

```json
{
  "bombs_enabled": true,
  "bomb_behavior": 2,
  "golden_apple_enabled": true,
  "golden_apple_duration": 10,
  "speed_percentage": 100,
  "screen_width": 1280,
  "screen_height": 720
}
```

- **bombs_enabled**: true or false to enable or disable bombs.

- **bomb_behavior**:

  - 1: Collision with a bomb ends the game.

  - 2: Collision cuts the snake's length in half.

- **golden_apple_enabled**: true or false to enable or disable golden apples.

- **golden_apple_duration**: Time in seconds before a golden apple disappears.

- **speed_percentage**: Adjusts the game speed (from 50% to 300%).

- **screen_width and screen_height**: Set the game's resolution (minimum 1280x720).

## Creating a Similar Project

This project is intended to be a learning resource. If you'd like to create a similar game or learn from this project, here are the steps you can follow:

### 1. Set Up Your Development Environment

- Install Python and pygame.

- Choose a code editor or IDE (e.g., VSCode, PyCharm).

### 2. Understand the Game Mechanics

- **Game Loop**: The core of the game, handling events, updates, and rendering.

- **Event Handling**: Capturing user inputs and responding to them.

- **Game States**: Managing different screens (start, pause, game over).

### 3. Create the Game Window

- Use pygame to initialize and set up the display window with the desired resolution.

### 4. Implement the Snake

- Represent the snake as a list of coordinate tuples.

- Implement movement logic and ensure the snake moves smoothly on the grid.

### 5. Add Food Items

- Create regular apples that the snake can eat to grow longer.

- Randomly place apples on the grid, avoiding the snake's current position.

### 6. Implement Collision Detection

- Check for collisions with the snake's own body.

- Implement behavior when the snake eats an apple.

### 7. Introduce Special Items

- **Golden Apples**: Implement logic for special apples that grant extra points and have a timer.

- **Bombs**: Add bombs that appear randomly and have specific collision behaviors.

### 8. Add Game Controls

- Implement key presses for controlling the snake.

- Add functionality to pause the game and return to the start screen.

### 9. Customize Settings

- Create a configuration file (settings.json) to allow easy customization of game parameters.

### 10. Enhance the User Interface

- Add a start screen with game information and instructions.

- Create a game over screen with options to restart or exit.

### 11. Document Your Code

- Add comments and docstrings to explain your code.

- Write a README file to provide an overview and usage instructions.

### 12. Test and Iterate

- Playtest your game thoroughly to find and fix bugs.

- Seek feedback and make improvements.

## Credits

- **Developer**: Itamar Itzhaki

- **Git Repository**: https://github.com/CMOSfail/nonspecial-snake

- **Acknowledgments**:

  - Utilizes the pygame library for game development.

---

Feel free to explore the code, customize it, and use this project as a starting point for your own game development journey!
