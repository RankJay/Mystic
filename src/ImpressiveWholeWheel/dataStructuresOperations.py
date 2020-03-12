class dataStructuresOperations:
  def cdataStructuresOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.c","w+")
      f.write("/*\nvoid swap(int* a, int* b)\n{\n\tint t = *a;\n\t*a = *b;\n\t*b = t;\n}\nint partition (int arr[], int low, int high)\n{\n\tint pivot = arr[high];\n\tint i = (low - 1);\n\tfor (int j = low; j <= high- 1; j++)\n\t{\n\t\tif (arr[j] < pivot)\n\t\t{\n\t\t\ti++;\n\t\t\tswap(&arr[i], &arr[j]);\n\t\t}\n\t}\n\tswap(&arr[i + 1], &arr[high]);\n\treturn (i + 1);\n}\nvoid quickSort(int arr[], int low, int high)\n{\n\tif (low < high)\n\t{\n\t\tint pi = partition(arr, low, high);\n\t\tquickSort(arr, low, pi - 1);\n\t\tquickSort(arr, pi + 1, high);\n\t}\n}\n*/\n")
      f.close
      function = '0\n\tquickSort(arr, 0, n-1);\n\tfor (int i=0; i < n; i++)\n\t\tprintf("%d ", arr[i]);\n\tprintf("\\n")'
      return str(function)

  def cPlusdataStructuresOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.c","w+")
      f.write("/*\nvoid swap(int* a, int* b)\n{\n\tint t = *a;\n\t*a = *b;\n\t*b = t;\n}\nint partition (int arr[], int low, int high)\n{\n\tint pivot = arr[high];\n\tint i = (low - 1);\n\tfor (int j = low; j <= high- 1; j++)\n\t{\n\t\tif (arr[j] < pivot)\n\t\t{\n\t\t\ti++;\n\t\t\tswap(&arr[i], &arr[j]);\n\t\t}\n\t}\n\tswap(&arr[i + 1], &arr[high]);\n\treturn (i + 1);\n}\nvoid quickSort(int arr[], int low, int high)\n{\n\tif (low < high)\n\t{\n\t\tint pi = partition(arr, low, high);\n\t\tquickSort(arr, low, pi - 1);\n\t\tquickSort(arr, pi + 1, high);\n\t}\n}\n*/\n")
      f.close
      function = '0\n\tquickSort(arr, 0, n-1);\n\tfor (int i=0; i < n; i++)\n\t\tprintf("%d ", arr[i]);\n\tprintf("\\n")'
      return str(function)
  
  def pythondataStructuresOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.py","w+")
      f.write("'''\ndef partition(arr,low,high):\n\ti = ( low-1 )\n\tpivot = arr[high]\n\n\tfor j in range(low , high):\n\t\tif arr[j] < pivot:\n\t\t\ti = i+1\n\t\t\tarr[i],arr[j] = arr[j],arr[i]\n\tarr[i+1],arr[high] = arr[high],arr[i+1]\n\treturn ( i+1 )\n\ndef quickSort(arr,low,high):\n\tif low < high:\n\t\tpi = partition(arr,low,high)\n\t\tquickSort(arr, low, pi-1)\n\t\tquickSort(arr, pi+1, high) \n\narr = [float(x) for x in input().split()] \nn = len(arr)\n'''\n")
      f.close
      function = 'quickSort(arr,0,n-1)\noutput=arr'
      return str(function)
  
  def javadataStructuresOperations(inputFromUser, outputFromUser):
    modularInOperations = [float(index) for index in inputFromUser.split(' ')]
    modularInOperations.sort()
    modularOutOperations = [float(index) for index in outputFromUser.split(' ')]
    if modularInOperations==modularOutOperations:
      f= open("Program.java","w+")
      f.write("/*class QuickSort\n{\n\tint partition(int arr[], int low, int high)\n\t{\n\t\tint pivot = arr[high];\n\t\tint i = (low-1);\n\t\tfor (int j=low; j<high; j++)\n\t\t{\n\t\t\tif (arr[j] < pivot)\n\t\t\t{\n\t\t\t\ti++;\n\t\t\t\tint temp = arr[i];\n\t\t\t\tarr[i] = arr[j];\n\t\t\t\tarr[j] = temp;\n\t\t\t}\n\t\t}\n\t\tint temp = arr[i+1];\n\t\tarr[i+1] = arr[high];\n\t\tarr[high] = temp;\n\n\t\treturn i+1;\n\t}\n\n\tvoid sort(int arr[], int low, int high)\n\t{\n\t\tif (low < high)\n\t\t{\n\t\t\tint pi = partition(arr, low, high);\n\n\t\t\tsort(arr, low, pi-1);\n\t\t\tsort(arr, pi+1, high);\n\t\t}\n\t}\n\tstatic void printArray(int arr[])\n\t{\n\t\tint n = arr.length;\n\t\tfor (int i=0; i<n; ++i)\n\t\t\tSystem.out.print(arr[i]+" ");\n\t\tSystem.out.println();\n\t}\n}*/\n")
      f.close
      function = '0'
      return str(function)
