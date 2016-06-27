# Tests for module level functions in student

#-- Import Statements --#
from nose.tools import *
from student.student import *

# Person objects for testing
p1 = Person(Name("Brian","McEntee"),25)
p2 = Person(Name("Brian","McEntee"),25)
p3 = Person(Name("Casey","Jones"),93) 

# Student objects for testing
s1 = Student(Name("Brian","McEntee"),25, "High Times University", "senior")
s2 = Student(Name("Brian","McEntee"),25,"High Times University", "senior")
s3 = Student(Name("Casey","Jones"),93, "Stony Brook University", "sophmore")

def test_sort_people() :
    # Sorting based on age tests
    people = [p3, p2, p1]
    presorted_people = [p1, p2, p3]
    assert_equals(sort_people(people), presorted_people)

def test_sort_students() :
    studs = [s1, s2, s3]
    presorted_studs = [s3, s1, s2]
    assert_equals(sort_students(studs), presorted_studs)
    assert_not_equal(studs, sort_students(studs))

def test_get_directory() :
    expected_dir = '/Users/brian/Dev/Python/projects/student_proj/student/data/test.txt'
    assert_equals(get_file_path('test.txt'), expected_dir)

def test_file_resources() :
    saved = [p1, p2, p3]
    save_to_file(saved, 'test.pkl')
    loaded = load_from_file('test.pkl')
    assert_equals(saved, loaded)

    save_to_file([],'test.pkl')
    loaded = load_from_file('test.pkl')
    assert_equals([],loaded)

    saved = [s1, s2, s3]
    save_to_file(saved, 'test.pkl')
    loaded = load_from_file('test.pkl')
    assert_equals(saved, loaded)

