'''
Subsetting lists of lists
50xp
You saw before that a Python list can contain practically anything; even other lists! To subset
lists of lists, you can use the same technique as before: square brackets. Try out the commands
in the following code sample in the IPython Shell:

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
x[2] results in a list, that you can subset again by adding additional square brackets.

What will house[-1][1] return? house, the list of lists that you created before, is already
defined for you in the workspace. You can experiment with it in the IPython Shell.

Possible Answers
A float: the kitchen area
A string: "kitchen"
A float: the bathroom area
A string: "bathroom"
'''

house = [['hallway', 11.25],
         ['kitchen', 18.0],
         ['living room', 20.0],
         ['bedroom', 10.75],
         ['bathroom', 9.5]]

# A float: the bathroom area

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

# First bracket signifies the column while second bracket signifies row which starts with index 0 each
print(x[2][0])
