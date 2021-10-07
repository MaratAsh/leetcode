class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		def predict_index(curr_row, curr_column, rows, columns):
			predicted = set()
			if (curr_row > 0):
				predicted.add((curr_row - 1, curr_column))
			if (curr_row < rows - 1):
				predicted.add((curr_row + 1, curr_column))
			if (curr_column > 0):
				predicted.add((curr_row, curr_column - 1))
			if (curr_column < columns - 1):
				predicted.add((curr_row, curr_column + 1))
			return predicted
		
		def fuzz(curr_r, curr_c, used_indxs, word):
			if (len(word) == 0):
				return True
			indxs = predict_index(curr_r, curr_c, row_l, column_l)
			for indx in filter(lambda indx: indx not in used_indxs, indxs):
				if (word[0] == board[indx[0]][indx[1]]):
					if (word[1::]):
						temp_used_indxs = set(used_indxs)
						temp_used_indxs.add(indx)
						res = fuzz(indx[0], indx[1], temp_used_indxs, word[1::])
						if (res):
							return True
					else:
						return True
			return False
			
		row_l = len(board)
		column_l = len(board[0])
		
		for row_id in range(row_l):
			for column_id in range(column_l):
				if (board[row_id][column_id] == word[0]):
					res = fuzz(row_id, column_id, {(row_id, column_id)}, word[1::])
					if (res or len(word) == 1):
						return True
		return False
