name = "tongchun"	# type 'str'
age = 42			# type 'int'
height = 176.5		# type 'float'
married = True		# type 'bool'

# Old Style String Formatting
message = "My name is %s. Age is %d. Height is %0.1f. He is married (%r)" % (name, age, height, married)
print(message)
# My name is tongchun. Age is 42. Height is 176.5. He is married (True)