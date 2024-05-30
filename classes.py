import random

class Lecture:
    def __init__(self, name, length, professor, wishlist_position,category):
        self.name = name
        self.length = length
        if professor is None:
            print("Class:", name, "has no professor")
            exit()
        self.professor = professor
        self.wishlist_position = wishlist_position
        self.rating = 0
        self.category = category

    # Calculates the difficulty rating of scheduling the lecture
    def calculate_rating(self, occurrences, available_days, heatmaps, pos):
        if occurrences == 0 or available_days is None:
            self.rating = 1000
        else:
            self.rating = len(available_days) - occurrences + (1 / self.wishlist_position) + (heatmaps[self.category][pos-1] * 10)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def link(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def sort(self,x,y):
        # Nothing to do if x and y are same
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.value.rating != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.value.rating != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return

        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # Else make y as new head
            self.head = currY

            # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # Else make x as new head
            self.head = currX

            # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def bubbleSort(self):
        count = 0
        start = self.head
        while start != None:
            count += 1
            start = start.next

        # Traverse through all nodes of linked list
        for i in range(0, count):

            # Last i elements are already in place
            start = self.head
            while start != None:

                # Swap adjacent nodes
                ptr = start.next
                if ptr != None:
                    if start.value.rating > ptr.value.rating:
                        self.sort(start.value.rating, ptr.value.rating)

                start = start.next

    def sorting_lectures(self, professors, heatmaps, pos):
        current = self.head

        while current is not None:
            current.value.calculate_rating(professors[current.value.professor].occurrences,
                                                   professors[current.value.professor].available_days, heatmaps, pos)
            current = current.next

        self.bubbleSort()

    def sorting_days(self,scheduled_days):
        current = self.head

        while current is not None:
            current.value.update_rating(scheduled_days)
            current = current.next
        self.bubbleSort()

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp.value

    def remove(self, value):
        if self.head.value is value:
            return self.pop()

        current_node = self.head
        prev = self.head
        while current_node is not None:
            if current_node.value is value:
                val = current_node.value
                prev.next = current_node.next
                return val
            prev = current_node
            current_node = current_node.next


class Day:
    def __init__(self, date, available_profs, pos):
        self.date = date
        self.available_profs = available_profs
        self.lecture = None
        self.pos = pos
        self.rating = available_profs

    def update_rating(self,scheduled_days):
        self.available_profs = self.available_profs - scheduled_days[self.pos -1]
        self.rating = self.available_profs + (self.pos/100)



class Professor:
    def __init__(self, name, lectures, available_days):
        self.name = name
        self.lectures = lectures
        self.available_days = available_days
        self.occurrences = 0

    def add_occurrences(self,length):
        self.occurrences = self.occurrences + length

    def remove_occurrence(self,length):
        self.occurrences = self.occurrences - length


class Course:
    def __init__(self, lectures, days, sessions,no_categories):
        self.lectures = lectures
        self.days = days
        self.scheduled = []
        self.not_scheduled = []
        self.heatmaps = []
        for category in range(0,no_categories):
            heatmap = [0] * sessions
            self.heatmaps.append(heatmap)


    def heating(self,pos,category):
        i = - 3
        while i != 3:
            if 0 <= pos + i < len(self.heatmaps):
                self.heatmaps[category][pos + i] = self.heatmaps[category][pos + i] + 1
            i = i + 1

