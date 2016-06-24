#-- Class Definitions --#

# A mapping from class standing to years in school
class_standings = {
    "freshman" : 1,
    "sophmore" : 2,
    "junior" : 3,
    "senior" : 4
}

class Person(object) :
    """ A class that represents a general person.

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
    """ A class that represents a student in college.

    Attributes :
        school_name - the name of the school the student is currently attending
        standing - the current class standing the student has
    """

    def __init__(self, first, last, age, school_name, standing) :
        self.school_name = school_name
        self.standing = standing
        super(Student, self).__init__(first, last, age)

    def __eq__(self, other) :
        return (super(Student, self).__eq__(other) and
                self.school_name == other.school_name and
                self.standing == other.standing)

def sort_people(people_list) :
    return sorted(people_list, key = lambda x: x.age)
    
class Error(Exception) :
    """ A base class for custom errors raised in classes. """
    pass

class StandingError(Error) :
    pass
