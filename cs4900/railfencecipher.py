class RailFenceCipher:
    def __init__(self, depth):
        self.depth = depth

    def encrypt(self, plaintext):
        # this encryption method does not include the zigzag where characters would go, but it does not affect the
        # proper functionality because the letters in the rows would be the same.

        rows = [''] * self.depth
        current_row = 0
        # up or down direction
        direction = 1

        for char in plaintext:
            if char != ' ':  # Ignore spaces
                rows[current_row] += char

            current_row += direction
            if current_row == 0 or current_row == self.depth - 1:
                direction = -direction

        # concatenates all characters in a row to form one string (ciphertext)
        ciphertext = ''.join(rows)

        return ciphertext

    def decrypt(self, ciphertext):
        # 2d array
        rail = [['\n' for i in range(len(ciphertext))] for j in range(self.depth)]

        # direction
        direction = None
        row, col = 0, 0

        # diagonal where letters will go will temporarily be placed with *
        for i in range(len(ciphertext)):
            # has to go down direction when row is 0
            if row == 0:
                direction = True
            # cannot go down direction because no further rows below
            if row == self.depth - 1:
                direction = False

            # place the marker
            rail[row][col] = '*'
            col += 1

            # moves down if direction is true else it moves up a row
            if direction:
                row += 1
            else:
                row -= 1

        # start to fill in the diagonal with characters of the ciphertext
        index = 0
        for i in range(self.depth):
            for j in range(len(ciphertext)):
                if (rail[i][j] == '*') and (index < len(ciphertext)):
                    rail[i][j] = ciphertext[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(ciphertext)):
            # direction must go down if row is 0 or go up if lower boundary is reached (self.depth - 1)
            if row == 0:
                direction = True
            if row == self.depth - 1:
                direction = False
            # place the marker
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1
            if direction:
                row += 1
            else:
                row -= 1
        return ("".join(result))

    def rail_fence_display(self, plaintext):
        matrix = [['.' for _ in range(len(plaintext))] for _ in range(self.depth)]
        current_row = 0
        direction = 1

        for i, char in enumerate(plaintext):
            if char != ' ':
                matrix[current_row][i] = char
                current_row += direction
                if current_row == 0 or current_row == self.depth - 1:
                    direction = -direction

        # Add the top border (not part of the actual rail)
        top_border = ['-' for _ in range(len(plaintext))]
        matrix = [top_border] + matrix

        # Add the bottom border (not part of the actual rail)
        bottom_border = ['-' for _ in range(len(plaintext))]
        matrix.append(bottom_border)

        # Print the Rail Fence pattern
        for row in matrix:
            print(''.join(row))