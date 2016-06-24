# Simple skeleton file for running tests on our project

from nose.tools import *
from student.student import *

# Person objects for testing
p1 = Person("Brian","McEntee",25)
p2 = Person("Brian","McEntee",25)
p3 = Person("Casey","Jones",93) 

# Student objects for testing
s1 = Student("Brian","McEntee",25, "High Times University", "senior")
s2 = Student("Brian","McEntee",25,"High Times University", "senior")
s3 = Student("Casey","Jones",93, "Stony Brook University", "sophmore")

def test_person_class() :
    # Attribute tests
    assert_equals(p3.first, "Casey")
    assert_equals(p3.last, "Jones")
    assert_equals(p3.age, 93)
    # Equality tests
    assert_equals(p1, p2)
    assert_not_equal(p1,p3)


def test_student_class() :
    # Attribute Tests
    assert_equals(s3.first, "Casey")
    assert_equals(s3.last, "Jones")
    assert_equals(s3.age, 93)  
    assert_equals(s3.school_name, "Stony Brook University")
    assert_equals(s3.standing, "sophmore")
    # Equality Tests
    assert_equals(s1, s2)
    assert_not_equal(s1,s3) 

def test_sort_people() :
    # Sorting based on age tests
    people = [p3, p2, p1]
    presorted_people = [p1, p2, p3]
    for x, y in zip(sort_people(people), presorted_people) :
        assert_equals(x, y)

