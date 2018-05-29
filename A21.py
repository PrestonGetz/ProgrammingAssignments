#check how to read and open a file from A20

#create a function to count a specified word
#Please change the example words

def countWord(file, word):
    result = 0
    f = open(file)
    for line in f:
      if word in line:
        result += 1
    f.close()
    return result

part1=countWord('alice.txt','Alice')
part2=countWord('alice.txt','alice')
names=part1+part2
print(str(names))
