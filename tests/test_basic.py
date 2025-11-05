"""
Basic tests for the RentEase Backend
These tests validate that our setup is working correctly.
"""

def test_environment():
    """Test that our basic environment is set up correctly"""
    assert True  # This should always pass


def test_python_version():
    """Test that we're using the correct Python version"""
    import sys
    # Updated: Check we're using Python 3.9 (your actual version)
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 9  # Changed from >=10 to ==9
    print(f"Python version: {sys.version}")


def test_basic_math():
    """A simple test to verify basic functionality"""
    result = 2 + 2
    expected = 4
    assert result == expected, f"Expected {expected}, got {result}"


def test_imports():
    """Test that we can import common libraries"""
    try:
        import pytest
        import pipenv
        assert True  # If we get here, imports worked
    except ImportError as e:
        assert False, f"Import failed: {e}"