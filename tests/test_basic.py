"""Basic tests for {{ cookiecutter.package_name }}."""

from {{ cookiecutter.package_name }} import hello, core

def test_hello():
    assert "Hello" in hello()

def test_add():
    assert core.add(2, 3) == 5

def test_multiply():
    assert core.multiply(2, 3) == 6
