import unittest
from tests.main_test_register import TestRegistration
from tests.main_test_home import TestHome
from tests.main_test_pick_business import TestPickBusiness
from tests.main_test_gift_purchase import TestGiftPurchase

#  Self Reference: https://docs.python.org/3/library/unittest.html#load-tests-protocol
test_classes = (TestRegistration, TestPickBusiness, TestGiftPurchase, TestHome)



def main():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
    # print("main running")


if __name__ == '__main__':
    main()
