from hello import add, subtract

# Refer to pytest documentation for setup and teardown functions:
# https://docs.pytest.org/en/6.2.x/xunit_setup.html

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    print(f" Running Setup: {function.__name__}")
    function.x = 3
    function.y = 2

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y


def test_add():
    assert add(test_add.x, test_add.y) == 5
    
def test_subtract():
    assert subtract(test_subtract.x, test_subtract.y) == 1