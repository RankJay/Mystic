class modularOperations:
  def cModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.c","w+")
      f.write("/*\n#include<stdio.h>\nvoid quicksort(int number[25],int first,int last)\n{\n\tint i, j, pivot, temp;\n\n\n\tif(first<last)\n\t{\n\t\tpivot=first;\n\t\ti=first;\n\t\tj=last;\n\n\t\twhile(i<j)\n\t\t{\n\t\t\twhile(number[i]<=number[pivot] && i<last)\n\t\t\t\ti++;\n\t\t\twhile(number[j]>number[pivot])\n\t\t\t\tj--;\n\t\t\tif(i<j)\n\t\t\t{\n\t\t\t\ttemp=number[i];\n\t\t\t\tnumber[i]=number[j];\n\t\t\t\tnumber[j]=temp;\n\t\t\t}\n\t\t}\n\n\t\ttemp=number[pivot];\n\t\tnumber[pivot]=number[j];\n\t\tnumber[j]=temp;\n\t\tquicksort(number,first,j-1);\n\t\tquicksort(number,j+1,last);\n\n\t}\n}*/")
      f.close
      function = 'quicksort(number,0,count-1);'
      return str(function)

  def cPlusModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.cpp","w+")
      f.write("/*\n#include<stdio.h>\nvoid quicksort(int number[25],int first,int last)\n{\n\tint i, j, pivot, temp;\n\n\n\tif(first<last)\n\t{\n\t\tpivot=first;\n\t\ti=first;\n\t\tj=last;\n\n\t\twhile(i<j)\n\t\t{\n\t\t\twhile(number[i]<=number[pivot] && i<last)\n\t\t\t\ti++;\n\t\t\twhile(number[j]>number[pivot])\n\t\t\t\tj--;\n\t\t\tif(i<j)\n\t\t\t{\n\t\t\t\ttemp=number[i];\n\t\t\t\tnumber[i]=number[j];\n\t\t\t\tnumber[j]=temp;\n\t\t\t}\n\t\t}\n\n\t\ttemp=number[pivot];\n\t\tnumber[pivot]=number[j];\n\t\tnumber[j]=temp;\n\t\tquicksort(number,first,j-1);\n\t\tquicksort(number,j+1,last);\n\n\t}\n}*/")
      f.close
      function = 'quicksort(number,0,count-1);'
      return str(function)
  
  def pythonModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.py","w+")
      f.write("'''\ndef partition(arr,low,high):\n\ti = ( low-1 )\n\tpivot = arr[high]\n\n\tfor j in range(low , high):\n\t\tif arr[j] < pivot:\n\t\t\ti = i+1\n\t\t\tarr[i],arr[j] = arr[j],arr[i]\n\tarr[i+1],arr[high] = arr[high],arr[i+1]\n\treturn ( i+1 )\n\ndef quickSort(arr,low,high):\n\tif low < high:\n\t\tpi = partition(arr,low,high)\n\t\tquickSort(arr, low, pi-1)\n\t\tquickSort(arr, pi+1, high) \n\narr = [float(x) for x in input().split()] \nn = len(arr)\n'''\n")
      f.close
      function = 'quickSort(arr,0,n-1)\noutput=arr'
      return str(function)
  
  def javaModularOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.java","w+")
      f.write("    /*\n\tint partition(int arr[], int low, int high) \n\t{ \n\t\tint pivot = arr[high]; \n\t\tint i = (low-1); // index of smaller element \n\t\tfor (int j=low; j<high; j++)\n\t\t{\n\t\t\tif (arr[j] <= pivot) \n\t\t\t{\n\t\t\t\ti++;\n\t\t\t\tint temp = arr[i];\n\t\t\t\tarr[i] = arr[j];\n\t\t\t\tarr[j] = temp; \n\t\t\t}\n\t\t}\n\n\n\t\tint temp = arr[i+1];\n\t\tarr[i+1] = arr[high];\n\t\tarr[high] = temp;\n\n\n\t\treturn i+1;\n\t}\n\n\tvoid sort(int arr[], int low, int high)\n\t{\n\t\tif (low < high)\n\t\t{\n\t\t\tint pi = partition(arr, low, high);\n\n\t\t\tsort(arr, low, pi-1);\n\t\t\tsort(arr, pi+1, high);\n\t\t}\n\t}\n\n\tstatic void printArray(int arr[])\n\t{\n\t\tint n = arr.length;\n\t\tfor (int i=0; i<n; ++i)\n\t\t\tSystem.out.print(arr[i]+" ");\n\t\tSystem.out.println();\n\t}\n*/")
      f.close
      function = 'pass'
      return str(function)
