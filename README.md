# Run all tests and add to report

pytest main.py --alluredir=allure-report
 
# Run Allure server
allure serve allure-report/
