class node(object):
	xxxProperties = None
	xxxBoundary = None
	
x = node
x.xxxProperties = "properties"
x.xxxBoundary = "boundary"

print x.("xxxProperties")