"""
Name: Huy Tran
Date: 20/9/2019
Brief Project Description: This is the project of implementing Travel Tracker 2.0 app
GitHub URL:
"""

# Create your main program in this file, using the TravelTrackerApp class

from place import Place
from placecollection import PlaceCollection
from operator import attrgetter
import csv

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty

# Sort:
SORT_TYPE = ["Priority", "Place", "Country", "Visited"]
YELLOW = (255, 255, 0, 0.5)
GREEN = (0, 255, 0, 0.5)

#Main app:
class TravelTrackerApp(App):
    status_text = StringProperty()
    places_status = StringProperty()
    click_status = StringProperty()

    current_sort = StringProperty()
    sort_codes = ListProperty()

    # Quit the app: onstop
    def on_stop(self):
        print("The programme is exiting!")

        filename = "places.csv"
        try:
            with open(filename, "w") as csv_place_list_file:
                for eachPlace in self.placelist.places:
                    csv_writer = csv.writer(csv_place_list_file)

                    if eachPlace.visited == "(visited)":
                        visitedMark = "v"
                    elif eachPlace.visited == "":
                        visitedMark = "n"
                    else:
                        visitedMark = eachPlace.visited

                    csv_writer.writerow([eachPlace.place_name, eachPlace.country, eachPlace.priority, visitedMark])
            print("Places saved to CSV successfully!")
        except:
            print("Error occurred when writing places to CSV or when quiting application.")
        csv_place_list_file.close()

    # Initialise:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.placelist = PlaceList()

    # Load the app:
    def build(self):
        self.title = 'Travel Tracker 2.0'
        self.root = Builder.load_file('app.kv')
        self.placelist.loadPlaces("places.csv")
        self.sort_codes = sorted(SORT_TYPE)

        # Set "priority" as default sort:
        self.current_sort = self.sort_codes[3]
        self.add_widgets("priority")

        return self.root

    # Change sort
    def change_sort(self, sort_type):
        if sort_type != self.current_sort:
            self.destroy_places_view()
            self.add_widgets(sort_type)
        self.current_sort = self.root.ids.spinner_sort.text

    # Clear current places in GUI:
    def destroy_places_view(self):
        self.root.ids.places_box.clear_widgets()

    # Show places in GUI:
    def add_widgets(self, sort_type):
        self.placelist.sortPlaces(sort_type)
        for place in self.placelist.places:

            # Coloring place based on visited status:
            if place.visited == "":
                temp_button = Button(text=song.__repr__(), id=song.__repr__(), background_color=YELLOW)
            else:
                temp_button = Button(text=song.__repr__(), id=song.__repr__(), background_color=GREEN)

            print(temp_button.id)
            temp_button.bind(on_release=self.callback)
            self.press(temp_button)
            self.root.ids.places_box.add_widget(temp_button)

    def press(self, instance):
        # Show the top status bar:
        name = instance.id
        self.places_status = "To visit (in yellow): {1}. Visited (in green): " \
                             "{0}".format(self.placelist.getNumberOfVisitedPlaces(),
                                          self.songlist.getNumberOfUnvisitedPlaces())

    # Event for clicking on a place:
    # Note: if the place is visited, clicking will make it 'unvisited':
    def callback(self, instance):
        name = instance.id
        status_visit_to_print = ""
        place_name_to_print = ""
        button_update_str = ""
        for place in self.placelist.places:
            if place.__repr__() == name:
                if place.visited == "":
                    place.visit()
                    status_visit_to_print = "visited"
                    instance.background_color = GREEN
                else:
                    place.unvisit()
                    status_visit_to_print = "unvisited"
                    instance.background_color = YELLOW
                place_name_to_print = place.name
                button_update_str = place.__repr__()
        print(button_update_str)
        instance.text = button_update_str
        instance.id = button_update_str

        # Update top and bottom status bar:
        self.click_status = "You have just {} {}.".format(status_visit_to_print, place_name_to_print)
        self.update_topbar()

    # Update the top status bar:
    def update_topbar(self):
        self.places_status = "To visit (in yellow): {1}. Visited (in green): {0}".format(
            self.placelist.getNumberOfVisitedPlaces(),
            self.songlist.getNumberOfUnvisitedPlaces())

    # Function adding place when clicking 'add place':
    def add_place(self):
        try:
            place_name = self.root.ids.title_input.text
            place_country = self.root.ids.artist_input.text
            place_priority = self.root.ids.year_input.text

            # Check if user missed something:
            if (place_name == "" or place_country == "" or place_priority == ""):
                self.click_status = "All fields must be completed!"
                return

            # Convert priority to INT to check:
            place_priority = int(place_priority)
            if (place_priority / 10000) >= 1:
                raise ValueError

            place_visited = ""

            place_to_add = Place(place_visited, place_name, place_country, place_priority)
            self.placelist.addPlace(place_to_add)

            # Print the place list to debug:
            print(self.placelist)

            self.destroy_places_view()
            self.add_widgets("priority")
            self.click_status = "New place added. Thank you!"
            self.update_topbar()
            self.clear_inputs()

        # When inputting an invalid place priority:
        except ValueError:
            self.click_status = "Please enter a valid number/data"

    # Clear all fields in adding-place section:
    def clear_inputs(self):
        self.root.ids.title_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""

    def clear_all(self):
        self.root.ids.main_box.clear_widgets()

    pass

if __name__ == '__main__':
    TravelTrackerApp().run()
