#-------------------------------------------------------------------------------
# Name: Tan Nguyen
# Assignment 12
# Due Date: December 6th, 2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, assignments are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#        10        20       30       40        50        60        70        80
#-------------------------------------------------------------------------------

class Plane: #define plane class
    # initialize instance variables
    def __init__(self,model,manufacturer,fuel):
        self.model = model
        self.manufacturer = manufacturer
        self.fuel = fuel

    # create and return required string using f-string
    def __str__(self):
        s = f"{self.model}, {self.manufacturer} :: {self.fuel} / 100"
        return s

    # check if two plane is equal or not (note that different fuel value doesnt affect equality)
    def __eq__(self,other):
        if self.model == other.model and self.manufacturer == other.manufacturer:
            return True
        else:
            return False

    # check whether the plane has no fuel left
    def is_empty(self):
        if self.fuel ==0:
            return True
        else:
            return False
    
    
    # refuel function for plane, noted that no negative amount be added,
    # and the post-refueling process will not yield in plane with fuel value >100
    def refuel(self,amount):
        # raise PlaneError if those conditions is met
        if amount <0 or (self.fuel + amount) >100:
            raise PlaneError("unable to refuel by {}".format(amount))
        else:
            self.fuel += amount

# define hangar class 
class Hangar:
    
    # initialize instance variables, default parameter for planes list is empty ([])
    def __init__(self,name):
        self.name = name
        self.planes = []
    
    
    # create and return string as needed, noted that when planes list is empty
    # -> return hangar's name and colon
    def __str__(self):
        s = f"{self.name}:\n"
        if self.planes !=[]:
            for plane in self.planes:
                s += f"\t{plane}\n"
        return s   
    
    
    # check if two hangar is equal, noted that name of hangar does not matter
    # will be TRUE even if the hangars' names are different 
    def __eq__(self,other):
        result = True
        # check for the length of 2 different hangar planes list, they have to be the 
        # same in the first place to be considered equal 
        if len(self.planes) == len(other.planes):
            for i in range(len(self.planes)):
                # compare consecutive pairs of 2 lists of planes (this relies on __eq__ method
                # Plane class)
                if self.planes[i] != other.planes[i]:
                    result = False
        else:
            result = False
        return result
    
    
    # add plane to self.planes list function
    def add_plane(self,plane):
        # only add plane to list if it's not in the list already
        if plane not in self.planes:
            self.planes.append(plane)
        else:
            # if it's in the plane list, raise PlaneError
            for plane in self.planes:
                raise PlaneError("duplicate plane '{}:{}'".format(plane.model,plane.manufacturer))
    
    
    # return Plane object whose title matches the model argument
    def plane_by_model(self,model):
        # Add all model of planes from self.planes to different list
        
        lst =[]
        for plane in self.planes:
            lst.append(plane.model)
        # if the examining model is in that list, we continue, otherwise, raise PlaneError
        if model in lst:
            #noted that self.planes length and lst length are the same
            #loop through self.planes list to check if model element of lst at i position of 
            # both lists, return plane at that i position
            for i in range(len(self.planes)):
                if model == lst[i]:
                    return self.planes[i]
        else:
            raise PlaneError("no plane found with model '{}'".format(model))


    # return the list of planes that built by examining company in list    
    def planes_by_manufacturer(self,company):
        # initialize that list with newlst
        newlst = []
        # loop through plane list
        for plane in self.planes:
            # if company found in plane class, add that plane to newlst
            if company == plane.manufacturer:
                newlst.append(plane)
        # raise PlaneError if no planes was built by that company, otherwise
        # return that newlst
        if len(newlst) != 0:
            return newlst
        else:
            raise PlaneError("no planes built by '{}'".format(company))


    #check total number of planes that are out of fuel
    def total_empty(self):
        count = 0
        # use is_empty method in Plane Class to check that. loop through
        # every single plane in planes list, if True, count incrementing by 1
        for x in self.planes:
            if x.is_empty() == True:
                count +=1
        return count

    # use try and except here
    def refuel_all(self,amount):
        # loop through each plane in self.planes list, if that plane cannot
        # be refueled, simply skip to next one using continue
        for plane in self.planes:
            try:
                plane.refuel(amount)
            except PlaneError:
                continue

             
    
# extends notion of an Exception, noted that we already made our exception
# store in single string message in every needed sub-definitions
class PlaneError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg



## this is a test update 

## this is second update for the test