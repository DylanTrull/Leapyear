import leapYear
import pytest


def test_leapyear():
    assert leapYear.leapYear(12) == True

def test_leapyearFalse():
    assert leapYear.leapYear(10) == False

def test_zero():
    assert leapYear.leapYear(0) == False