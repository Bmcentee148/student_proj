#-- Import Statements --#
from errors import StudentStandingError
import sys
import os
import pickle

#-- Module level attributes --#

# A mapping from class standing to years in school
class_standings = {
    "freshman" : 1,
    "sophmore" : 2,
    "junior" :   3,
    "senior" :   4
}

#-- Resource Handling Functions --#

def save_to_file(ppl_list, pkl_file_name) :
    """Saves a list of people to a file.

    Notes :
        overrides contents of existing file with new list, does not update.
    Args :
        pkl_file_name - the name of the .pkl file to save to
        ppl_list - the list of people to save to the file
    """
    file_path = get_file_path(pkl_file_name)
    try :
        with open(file_path, 'wb') as output_file :
            pickle.dump(ppl_list, output_file, pickle.HIGHEST_PROTOCOL)
    except IOError as e :
        print e
        sys.exit(1)

def load_from_file(pkl_file_name) :
    """Loads list of people from a file.

    Args :
        pkl_file_name - the .pkl file to load the list from 
    Returns :
        a list of objects that are of type Person or inherit from Person
    """
    file_path = get_file_path(pkl_file_name)
    result = []
    try :
        input_file = open(file_path,'rb')
    except IOError as e :
        print "No saved data file found."
    else :
        result = pickle.load(input_file)
    return result

def get_file_path(pkl_file_name) :
    """Get the path of file we save data to and load data from. 
    
    Args :
        pkl_file_name - the name of the .pkl data file
    Returns :
        the path of the file where saved data is located
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path =  os.path.join(dir_path,'data',pkl_file_name)
    return file_path

#-- Class Definitions --#

class Person(object) :
    """A class that represents a general person.

    Attributes :
        first - the first name of the person
        last - the last name of the person
        age - the age of the person in years
    """

    def __init__(self, first, last, age) :
        self.first = first
        self.last = last
        self.age = age

    def __eq__(self, other) :
        return (self.first == other.first and
                self.last == other.last and
                self.age == other.age)

class Student(Person) :
    """A class that represents a student in college.

    Attributes :
        school_name - the name of the school the student is currently attending
        standing - the current class standing the student has
    """

    def __init__(self, first, last, age, school_name, standing) :
        if standing in class_standings :
            super(Student, self).__init__(first, last, age)
            self.school_name = school_name
            self.standing = standing
        else :
            raise StudentStandingError(
                "Unexpected standing encountered for student", standing 
                )

    def __eq__(self, other) :
        return (super(Student, self).__eq__(other) and
                self.school_name == other.school_name and
                self.standing == other.standing)

def sort_people(people_list) :
    """Get a sorted list of the people by age.

    Notes :
        - does not alter the original list passed
    Args :
        people_list - the list of People objects to sort
    Returns :
        a sorted list of the people by age
    """
    return sorted(people_list, key = lambda x: x.age)

def sort_students(student_list) :
    """Get a sorted list of the students by class standing.

    Notes :
        does not alter the original list passed
    Args :
        student_list - the list of Student objects to sort
    Returns :
        a sorted list of the students by current class standing
    """
    return sorted(student_list, key= lambda x: class_standings[x.standing])
    
















