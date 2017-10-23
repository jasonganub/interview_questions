board = [
['0', '0', '0', '0', '0', '0', '1', '0'],
['0', '0', '1', '0', '0', '1', '0', '0'],
['0', '0', '0', '0', '0', '0', '0', '0'],
['0', '0', '1', '0', '0', '0', '1', '0'],
['0', '0', '0', '1', '0', '0', '0', '0'],
['0', '0', '0', '1', '0', '1', '0', '0']
]

r = len(board)
c = len(board[0])

i = 0
j = 0
end = False
move = 4

# if move == 1, go down
# if move == 2, go left
# if move == 3, go up
# if move == 4, go right
# reset move to 1

while end == False:
    print("{},{}".format(i, j))
    if i < 0 or i > r-1:
        print("exited wall at {},{}".format(i-1,j))
        end = True
        break
    if j < 0 or j > c-1:
        print("exited wall at {},{}".format(i,j-1))
        end = True
        break

    if board[i][j] == '1':
        if move < 4:
            move += 1
        else:
            move = 1

    if move == 1:
        i+=1
    elif move == 2:
        j-=1
    elif move == 3:
        i-=1
    elif move == 4:
        j+=1


# if it's up, decrement i
# if it's down, increment i
# if it's right, increment j
# if it's left, decrement j
