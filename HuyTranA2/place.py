"""..."""

# Create your Place class in this file

class Place:

    # Initialise a place:
    def __init__(self, visited="", place_name="", country="", priority=0):
        self.visited = visited
        self.place_name = place_name
        self.country = country
        self.priority = int(priority)

    # Mark a place as visited:
    def visit(self):
        self.visited = "(visited)"

    # Mark a place as unvisited:
    def unvisit(self):
        self.visited = ""

    # Print a place to screen:
    def __str__(self):
        return "\"{1}\" in {2} as priority {3}. {0}".format(self.visited, self.place_name, self.country, self.priority)

    # Print a place as dynamic widget:
    def __repr__(self):
        return "\"{1}\" in {2} as priority {3}. {0}".format(self.visited, self.place_name, self.country, self.priority)

"""..."""