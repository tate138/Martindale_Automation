from tests import banner_module
from tests import blade_module
from tests import featured_blocks
from tests import call_to_action

if __name__ == "__main__":
    banner_module.test_suite()
    blade_module.test_suite()
    featured_blocks.test_suite()
    call_to_action.CallToAction.test_call_to_action()