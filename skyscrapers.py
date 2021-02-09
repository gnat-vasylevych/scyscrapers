def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    """
    result = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.replace('\n', '')
            result.append(line)
    return result


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    # >>> left_to_right_check("412453*", 4)
    True
    # >>> left_to_right_check("452453*", 5)
    False
    """
    check = 0
    temp = 0
    for number in input_line[1:-1]:
        if int(number) > temp:
            check += 1
            temp = int(number)
    if check >= pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    # >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    # >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    # >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        for elem in line:
            if elem == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    # >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    # >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    # >>> check_uniqueness_in_rows(['***212*', '412453*', '423145*', '*543215', '*35214*', '441532*', '*22222*'])
    False
    """
    for line in board[1:-1]:
        line = line[1:-1]
        line = line.replace('*', '')
        if len(set(line)) != len(line):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    # >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    # >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    # >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        if line[0] != '*':
            if not left_to_right_check(line, int(line[0])):
                return False
        if line[-1] != '*':
            if not left_to_right_check(line[::-1], int(line[-1])):
                return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    # >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    # >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    # >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    inverse_board = []
    for index in range(7):
        temp = ""
        for line in board:
            temp += line[index]
        inverse_board.append(temp)

    return check_uniqueness_in_rows(inverse_board) and check_horizontal_visibility(inverse_board)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """
    board = read_input(input_path)
    if check_not_finished_board(board):
        if check_uniqueness_in_rows(board):
            if check_horizontal_visibility(board):
                if check_columns(board):
                    return True
    return False


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
