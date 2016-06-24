# This module will contains errors that are raised within the student package.

class Error(Exception) :
    """A base class for custom errors raised in modules classes."""
    pass

class StudentStandingError(Error) :
    """Raised when a an unexpected student class standing is encountered.

    Attributes :
        msg - a message explaining why the error was raised
        standing - the standing which caused this particular error   
    """
    def __init__(self, msg, standing) :
        self.msg = msg
        self.standing = standing

    def __str__(self) :
        return repr(self.standing)