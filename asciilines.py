import sys
filename = ''

if len(sys.argv) < 2:
    print("Please specify a TVG file to process")
    sys.exit()
else:
    filename = sys.argv[1]
with open(filename) as f:
    infile = f.readlines()

infile = [x.strip() for x in infile] 

size = infile[0].split()
size_row = int(size[0])
size_col = int(size[1])

canvas = [['.'] * size_col for i in range(size_row)]


for line in infile[1:]:
    token = line.split()
    if len(token):
        char = token[0]
        row = int(token[1])
        if row < 0:
            row = 0
        col = int(token[2])
        if col < 0:
            col = 0
        direct = token[3]
        length = int(token[4])

        if direct == 'h':
            for i in range(col, col + length):
                if i < size_col: 
                    canvas[row][i] = char
        elif direct == 'v':
            for j in range(row, row + length):
                if j < size_row: 
                    canvas[j][col] = char
for i in range(size_row):
    for j in range(size_col):
        print(canvas[i][j], end = '')
    print('')
