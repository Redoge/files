#Redoge
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
input_list = list(map(int, input("Enter your unordered list:  ").split()))
insertion_sort(input_list)
out_line = ""
for i in range(len(input_list)): out_line += str(input_list[i]) + ' '
print ("Your ordered list: ", out_line)
