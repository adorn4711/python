def add(x,y):
    return x+y

# Call pytest with tests for this module
if __name__ == '__main__':
    import pytest
    pytest.main(["-x", "unittest\\test_simple_function.py", "-vv"])
