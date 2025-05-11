import one

print("TOP LEVEL IN TWO.PY")
	
# This is to call the main python script's func()
one.func()

if __name__ == '__main__':

	print("TWO.PY is being run directly!")

else:
	print('TWO.PY has been imported!')


''' 
When we run this, we see that it goes into one.py first but doesn't treat it as if it is the main one
It tells that it has been imported instead

'''

