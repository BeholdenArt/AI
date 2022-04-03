from collections import defaultdict


# jug1, jug2, aim = 4, 3, 2
jug1, jug2, aim = 5, 10, 2
print(f"Jug1 capacity: {jug1}, Jug2 capacity: {jug2}, Aim: {aim}")

visited = defaultdict(lambda: False)


def waterJugSolver(amt1, amt2):

	# returns true if achieved.
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True
	
	# Checks if we have already visited the
	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		# Changes the boolean value of
		visited[(amt1, amt2)] = True
	
		# Check for all the 6 possibilities and
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	else:
		return False

print("Steps: ")

waterJugSolver(0, 0)
