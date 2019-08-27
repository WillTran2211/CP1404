"""
Name: Tran Nguyen Gia Huy
Student ID: 13721408
Assignment 1: Travel Tracker
Date started: 20/8/2019
GitHub URL: https://github.com/WillTran2211/CP1404/tree/master/HuyTran-A1
"""

place_names = []
place_countries = []
place_priority = []
place_visited = []

#Create function menu:
def menu():
	user_choice = ""
	#Loop to continue menu until user quits:
	while user_choice != "Q":
		#Print menu with options:
		print("Menu:")
		print("L - List places")
		print("A - Add new place")
		print("M - Mark a place as visited")
		print("Q - Quit")
		#Input choice from options:
		user_choice = input(">>> ").upper()
		#Choice L - List places:
		if user_choice == "L":
			places_list()
		#Choice A - Add new place:
		elif user_choice == "A":
			add_a_place()
		#Choice M - Mark a place as visited:
		elif user_choice == "M":
			visited_mark()
		#Choice Q - Quit:
		else:
			save_places()
			print("Have a nice day :)")

#Create function places list:
def places_list():
	#Print all places:
	for i in range(0, len(place_names)):
		print(" {0} {1}. {2:30} in {3:30} priority ({4})".format(place_visited[i], i, place_names[i],
									 place_countries[i], place_priority[i]))
	#Print numbers of both place visited and not visited:
	print("{} places. You still want to visit {} places.".format(len(place_names), place_visited.count("*")))

#Create function add a place:
def add_a_place():
	#Loop to input a place name:
	while True:
		new_place_name = input("Name: ")
		if new_place_name == "":
			print("Input can not be blank")
		else:
			break
	#Loop to input a country name:
	while True:
		new_country_name = input("Country: ")
		if new_country_name == "":
			print("Input can not be blank")
		else:
			break
	#Loop to input a priority number:
	while True:
		try:
			new_priority_number = int(input("Priority: "))
			if new_priority_number <= 0:
				print("Number must be > 0")
			else:
				break
		except ValueError:
			print("Invalid input; enter a valid number")
	print("{} in {} (priority {}) added to Travel Tracker".format(new_place_name, new_country_name,
								      new_priority_number))

#Create function visited mark:
def visited_mark():
	#Input the number of the place visited:
	for i in range(0, len(place_names)):
		print(" {0} {1}. {2:30} in {3:30} priority ({4})".format(place_visited[i], i, place_names[i],
									 place_countries[i], place_priority[i]))
	#Print numbers of both place visited and not visited:
	print("{} places. You still want to visit {} places.".format(len(place_names), place_visited.count("*")))
	print("Enter the number of a place to mark as visited: ")
	new_mark = int(input(">>> "))
	try:
		#Loop to check the number is correct:
		if 0 <= new_mark < len(place_names):
			if place_visited[new_mark] == "*":
				print("{} in {} visited!".format(place_names[new_mark], place_countries[new_mark]))
				place_visited[new_mark] = " "
			else:
				print("That place is already visited.")
		else:
			print("Invalid input; enter a valid number!")
	except ValueError:
		print("Invalid input; enter a valid number!")

#Create function save places:
def save_places():
	#Open CSV file and edit changes:
	out_file = open("places.csv", 'w')
	#Loop through the list:
	for i in range(0, len(place_names)):
		#Change the symbols from "*" and " " back to "n" and "v":
		save_places = place_visited[i]
		if save_places == " ":
			save_places = "v"
		else:
			save_places = "n"
		print("{},{},{},{}".format(place_names[i], place_countries[i], place_priority[i], place_visited[i]))
	out_file.close()

#Create function load places:
def load_places():
	#Load file CSV:
	in_file = open("places.csv", 'r')
	#Loop through the file:
	for line in in_file:
		#Split read line by ','
		place_item = line.split(',')
		#Save the places into a list:
		place_names.append(place_item[0])
		#Save the countries into a list:
		place_countries.append(place_item[1])
		#Save the priority to a list:
		place_priority.append(int(place_item[2]))
		#Save the visited mark to a list:
		place_item[3] = place_item[3].strip('\n')
		if place_item[3] == "v":
			place_item[3] = " "
		else:
			place_item[3] = "*"
		place_visited.append(place_item[3])
	in_file.close()
	#Print the numbers of places loaded:
	print("{} places loaded from places.csv".format(len(place_names)))

#Create main function:
def main():
	#Print welcome message:
	print("Travel Tracker 1.0 - by <Tran Nguyen Gia Huy>")
	#Use other functions:
	load_places()
	menu()

if __name__ == '__main__':
	main()