import pytest

@pytest.mark.usefixtures("driver_setup")
class BaseClass:
    global driver

    def something(self):
        pass