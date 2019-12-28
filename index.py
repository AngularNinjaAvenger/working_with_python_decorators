import functools

def blabla(level):
	# this level arguments is he the one passed to the decorator 
	def trigger(func):
		functools.wraps(func)
		def nodemon(arguments):
				# this method is where you recive the functions argument gongon
				return func(arguments)
		return nodemon
	return trigger;
	# the trigger element is the return of the blabla ie blabla("level")() <-- 
@blabla("level")
def get_node(arguments):
	print(arguments)

get_node("bishop")