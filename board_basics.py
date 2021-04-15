from skimage.metrics import structural_similarity


class Board_basics:
    def __init__(self, side_view_compensation):
        self.d = [side_view_compensation, (0, 0)]

    def get_square_image(self, row, column,
                         board_img):
        height, width = board_img.shape[:2]
        minX = int(column * width / 8)
        maxX = int((column + 1) * width / 8)
        minY = int(row * height / 8)
        maxY = int((row + 1) * height / 8)
        square = board_img[minY:maxY, minX:maxX]
        return square

    def convert_row_column_to_square_name(self, row, column):
        number = repr(8 - row)
        letter = str(chr(97 + column))
        return letter + number

    def square_region(self, row, column):
        region = set()
        for d_row, d_column in self.d:
            n_row = row + d_row
            n_column = column + d_column
            if not (0 <= n_row < 8):
                continue
            if not (0 <= n_column < 8):
                continue
            region.add((n_row, column))
        return region

    def get_potential_moves(self, fgmask, previous_frame, next_frame):
        board = [[self.get_square_image(row, column, fgmask).mean() for column in range(8)] for row in range(8)]
        previous_board = [[self.get_square_image(row, column, previous_frame) for column in range(8)] for row in
                          range(8)]
        next_board = [[self.get_square_image(row, column, next_frame) for column in range(8)] for row in
                      range(8)]
        potential_squares = []
        for row in range(8):
            for column in range(8):
                score = board[row][column]
                if score < 10.0:
                    continue
                potential_squares.append((score, row, column))

        potential_squares.sort(reverse=True)
        potential_squares = potential_squares[:4]
        potential_moves = []

        for start_square_score, start_row, start_column in potential_squares:
            start_region = self.square_region(start_row, start_column)
            for arrival_square_score, arrival_row, arrival_column in potential_squares:
                if (start_row, start_column) == (arrival_row, arrival_column):
                    continue
                ssim_start = structural_similarity(next_board[start_row][start_column],
                                                   previous_board[start_row][start_column], multichannel=True)
                ssim_arrival = structural_similarity(next_board[arrival_row][arrival_column],
                                                     previous_board[arrival_row][arrival_column], multichannel=True)
                if ssim_start > 0.8 or ssim_arrival > 0.8:
                    continue
                arrival_region = self.square_region(arrival_row, arrival_column)
                region = start_region.union(arrival_region)
                total_square_score = sum(
                    board[row][column] for row, column in region) + start_square_score + arrival_square_score
                start_square_name = self.convert_row_column_to_square_name(start_row, start_column)
                arrival_square_name = self.convert_row_column_to_square_name(arrival_row, arrival_column)
                potential_moves.append(
                    (total_square_score, start_square_name, arrival_square_name))

        potential_moves.sort(reverse=True)

        for i in range(len(potential_squares)):
            score, row, column = potential_squares[i]
            potential_squares[i] = (score, self.convert_row_column_to_square_name(row, column))

        return potential_squares, potential_moves
