class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        removable = {'A': 0, 'B': 0}
        prev_color = prev_prev_color = None
        for color in colors:
            if prev_color == prev_prev_color == color:
                removable[color] += 1
            prev_prev_color = prev_color
            prev_color = color
        return removable['A'] > removable['B']
