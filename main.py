from workplace import movieTickets
import sys

# dont touch this stuff 

taskNum = 7
numtasks = 4
variables = {}
perfect = True

for i in range(1, numtasks+1):
  testCase = open(("TestCases/testCase" + str(i) + ".py"), "r").readlines()

  print("---------- test" + str(i) + " ----------")
  variables["t{0}t".format(i)] = open(("TaskResults/task" + str(i) + "Test.py"), "r").read()

  # function name - - - - - - - ->
  variables["t{0}a".format(i)] = movieTickets(testCase)

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("|         Success         |")
  else:
    print("|       You failed.       |")
    perfect = False

print("---------------------------")

if perfect == True:
  print("\nCongratulations! You successfully completed PPSC_task_" + str(taskNum))
