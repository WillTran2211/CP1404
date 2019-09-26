"""..."""

# Create your PlaceCollection class in this file

import csv
from place import Place
from operator import attrgetter

class PlaceCollection:

    # Initialise a place list:
    def __init__(self):
        self.places = []

    # Add a place:
    def addPlace(self, add_place):
        self.places.append(add_place)
        return (self.places)

    # Print places in list:
    def __str__(self):
        print_place = ""
        for element in self.places:
            print_place += ("{}\n".format(element))
        return print_place

    # Count unvisited places:
    def countUnvisitedPlaces(self):
        unvisitedPlaces = 0

        for element in self.places:
            if element.visited != "(visited)":
                unvisitedPlaces += 1
        return unvisitedPlaces

    # Count visited places:
    def countVisitedPlaces(self):
        visitedPlaces = 0

        for element in self.places:
            if element.visited == "(visited)":
                visitedPlaces += 1
        return visitedPlaces

    # Extract places in csv:
    def loadPlaces(self, filename):
        csv_place_list_file = open(filename, "r")
        csv_place_list = csv.reader(open(filename, "r"))

        # Create list to contain places:
        placeList = []
        for line in csv_song_list:
            if line[3].strip().lower() == "v":
                visitedMark = "(visited)"
            elif line[3].strip().lower() == "n":
                visitedMark = ""
            else:
                visitedMark = line[3]

            # Add a place to list:
            place = Place(visitedMark, line[0], line[1], line[2])
            placeList.append(place)

        csv_place_list_file.close()
        self.places = placeList

    # Save places back to CSV file:
    def savePlaces(self, filename):
        visited_status = ""
        with open(filename, "w") as csv_place_list_file:
            for eachPlace in self.places:
                csv_writer = csv.writer(csv_place_list_file)

                if eachPlace == "(visited)":
                    visited_status = "v"
                elif eachPlace == "":
                    visited_status = "n"
                else:
                    visited_status = eachPlace.visited

                csv_writer.writerow([eachPlace.place_name, eachPlace.country, eachPlace.priority, eachPlace.visited])
        print("{} place saved to {}".format(len(self.places), filename))
        csv_place_list_file.close()

    # Sort places in list:
    def sortPlaces(self, key):
        sortedPlaces = []
        key = key.lower()

        if key == "place_name":
            key = "name"

        sortedPlaces = sorted(self.places, key=attrgetter(key, "name"))
        self.places = sortedPlaces

"""..."""