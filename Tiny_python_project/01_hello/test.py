#import os & pytest
import os, pytest

#give a name to the file
file_name = '_\hello.py'

#check if the file exixts
def file_exists():
    assert os.path.isfile(file_name)

#import getoutput module
from subprocess import getstatusoutput, getoutput

#check if the program will run
def test_runs():
    program_exec = getoutput(file_name)
    assert program_exec.strip() == 'Hello world'
    
#check if the test will execute
def test_executable():
    program_exec = getoutput(file_name)
    assert program_exec.strip() == 'Hello world'
    
#use pytest -xv test.py to run the test