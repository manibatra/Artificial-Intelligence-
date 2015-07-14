from simpleai.search import astar, SearchProblem

GOAL = '''1-2-3
4-5-6
7-8-e'''

INITIAL ='''4-1-2
7-e-3
8-5-6'''

def string_to_list(state):
	return [row.split('-') for row in state.split('\n')]

def find_location(state_list, element_to_find):
	for ir, row in enumerate(state_list):
		for ic, element in enumerate(row):
			if element == element_to_find:
				return ir, ic

def list_to_string(state_list):
	return '\n'.join(['-'.join(row) for row in state_list])

goal_pos = {}
goal_list = string_to_list(GOAL)
for number in '12345678e':
	goal_pos[number] = find_location(goal_list, number)
	print goal_pos[number]

class EightPuzzleProblem(SearchProblem):
	def actions(self, state):
		actions = []
		state_list = string_to_list(state)
		row_e, col_e = find_location(state_list, 'e')

		if row_e > 0:
			actions.append(state_list[row_e-1][col_e])
		if row_e < 2:
			actions.append(state_list[row_e+1][col_e])
		if col_e > 0:
			actions.append(state_list[row_e][col_e-1])
		if col_e < 2:
			actions.append(state_list[row_e][col_e+1])

		return actions

	def result(self, state, action):
		state_list = string_to_list(state)
		row_e, col_e = find_location(state_list, 'e')
		row_a, col_a = find_location(state_list, action)

		state_list[row_e][col_e], state_list[row_a][col_a] = state_list[row_a][col_a], state_list[row_e][col_e]

		return list_to_string(state_list)

	def is_goal(self, state):
		return state == GOAL

	def cost(self, state, action, state2):
		return 1

	def heuristic(self, state):

		distance = 0

		state_list = string_to_list(state)

		for number in '12345678e':
			row_s, col_s = find_location(state_list, number)
			row_g, col_g = goal_pos[number]
			distance += abs(row_s - row_g) + abs(col_s - col_g)

		return distance

result = astar(EightPuzzleProblem(INITIAL))

for action, state in result.path():
	print ('Move number', action)
	print (state)

