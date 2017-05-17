if not exist groups\%2 (
	md groups\%2
)
if not exist groups\%2\%1-ans (
	md groups\%2\%1-ans
)
if not exist groups\%2\%1-task (
	md groups\%2\%1-task
)
if not exist archive\%2 (
	md archive\%2
)

move ans*.pdf groups\%2\%1-ans
move *.pdf groups\%2\%1-task