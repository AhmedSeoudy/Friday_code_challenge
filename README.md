# Friday_code_challenge
Address Parsing using Python

Description:
An address provider returns addresses only with concatenated street names and numbers. Our system has separate fields for street name and house numbers. 
Input: String of address
Output: String of street name and a string of house number as a json object.
The code is developed 100% in Python


Introduction:
I followed Test Driven development during implementing the tasks where I wrote test cases then started development of the code. The test cases where made based on the criteria discussed below. 


Criteria for Street Name: 
Street names can consist of letters (incl. special German characters), spaces, dots or hyphens. 
Ex: Weinbergstrasse or Calle Aduana or Weibergstr. or Heinrich-Heine 
Regex used to handle these cases for street names: “\s*([a-zA-ZäöüÄÖÜß-]+[\.]?[\s]*)+”
A street name can end with numbers if the comma separator is used between street name and house number. It can also start or/and end with numbers if the street name and the house numbers are separated by the word “No.”, “No ” or “N.” (case insensitive)
Ex: 4, rue de la revolution 10  where street name is rue de la revolution 10 and house is 4
Calle Ave 39 No.1540 B  street name is Calle Ave 39 and house is 1540 B

Criteria for House Number:  
House Numbers can be a simple number, but can also be 2 numbers / a number and a letter separated by a hyphen or a forward slash
Ex: 45 or 12-A or 23/B or 12-14
Regex used: [0-9]+\s*([/|-]\s*([0-9]*)?)?\s*[a-zA-ZäöüÄÖÜß-]*

The three main Regex Cases:
	•	Street name followed by a house number (house number can be numeric or alphanumeric) and the separator between street and house number can be any number of spaces or a comma.  "\s*([a-zA-ZäöüÄÖÜß-]+[\.]?[\s]*)+([\d]*[\s]*,)?[\s]*[0-9]+\s*([/|-]\s*([0-9]*)?)?\s*[a-zA-ZäöüÄÖÜß-]*\s*"
	•	House number (house number can be numeric or alphanumeric) followed by a street name  "\s*[0-9]+[/|-]?([-][0-9]*)?[\s]*[a-zA-ZäöüÄÖÜß-]?\s*,?\s*([a-zA-ZäöüÄÖÜß-]+[\d]*[\.]?\s*)+[\d]*"
	•	Street name followed by a house number (house number can be numeric or alphanumeric) separated by No. or N.   "(?i)\s*[0-9]*([-][0-9]*)?\s*([a-zA-ZäöüÄÖÜß]+[-]?\s*)+[\.]?[\s]?[0-9]*\s*(NO((\.[\s]?)|[\s]+)|N[\.][\s]?)[0-9]*[/|-]?([-][0-9]*)?[\s\D]*\s*"
	•	If there is no numbers only letters then all string is added to street name and house number is none

To Run the Code:
	•	Add your test strings in test.txt
	•	Run task_main.py and make sure address_parser is imported  
	•	The resulted json file under the name json_data is generated containing the results

Contact:
Author: Ahmed Saudi – ahmedseoudy95@gmail.com
