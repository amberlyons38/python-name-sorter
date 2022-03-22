with open("Sort Me.txt") as file:
        names = [line.rstrip() for line in file]

	
names.sort()
def SortByLen(names):
        names.sort(key=len)
        return names

names = SortByLen(names)
for x in names:
        print(x)

