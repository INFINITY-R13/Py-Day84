# Tic Tac Toe Game

A simple text-based Tic Tac Toe game built in Python for two players.

## Features

- Clean ASCII art board display
- Interactive gameplay for two players
- Input validation and error handling
- Win detection for all possible combinations
- Tie game detection
- Play multiple rounds
- Position reference guide

## How to Run

```bash
python tic_tac_toe.py
```

## How to Play

1. The game displays a 3x3 grid with position numbers 1-9
2. Player X goes first, followed by Player O
3. Enter a number (1-9) to place your symbol in that position
4. First player to get 3 symbols in a row wins!
5. Game ends in a tie if all positions are filled with no winner

## Board Layout

```
Position numbers:     Example game:
 1 | 2 | 3            X | O | X
___|___|___          ___|___|___
 4 | 5 | 6            O | X | O
___|___|___          ___|___|___
 7 | 8 | 9            X | O | X
```

## Winning Conditions

You win by getting 3 of your symbols in a line:
- **Horizontal**: Rows 1-2-3, 4-5-6, or 7-8-9
- **Vertical**: Columns 1-4-7, 2-5-8, or 3-6-9
- **Diagonal**: 1-5-9 or 3-5-7

## Game Flow

1. Game shows position reference
2. Current board state is displayed
3. Current player is prompted for their move
4. Invalid moves are rejected with helpful messages
5. Game checks for winner or tie after each move
6. Option to play again after game ends

## Requirements

- Python 3.x
- No external dependencies required

## Code Structure

The game is built using object-oriented programming with a `TicTacToe` class that handles:
- Board state management
- Move validation
- Win/tie detection
- Player switching
- Game display

Enjoy playing! 🎮