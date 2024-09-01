import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input(
                'Enter your move (rock, paper, scissors)'
                ' [q to quit]: ').lower()
            if move in moves:
                return move
            elif move == 'q':
                print("-----------------------------------------")
                return 'q'
            else:
                print('Invalid move,Try again')

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_moves = []

    def move(self):
        for move in moves:
            if move not in self.last_moves:
                return move

    def learn(self, my_move, their_move):
        self.last_moves.append(my_move)
        if len(self.last_moves) % 3 == 0:
            self.last_moves = []


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.current_round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == 'q' or move2 == 'q':
            return False
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1.score += 1
            print(f"Player 1 wins the Round {self.current_round}!")
        elif beats(move2, move1):
            self.p2.score += 1
            print(f"Player 2 wins the Round {self.current_round}!")
        else:
            print("Tie...")
        return True

    def play_game(self):
        print(
            "-----------------------------{Game start!}----------"
            "--------------------")
        while True:
            self.current_round += 1
            print(f"Round {self.current_round}:")
            print(f"[Player 1] {self.p1.score} - {self.p2.score} "
                  "[Player 2]\n")
            if not self.play_round():
                break
            print(
                "----------------------------------------------------"
                "--------------------")
            if self.p1.score == 3 or self.p2.score == 3:
                break
        print("-------------------------------{Game over!}---------"
              "--------------------")
        print(
            "---------------------------------------------------------"
            "---------------")
        print("Final Score board:\n"
              f"[Player 1] {self.p1.score} - {self.p2.score} [Player 2]")
        print(
            "----------------------------------------------------------"
            "--------------")
        if self.p1.score > self.p2.score:
            print("Player 1 wins the game!")
        elif self.p1.score < self.p2.score:
            print("Player 2 wins the game!")
        else:
            print("It's a tie!")


def start_game():
    while True:
        game_mode = input(
            "Choose the difficulty of the game "
            "(Starter, Easy, Medium, Hard): ").lower()
        if game_mode == 'starter':
            game = Game(HumanPlayer(), RockPlayer())
            break
        elif game_mode == 'easy':
            game = Game(HumanPlayer(), RandomPlayer())
            break
        elif game_mode == 'medium':
            game = Game(HumanPlayer(), ReflectPlayer())
            break
        elif game_mode == 'hard':
            game = Game(HumanPlayer(), CyclePlayer())
            break
        else:
            print("Invalid difficulty level. Try again.")
    game.play_game()


def play_again():
    response = input("Do you want to play again? (y/n): ")
    if response.lower() == 'y':
        return True
    elif response.lower() == 'n':
        return False
    else:
        print("Invalid input. Try again.")
        play_again()


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors Game!")
    while True:
        start_game()
        print(
            "-----------------------------------------------------"
            "-------------------")
        print(
            "-----------------------------------------------------"
            "-------------------")
        if not play_again():
            print(
                "-------------------------{Thanks for playing!}--------"
                "------------------")
            break
        