import json

# just an example class to save and load data from
class example:
    def __init__(self):
        self.running = 4
        self.ran = 5

# adds functionality for saving classes with __dict__
def jdefault(o):
    return o.__dict__

# main class its quite simple and it just has two functions
class save_engine:
    # saves the a class in a file with json
    def save(self,file, object):
        # opens/creates file in write mode
        with open(file, 'wb') as data:
            # dumps all of the  __dict__ for a class into a variable in json
            save = json.dumps(object, default=jdefault)
            # writes all of the json to said file
            data.write(save.encode())
        
    # loads a class with json into an object
    def load(self,file,object):
        # open the save file in read mode
        with open(file, 'r') as data:
            # reads data into variable
            raw_data = data.read()
      
        # makes the data be python and not json
        read_data = json.loads(raw_data)
        # loads the data into the object
        object.__dict__ = read_data


