class Location:
    north = None
    south = None
    west = None
    east = None

    location_name = None
    location_description = None

    def __init__(self, location_name, location_description):
        self.location_name = location_name
        self.location_description = location_description

    def __str__(self):
        output = (self.location_name + "\n"
                  + self.location_description + "\n\n")
        direction = ""
        if self.north:
            direction += "sever "
        if self.south:
            direction += "jih "
        if self.west:
            direction += "západ "
        if self.east:
            direction += "východ "
        output += f"Můžeš jít na {direction}\n"
        return output