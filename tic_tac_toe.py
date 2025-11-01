class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as list
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current state of the board"""
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   \n")
    
    def display_positions(self):
        """Show position numbers for reference"""
        print("\nPosition numbers:")
        print("   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   \n") 
   
    def is_valid_move(self, position):
        """Check if the move is valid"""
        return 1 <= position <= 9 and self.board[position - 1] == ' '
    
    def make_move(self, position):
        """Make a move on the board"""
        if self.is_valid_move(position):
            self.board[position - 1] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner"""
        # Winning combinations (indices)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        return ' ' not in self.board
    
    def switch_player(self):
        """Switch between X and O"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'    

    def play(self):
        """Main game loop"""
        print("Welcome to Tic Tac Toe!")
        print("Player X goes first.")
        self.display_positions()
        
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                position = int(input("Enter position (1-9): "))
                
                if not self.is_valid_move(position):
                    print("Invalid move! Position already taken or out of range.")
                    continue
                
                self.make_move(position)
                
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Player {winner} wins!")
                    break
                
                # Check for tie
                if self.is_board_full():
                    self.display_board()
                    print("It's a tie! 🤝")
                    break
                
                self.switch_player()
                
            except ValueError:
                print("Please enter a valid number between 1 and 9.")


def main():
    """Main function to run the game"""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()