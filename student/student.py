#-- Import Statements --#
from errors import StudentStandingError

#-- Class Definitions --#

# A mapping from class standing to years in school
class_standings = {
    "freshman" : 1,
    "sophmore" : 2,
    "junior" :   3,
    "senior" :   4
}

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
    
















