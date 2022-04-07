import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("--sort", help = 'Sort names in a specified file by length and alphabetical order', metavar="'FILENAME'", type = str)
group.add_argument("--rev", help = 'Sort names in a specified file by length and alphabetical order in reverse', metavar="'FILENAME'", type = str)
group.add_argument("--test", help = "'n' performs a normal sort test and 'r' performs a reverse sort test", metavar="'n', 'r'", type = str)

args = parser.parse_args()
	
def SortNormal(names):
        names.sort()
        names.sort(key=len)
        return names

def SortRev(names):
        rev = sorted(names, reverse=True)
        rev.sort(key = len, reverse=True)
        return rev

if args.sort:
        with open(str(args.sort)) as file:
                names = [line.rstrip() for line in file]
        names = SortNormal(names)
        for x in names:
                print(x)

elif args.rev:
        with open(args.rev) as file:
                names = [line.rstrip() for line in file]
        names = SortRev(names)
        for x in names:
                print(x)

elif args.test:

        if args.test == 'n':
                with open("Sorted Text.txt") as file:
                        testnames = [line.rstrip() for line in file]
                with open("Sort Me.txt") as file:
                        names = [line.rstrip() for line in file]

                names = SortNormal(names)

                same = True
                        
                if names != testnames:
                        same = False

                print("Sort Me.txt Output: ")
                
                for x in names:
                        print(x)
                print()
                        
                print("Sorted Text.txt Output: ")
                
                for x in testnames:
                        print(x)

                print()

                if same == False:
                        print("Outputs are not the same.")
                        
                else:
                        print("Outputs are the same.")

        elif args.test == 'r':
                with open("Sorted Text Rev.txt") as file:
                        testnames = [line.rstrip() for line in file]
                with open("Sort Me.txt") as file:
                        names = [line.rstrip() for line in file]

                names = SortRev(names)
                        
                same = True
                        
                if names != testnames:
                        same = False

                print("Sort Me.txt Output: ")
                
                for x in names:
                        print(x)

                print()
                        
                print("Sorted Text Rev.txt Output: ")
                
                for x in testnames:
                        print(x)

                print()

                if same == False:
                        print("Outputs are not the same.")
                        
                else:
                        print("Outputs are the same.")
                
           

