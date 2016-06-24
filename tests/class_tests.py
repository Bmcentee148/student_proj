# Simple skeleton file for running tests on our project

from nose.tools import *
import student

def setup() :
    print 'SETUP!'

def teardown() :
    print 'TEARDOWN!'

def test_basic() :
    print 'I RAN!'