from vector3 import Vector3
import pytest

def test_u():
    v=Vector3(1,2,3)
    w=Vector3(-5,1,1)
    u = v.add(w).mul(10)
    assert u.a == -40
    assert u.b == 30
    assert u.c == 40

def test_v():
    v=Vector3(1,2,3)
    w=Vector3(-5,1,1)
    x = v.dot(w)
    assert x == 0
