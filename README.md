# Mystic:
## [MIT License](https://github.com/RankJay/Mystic/blob/master/LICENSE)
## Website Protoptype: [Mystic.io](https://rankjay.github.io/Mystic/)
Download this [file](https://github.com/RankJay/Mystic/tree/master/docs) to get a better version of website on your chrome browser.
## Working Code without PyTorch Model: [Code](https://repl.it/repls/ImpressiveWholeWheel)
This is our working backend `python` model to write code.
- **NOTE:** This does not have PyTorch model working on backend since it takes enormous amount of time to process, hence this will provide a clearer version of our work so far.

# Documentation:
>Mystic though still-under-construction, in its beta release, will be transformed into a website based on `Python` Back-end architecture connected with `React JavaScript` based front-end designed on Adobe XD as well as an ordinary JavaScript Compiler with an exclusive access to Pandit Deendayal Petroleum University students for their academic as well as non-academic programming practices and interested candidates based on their relativistic and working module ideas that might take this project a step-forward will be allowed to contribute to this project.

- Mystic is an open-source project designed to help developers instantly get the most optimized code for their respective intended input and output with additionally providing them with 4 different coding language export namely `C`,`C++`,`Python` and `Java`.
- Originally, it is designed to provide the user with the most accurate math function concerning user-provided input-output and programming language they wanted the respective program in.
- Since then, Mystic has been expanded single-handedly in string operations like string appending as well as concatenation and deleting of a string and also in data structures operations like array sorting, linked-lists, and search trees as well as graph operations.
- As of now, programming of multi-language conversion is under development which when deployed will be able to convert a program from one programming language to another programming language among `C`,`C++`,`Python`,`Java`. This will be handy for most of the programming project and user will be provided with instant language transfer as per his/her designed system compatibility.
- Further, `GraphQL` and `Graph Plot` as well as `matplotlib` and `seaborn` have been incorporated to provide a quicker analysis of cumulative data sets fed as input.
- `PyTorch` based Deep Learning Prediction model will be trained to further make system append log of data queries generated from the users globally while learning from it in due course.

## Input-Output Based Operations
This section scans the input and checks whether the data received is any programming language code or not, if not it further asks the user to enter the desired output and respective language they want this program in.
The MasterControl then sends this data to Module.py which takes further steps to forward the data entries to respective intended language writers and its function generator to process out the procedure of writing code.
- [Module.py](https://github.com/RankJay/Mystic/blob/master/Module.py) is basically, the core-processor of the entire Input-Output Based Operations functionalities. The only module that reads the received input-output decides which operations should be executed and accordingly forwards the data to generate respective function and then further forward it to respective language `moduleWriter` class to write down the entire code and provide the user with processed code in the desired language intended by the user.
- Functionality Distributor:
  1) Mathematical Functionality
  2) String-related Functionality
  3) Data Structures Functionality
### Mathematical Functionality
The underlying architecture of this entire module lies in interpreting and generating the mathematical function based on input-output that is provided by the user. By following a certain set of protocols as input, the user can easily get the desired mathematical function.
1) Basic Arithmetic Operations: Addition, Subtraction, Multiplication, and Division
2) Power raise to N
3) Nth Root
4) Logarithm to the Base N
5) Floor function
6) Ceiling function
7) Sine function
8) Cosine function
9) Tangent function
10) Sine-Hyperbolic function
11) Cosine-Hyperbolic function
12) Tangent-Hyperbolic function
13) Inverse Sine-Hyperbolic function
14) Inverse Cosine-Hyperbolic function
15) Inverse Tangent-Hyperbolic function
16) Absolute Value Function
17) Maximum function
18) Minimum function
### String-related Functionality
The underlying architecture of this entire module lies in interpreting and generating the function related to string and file handling like concatenation as well as changing cases and handling any grammatical error based on input-output that is provided by the user. By following a certain set of protocols as input, the user can be easily provided with the most significant algorithm based on the output generated.
1) String Concatenation
2) String Deletion
3) Palindrome
### Data Structures Functionality
The underlying architecture of this entire module lies in interpreting and generating the source data structure based on the input-output that is provided by the user. By following a certain set of protocols as input, the user can be easily provided with the most significant algorithm for the required data structure based on expected output. Here, the size of input matters, since asymptotic notations like Big-Oh is taken into consideration for evaluating certain parameters to generate expected outcomes.
1) Sorting Algorithm based on input array size
## Code Based Operations
This section scans the input and checks whether the data received is any programming language code or not, if yes it further asks the user to enter desired programming language they want this program in.
The MasterControl then sends this data to languageTranslator.py which takes further steps to forward the program to respective intended languagetranslator which further forwards it to Interpreter. Here, the entire program irrespective of the programming language is converted into the interpreted mode and then it passes through languageConvertor to process out the procedure of writing code.
### Language Translator
The underlying architecture of this entire module lies in recognizing and interpreting the programming language based on input that is provided by the user and converting it to the required programming language as suggested by the user. By following a certain set of protocols as input, the user can easily get the program in the required programming language
