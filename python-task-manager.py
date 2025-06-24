#take number of task with valid name,duration and priority from user
number_of_task = int(input("Enter the number of task you're working on: "))
#initiliaze an empty list
task = []


#initialize a counter and increment it after each itirration to break from the while loop when it reaches the condition. time complexity (O(n))
i=0

while i < number_of_task:
    name_of_task = str(input("Enter the name of the task: "))
    duration_of_task = float(input("Enter the duration of the task: "))
    priority_of_task = int(input("Enter the priority of the task (lower value means higher priority): "))
    #adding input to the list as a tupple
    task.append((priority_of_task,name_of_task,duration_of_task))
    #increment the counter
    i+=1

#function to insert a task
def insert(new_task:tuple):
    task.append(new_task)
    return task

#function to extract a task (O(n) time complexity)
def extract(remove_task:tuple):
    if not remove_task:
        return None
    for i in range(len(task)):
        if remove_task[1] == task[i][1]:
            task.pop(i)
    return task

#function to peek through the task
def peek(task:list):
    if not task:
        return None
    return "Your first task to complete is: " + str(task[0])

#function to check if the list is empty
def is_empty(task:list):
    if not task:
        return True
print(is_empty(task))

#function to complete the next task (O(n) in terms of time complexity)
def complete_next_task(task:list):
    if not task:
        return None
    highest_priority = 0
    for i in range(1,len(task)):
        if task[i][0] < task[highest_priority][0]:
            highest_priority = i
    return task.pop(highest_priority)

#function to search for a task. o(log n) in term of time complexity
def search_for_task(task:list,title:str):
    low = 0
    high = len(task) - 1 
    while low<=high:
        mid = (low+high)//2
        if task[mid][1] == title:
            return task[mid]
        elif title < task[mid][1]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 

#function to sort the list based on priority. O(n log n) time complexity
def sort_task(task:list):
    if len(task)<=1:
        return task
    mid = len(task)//2
    left = sort_task(task[:mid])
    right = sort_task(task[mid:])
    return merge(left,right)

#helper function for the sorting algorithm
def merge(left,right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i][0]<right[j][0]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result