# One.py

# In Python, we do not have a main() function that acts as our start point
print("Hello")

# What Python does in the background
# Python assigns the module as the main the one is focus running
# What Python does is that it assigns the script that we actually ran on the command line as the main one
# There by it allows us to check if the current running file is the main one

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

def function():
	pass

def function2():
	pass

# This can be used to control the entire program flow that is, we can use this to only execute certain functions if it is he one actually running and not just being imported!
if __name__ == '__main__':
	# RUN THE SCRIPT!
	function2()
	function()

'''
if __name__ == '__main__':
	# If One.py is the main file 
	print('ONE.PY is being run directly!')
else:
	# If one.py has been imported
	print('ONE.PY has been imported')
'''