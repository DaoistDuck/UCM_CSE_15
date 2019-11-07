from logic import TruthTable
#problem 1

#and
myTable = TruthTable(['a','b'],['a and b'])
myTable.display()
print(" ")

#or
myTable = TruthTable(['a','b'],['a or b'])
myTable.display()
print(" ")

#not
myTable = TruthTable(['a'],['-a'])
myTable.display()
print(" ")

#right arrow
myTable = TruthTable(['a','b'],['a -> b'])
myTable.display()
print(" ")

#leftandrightarrow
myTable = TruthTable(['a','b'],['a <-> b'])
myTable.display()
print(" ")


#problem 2
inputProposition1 = input("Enter proposition 1: ")
inputProposition2 = input("Enter proposition 2: ")

myTable = TruthTable(['p','q'],[inputProposition1 , inputProposition2])
tableList = myTable.table
checkValue = 0
for row in tableList:
    propositionList = row[-1]
    if(propositionList[0] != propositionList[1]):
        checkValue = 1
print(" ")
if(checkValue == 0):
    print("The propositions are equivalent")
else:
    print("The propositions are not equivalent")