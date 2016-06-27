# Tests for core classes and their accompanying methods

#-- Import Statements --#
from nose.tools import *
from student.student import *
from student.errors import *

# Person objects for testing
p1 = Person(Name("Brian","McEntee"),25)
p2 = Person(Name("Brian","McEntee"),25)
p3 = Person(Name("Casey","Jones"),93) 

# Student objects for testing
s1 = Student(Name("Brian","McEntee"),25, "High Times University", "senior")
s2 = Student(Name("Brian","McEntee"),25,"High Times University", "senior")
s3 = Student(Name("Casey","Jones"),93, "Stony Brook University", "sophmore")

def test_person_class() :
    # Attribute tests
    assert_equals(p3.name.first, "Casey")
    assert_equals(p3.name.last, "Jones")
    assert_equals(p3.age, 93)
    # Equality tests
    assert_equals(p1, p2)
    assert_not_equal(p1,p3)


def test_student_class() :
    # Attribute Tests
    assert_equals(s3.name.first, "Casey")
    assert_equals(s3.name.last, "Jones")
    assert_equals(s3.age, 93)  
    assert_equals(s3.school_name, "Stony Brook University")
    assert_equals(s3.standing, "sophmore")
    # Equality Tests
    assert_equals(s1, s2)
    assert_not_equal(s1,s3)
    # Error raising Tests
    assert_raises(StudentStandingError, Student,
       Name( "Casey","Jones"),93, "Stony Brook University", "none")





