import pytest
import main

name = "A B C"
post = "abc"
time = 120
salary = 10000
payment = round(salary * (time / main.Person.hours_norm), 2)

pers = main.Person(name,post,time,salary)

def test_getters():
    assert main.Person.get_name(pers) == name
    assert main.Person.get_post(pers) == post
    assert main.Person.get_time(pers) == time
    assert main.Person.get_salary(pers) == salary
    assert main.Person.get_payment(pers) == payment

def test_show_persons():
    assert main.show_persons() == 0
