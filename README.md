# Run all tests and add to report
pytest main_test_register.py --alluredir=allure-report
 
# Run Allure server
allure serve allure-report/
