numbers=input("Input your list of numbers:\n")
number_list=numbers.split()
numbers=[s for s in number_list if s.isdigit()]
numberlist=[]
numbers=[int(i) for i in numbers]
numbers=sorted(numbers)
class Math():
    def __init__(self,numbers):
        self.numbers=numbers
    def findmean(self,numbers):
            mean=round((sum(numbers)/len(numbers)),1)
            return mean
    def findmedian(self,numbers):
        oddeven=0
        for x in numbers:
            oddeven+=1
        if oddeven%2==0:
            even1=(oddeven/2)-1
            even2=even1+1
            if numbers[int(even1)]==numbers[int(even2)]:
                median=numbers[int(even1)]
            else:
                median=[numbers[int(even1)],numbers[int(even1)]]
        if oddeven%2!=0:
            even=(oddeven/2)-0.5
            median=numbers[int(even)]
        return median
    def findmode(self,numbers):
        mode=round(max(set(numbers),key=numbers.count),1)
        return mode
print()
a=Math(numbers)
print('mean:',a.findmean(numbers))
print('median:',a.findmedian(numbers))
print('mode:',a.findmode(numbers))
