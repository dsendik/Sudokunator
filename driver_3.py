#!/usr/bin/env python
#coding:utf-8
import random
import time as time
import os

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"
myRowDict = []
myColDict = []
myBoxDict = []
traversal = []
mylist = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
          'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
          'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
          'D1', 'D2', 'D3', 'D4', 'D5', 'E6', 'D7', 'D8', 'D9',
          'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
          'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
          'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'
          ]
mylist.reverse()
empties = []


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]



def split_dict_equally(input_dict, chunks=2):
    "Splits dict by keys. Returns a list of dictionaries."
    # prep with empty dicts
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in input_dict.items():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list


def makeColDict(board):
    myColDict = split_dict_equally(board, 9)
    return myColDict


def makeRowDict(board, myRowDict):
    rowDict1 = {k: board[k] for k in
                board.keys() & {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                                'A9'}}
    rowDict2 = {k: board[k] for k in
                board.keys() & {'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
                                'B9'}}
    rowDict3 = {k: board[k] for k in
                board.keys() & {'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
                                'C9'}}
    rowDict4 = {k: board[k] for k in
                board.keys() & {'D1', 'D2', 'D3', 'D4', 'D5', 'E6', 'D7', 'D8',
                                'D9'}}
    rowDict5 = {k: board[k] for k in
                board.keys() & {'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
                                'E9'}}
    rowDict6 = {k: board[k] for k in
                board.keys() & {'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                                'F9'}}
    rowDict7 = {k: board[k] for k in
                board.keys() & {'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
                                'G9'}}
    rowDict8 = {k: board[k] for k in
                board.keys() & {'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8',
                                'H9'}}
    rowDict9 = {k: board[k] for k in
                board.keys() & {'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8',
                                'I9'}}
    if len(myRowDict) <= 9:
        myRowDict.append(rowDict1)
        myRowDict.append(rowDict2)
        myRowDict.append(rowDict3)
        myRowDict.append(rowDict4)
        myRowDict.append(rowDict5)
        myRowDict.append(rowDict6)
        myRowDict.append(rowDict7)
        myRowDict.append(rowDict8)
        myRowDict.append(rowDict9)
    else:
        myRowDict[0] = rowDict1
        myRowDict[1] = rowDict2
        myRowDict[2] = rowDict3
        myRowDict[3] = rowDict4
        myRowDict[4] = rowDict5
        myRowDict[5] = rowDict6
        myRowDict[6] = rowDict7
        myRowDict[7] = rowDict8
        myRowDict[8] = rowDict9


    return myRowDict

def makeBoxdict(board, myBoxDict):

    boxDict1 = {k: board[k] for k in
                board.keys() & {'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2',
                                'C3'}}
    boxDict2 = {k: board[k] for k in
                board.keys() & {'A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5',
                                'C6'}}
    boxDict3 = {k: board[k] for k in
                board.keys() & {'A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8',
                                'C9'}}
    boxDict4 = {k: board[k] for k in
                board.keys() & {'D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2',
                                'F3'}}
    boxDict5 = {k: board[k] for k in
                board.keys() & {'D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5',
                                'F6'}}
    boxDict6 = {k: board[k] for k in
                board.keys() & {'D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8',
                                'F9'}}
    boxDict7 = {k: board[k] for k in
                board.keys() & {'G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2',
                                'I3'}}
    boxDict8 = {k: board[k] for k in
                board.keys() & {'G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5',
                                'I6'}}
    boxDict9 = {k: board[k] for k in
                board.keys() & {'G7', 'G8', 'G9', 'H7', 'H8', 'H6', 'I7', 'I8',
                                'I9'}}

    if len(myBoxDict) <= 9:
        myBoxDict.append(boxDict1)
        myBoxDict.append(boxDict2)
        myBoxDict.append(boxDict3)
        myBoxDict.append(boxDict4)
        myBoxDict.append(boxDict5)
        myBoxDict.append(boxDict6)
        myBoxDict.append(boxDict7)
        myBoxDict.append(boxDict8)
        myBoxDict.append(boxDict9)
    else:
        myBoxDict[0] = boxDict1
        myBoxDict[1] = boxDict2
        myBoxDict[2] = boxDict3
        myBoxDict[3] = boxDict4
        myBoxDict[4] = boxDict5
        myBoxDict[5] = boxDict6
        myBoxDict[6] = boxDict7
        myBoxDict[7] = boxDict8
        myBoxDict[8] = boxDict9

    return myBoxDict


def update(board, row, box):
    myRowDict = makeRowDict(board, row)
    myColDict = makeColDict(board)
    myBoxDict = makeBoxdict(board, box)


def getCurrRow(each):
    if each[0] == 'A': return 0
    if each[0] == 'B': return 1
    if each[0] == 'C': return 2
    if each[0] == 'D': return 3
    if each[0] == 'E': return 4
    if each[0] == 'F': return 5
    if each[0] == 'G': return 6
    if each[0] == 'H': return 7
    if each[0] == 'I': return 8


# def getCurrRow(each):
#     if each == 0: return 'A'
#     if each == 1: return 'B'
#     if each == 2: return 'C'
#     if each == 3: return 'D'
#     if each == 4: return 'E'
#     if each == 5: return 'F'
#     if each == 6: return 'G'
#     if each == 7: return 'H'
#     if each == 0: return 'I'



def getCurrBox(each):
    if each == 'A1' or each == 'A2' or each == 'A3' \
            or each == "B1" or each == "B2" or each == "B3" \
            or each == "C1" or each == "C2" or each == "C3":
        return 0
    if each == "A4" or each == "A5" or each == "A6" \
            or each == "B4" or each == "B5" or each == "B6" \
            or each == "C4" or each == "C5" or each == "C6":
        return 1
    if each == "A7" or each == "A8" or each == "A9" \
            or each == "B7" or each == "B8" or each == "B9" \
            or each == "C7" or each == "C8" or each == "C9":
        return 2
    if each == "D1" or each == "D2" or each == "D3" \
            or each == "E1" or each == "E2" or each == "E3" \
            or each == "F1" or each == "F2" or each == "F3":
        return 3
    if each == "D4" or each == "D5" or each == "D6" \
            or each == "E4" or each == "E5" or each == "E6" \
            or each == "F4" or each == "F5" or each == "F6":
        return 4
    if each == "D7" or each == "D8" or each == "D9" \
            or each == "E7" or each == "E8" or each == "E9" \
            or each == "F7" or each == "F8" or each == "F9":
        return 5
    if each == "G1" or each == "G2" or each == "G3" \
            or each == "H1" or each == "H2" or each == "H3" \
            or each == "I1" or each == "I2" or each == "I3":
        return 6
    if each == "G4" or each == "G5" or each == "G6" \
            or each == "H4" or each == "H5" or each == "H6" \
            or each == "I4" or each == "I5" or each == "I6":
        return 7
    if each == "G7" or each == "G8" or each == "G9" \
            or each == "H7" or each == "H8" or each == "H9" \
            or each == "I7" or each == "I8" or each == "I9":
        return 8


def inBox(board, boxRow, boxCol, val):
    for iter in range(0, 3):
        for j in range(0, 3):
            if (board[iter + boxRow][j + boxCol] == val):
                return True
    return False


def is_safe(board, row, column, val):
    box = [row - row % 3, int(column) - int(column) % 3]
    for iter1 in range(9):
        if board[row][iter1] == val:
            return False
    for iter2 in range(9):
        if board[iter2][int(column)] == val:
            return False
    if inBox(board, box[0], box[1], val):
        return False
    return True


def isEmpty(board, l, unassigned, domain, listGrid):
    # index = mrv(listGrid, board)
    for row in range(9):
        for col in range(9):
            # newRow = getCurrRow(index)

            if listGrid[row][col] == 0:
                empties.append(str(row) + str(col))
                l[0] = row
                l[1] = col
                return False
    return True


def convertToList(board):
    listConversion = []
    listGrid = []
    for each in board:
        listConversion.append(board[each])
    listGrid = list(chunks(listConversion, 9))
    i = 0
    return listGrid


def random_items(iterator, items_wanted=9):
    selected_items = [None] * items_wanted

    for item_index, item in enumerate(iterator):
        for selected_item_index in range(items_wanted):
            if not random.randint(0, item_index):
                selected_items[selected_item_index] = item

    return selected_items

#
# def mrv(domain, unassigned):
#     minIdx, minVal = -1, float('inf')
#     for i in unassigned:
#         if len(domain[i]) < minVal:
#             minVal = len(domain[i])
#             minIdx = i
#     return minIdx
#

# # my mrv first gives a score to each column and each row, then combines these scores to give a score to each square
# # it then send the location of the lowest score as the first grid square to fill in
# def mrv(listGrid, board):
#     i = 0
#     myColumn = makeColDict(board)
#     newColumn = []
#     squareValsCol = []
#     finalSquareVals = []
#     boardWithScores = {}
#     for each in myColumn:
#         newColumn.append(list(each.values()))
#     squareVals = []
#
#     for each in newColumn:
#         myVal = sum(each)
#         squareValsCol.append(myVal)
#         myVal = each[0]
#     for each in listGrid:
#         myVal = sum(each)
#         squareVals.append(myVal)
#         myVal = each[0]
#     for rowNum in range(9):
#         for colNum in range(9):
#             finalSquareVals.append(squareVals[rowNum]+squareValsCol[colNum])
#     k = 0
#     for each in board:
#         boardWithScores[each] = finalSquareVals[k]
#         k+=1
#         minVal = 2**10000
#         minLocation = ""
#     for eachVal in boardWithScores:
#         if boardWithScores[eachVal] < minVal:
#             minVal = boardWithScores[eachVal]
#             minLocation = eachVal
#     result = minLocation
#     boardWithScores.__delitem__(minLocation)
#     return result


def backtracking(listGrid, board):
    """Takes a board and returns solved board."""
    start = time.time()
    emptiesList = [0, 0]
    domain = {}
    emptiesList2 = []
    # for each in board:
    #     emptiesList2.append(each)
    # for each in board:
    #     if board[each] != 0:
    #         domain[each] = set([board[each]])
    #         emptiesList2.remove(each)
    #     else:
    #         domain[each] = set(range(1, 10))
    # index = mrv(listGrid, board)

    if isEmpty(board, emptiesList, emptiesList2, domain, listGrid):
        return True

    row = emptiesList[0]
    col = emptiesList[1]
    # print(empties)
    # newRow = getCurrRow(index)
    for n in range(10):
        # for n in range(10):
        if is_safe(listGrid, row, col, n):
            listGrid[row][col] = n
            # print_board(board)
            if backtracking(listGrid, board):
                return listGrid
            listGrid[row][col] = 0
    return False


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

    solved_board = board
    return solved_board

def convertToDict(boardList):
    myVals = ""
    myDict = {}
    for each in boardList:
        for val in each:
            myVals = myVals+str(val)
    board = {ROW[r] + COL[c]: int(myVals[9 * r + c])
             for r in range(9) for c in range(9)}
    return board



if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")
    # Solve each board using backtracking
    i = 0
    for line in sudoku_list.split("\n"):
        # print("trying to solve # " + str(i))
        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = {ROW[r] + COL[c]: int(line[9*r+c])
                 for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        # print_board(board)
        boardList = convertToList(board)
        # Solve with backtracking
        start = time.time()
        solved_board = backtracking(boardList, board)
        solved_board = convertToDict(boardList)
        # Print solved board. TODO: Comment this out when timing runs.

        i+=1
        outfile.write(board_to_string(solved_board))
        print("solved board:")
        print_board(solved_board)
        outfile.write('\n')
        end = time.time()
        # print("solved " + str(i) + " in " + str(end - start))
