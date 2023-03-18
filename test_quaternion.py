from quaternion import Quaternion
import pytest

def test_conjugate():
    q1 = Quaternion(0,1,2,3)
    q2 = Quaternion(0,-1,-2,-3)
    assert q1.conjugate()==q2
    

def test_mul():
    q1 = Quaternion(0,1,2,3)
    q2 = Quaternion(0,-1,-2,-3)
    expected =Quaternion(14,0,0,0)
    assert q1*q2==expected