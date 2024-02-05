class FruitList: # parent class
    def __init__(self):
        self.fruits = []# empty list to store fruit list
    def add_new(self, fruit): # method to append new fruit
        self.fruits.append(fruit)
    def remove_fruits(self, fruit): # method to pop fruit
        self.fruits.remove(fruit)

    def display(self): # display the most updated list
        print(self.fruits)

class OrderedList(FruitList): # child class
    def add_new(self, fruit):
        """
        index = 0
        while index < len(self.fruits) and self.fruits[index] < fruit:
            index += 1
        self.fruits.insert(index, fruit)
    print("Ordered list:")"""
        value = 0

        for i in range(len(self.fruits)):# run the program within the range of the list
            # Iteration condition, new fruit is less than the length of the list and the new fruit is less than the current fruit
            while value< len(self.fruits) and self.fruits[value]< fruit:
                value +=1# move to the next element when the iteration is done
        self.fruits.insert(value, fruit)# insert the new fruit to the correct position
    print("Ordered list: ")


class UnorderedList(FruitList):
    pass

sort_list = OrderedList()
sort_list.add_new("Strawberry")
sort_list.add_new("Mango")
sort_list.add_new("Apple")
sort_list.add_new("Blueberry")
sort_list.remove_fruits("Mango")
sort_list.display()


unsort_list = UnorderedList()
unsort_list.add_new("Kiwi")
unsort_list.add_new("Blackberry")
unsort_list.add_new("Cherry")
unsort_list.add_new("Pineapple")
unsort_list.remove_fruits("Blackberry")
print("Unordered list: ")
unsort_list.display()


