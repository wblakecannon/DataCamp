'''
Slicing and dicing (2)
100xp
In the video, Filip first discussed the syntax where you specify both where to begin and end the
slice of your list:

my_list[begin:end]
However, it's also possible not to specify these indexes. If you don't specify the begin index,
Python figures out that you want to start your slice at the beginning of your list. If you don't
specify the end index, the slice will go all the way to the last element of your list. To experiment
with this, try the following commands in the IPython Shell:

x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]

Instructions
Use slicing to create the lists downstairs and upstairs again, but this time without using indexes
if it's not necessary. Remember downstairs is the first 6 elements of areas and upstairs is the last
4 elements of areas.
'''
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room",
         20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]
print(downstairs)

# Alternative slicing to create upstairs
# Search index starts from 0 from the very left hand side
upstairs = areas[6:]
