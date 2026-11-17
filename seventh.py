
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            moves = [(row + 1, col)]
        else:
            moves = [(row - 1, col)]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for i in range(1, 8):
            moves.extend([
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ])

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for i in range(1, 8):
            moves.extend([
                (row + i, col),
                (row - i, col),
                (row, col + i),
                (row, col - i)
            ])

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for i in range(1, 8):
            moves.extend([
                (row + i, col),
                (row - i, col),
                (row, col + i),
                (row, col - i),
                (row + i, col + i),
                (row + i, col - i),
                (row - i, col + i),
                (row - i, col - i)
            ])

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position

        moves = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col + 1),
            (row - 1, col - 1)
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())

    pawn_white = Pawn("white", (2, 4))
    print(pawn_white)
    print(pawn_white.possible_moves())

    pawn_black = Pawn("black", (7, 4))
    print(pawn_black)
    print(pawn_black.possible_moves())

    bishop = Bishop("white", (4, 4))
    print(bishop)
    print(bishop.possible_moves())

    rook = Rook("black", (1, 1))
    print(rook)
    print(rook.possible_moves())

    queen = Queen("white", (4, 4))
    print(queen)
    print(queen.possible_moves())

    king = King("black", (8, 8))
    print(king)
    print(king.possible_moves())
