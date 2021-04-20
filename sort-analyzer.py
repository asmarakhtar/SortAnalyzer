# Sort Analyzer by Mr. V
def bubbleSort(anArray)
   n = len(anArray)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if anArray[j] > anArray[j+1] :
               anArray[j], anArray[j+1] = anArray[j+1], anArray[j]

def selectionsort(anArray):
   for i in range(len(anArray)-1):
    
     min = i
     for j in range(i+1, len(anArray)):
         if anArray[min] > anArray[j]:
            min = j
            
     anArray[i], anArray[min] = anArray[min], anArray[i]


def insertionSort(anArray):
 
   for i in range(1, len(anArray)):
        current = anArray[i]
       j = i-1
       while j >=0 and current < anArray[j] :
               anArray[j+1] = anArray[j]
               j -= 1
       anArray[j+1] = current



def main():
    # Load data files into variables
    randomData = loadDataArray("data-files/random-values.txt")
    reversedData = loadDataArray("data-files/reversed-values.txt")
    fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
    nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")

    # Test file load
    print(randomData[0:15])
    print(reversedData[0:15])
    print(fewUniqueData[0:15])
    print(nearlySortedData[0:15])

    # Main Menu
    loop = True
    while loop:
        # Print main menu and get user selection
        selection = mainMenu()

        # Process selection
        if (selection == "1"):
            print("\nBubble Sort Random Data")
            bubbleSort(randomData)
        elif (selection == "2"):
            print("\nBubble Sort Reversed Data")
            bubbleSort(reversedData)
        elif (selection == "3"):
            print("\nBubble Sort Few Unique Data")
            bubbleSort(fewUniqueData)
        elif (selection == "4"):
            print("\nBubble Sort Nearly Sorted Data")
            bubbleSort(nearlySortedData)
        elif (selection == "5"):
            print("\nSelection Sort Random Data")
            selectionsort(randomData)
        elif (selection == "6"):
            print("\nSelection Sort Reversed Data")
            selectionsort(reversedData)
        elif (selection == "7"):
            print("\nSelection Sort Few Unique Data")
            selectionsort(fewUniqueData)
        elif (selection == "8"):
            print("\nSelection Sort Nearly Sorted Data")
            selectionsort(nearlySortedData)
        elif (selection == "9"):
            print("\nInsertion Sort Random Data")
            insertionSort(randomData)
        elif (selection == "10"):
            print("\nInsertion Sort Reversed Data")
            insertionSort(reversedData)
        elif (selection == "11"):
            print("\nInsertion Sort Few Unique Data")
            insertionSort(fewUniqueData)
        elif (selection == "12"):
            print("\nInsertion Sort Nearly Sorted Data")
            insertionSort(nearlySortedData)
        elif (selection == "13"):
            loop = False
    # end while loop
    print("goodbye")
# end main()


def loadDataArray(fileName):
    # Return data from file as an array of integers.
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp
# end loadDataArray()


def mainMenu():
    # Print Main Menu
    print("\nMain Menu")
    print("1: Bubble Sort Random Data")
    print("2: Bubble Sort Reversed Data")
    print("3: Bubble Sort Few Unique Data")
    print("4: Bubble Sort Nearly Sorted Data")
    print("5: Selection Sort Random Data")
    print("6: Selection Sort Reversed Data")
    print("7: Selection Sort Few Unique Data")
    print("8: Selection Sort Nearly Sorted Data")
    print("9: Insertion Sort Random Data")
    print("10: Insertion Sort Reversed Data")
    print("11: Insertion Sort Few Unique Data")
    print("12: Insertion Sort Nearly Sorted Data")
    print("13: Exit")
    return input("Enter menu selection (1-13): ")
# end mainMenu()


# Call main() to begin program
main()
