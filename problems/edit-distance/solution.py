class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        sol = [
            [0 for i in range(len(word1) + 1)]
                for j in range(len(word2) + 1)
                ]
        
        for i in range(len(word1) + 1):
            sol[len(word2)][i] = len(word1) - i
        for i in range(len(word2) + 1):
            sol[i][len(word1)] = len(word2) - i

        for j in range(len(word2) - 1, -1, -1):
            for i in range(len(word1) - 1, -1, -1):
                if word1[i] == word2[j]:
                    sol[j][i] = sol[j + 1][i + 1]
                else:
                    sol[j][i] = 1 + min(sol[j + 1][i], sol[j][i + 1], sol[j + 1][i + 1])
        return sol[0][0]
