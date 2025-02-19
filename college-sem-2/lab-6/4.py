import operator
def sort_item(lst):
	lst.sort(key=operator.itemgetter(1))
	return lst

lst=[('banana',20),('apple',30),('orange',10),('mango',25),('pineapple',15)]

print(sort_item(lst))
