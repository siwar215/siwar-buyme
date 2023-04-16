# Run all tests and add to report
pytest --alluredir=allure-report

# Run a specific tests folder and add to report
pytest main.py --alluredir=allure-report
 
# Run Allure server
allure serve allure-report/


<img width="1279" alt="Screenshot 2023-04-16 at 22 49 39" src="https://user-images.githubusercontent.com/49609496/232338739-585e0f10-af4d-4bf5-a192-e5bd2969c675.png">
<img width="1257" alt="Screenshot 2023-04-16 at 22 50 12" src="https://user-images.githubusercontent.com/49609496/232338760-c5b35814-3e6f-4085-8fe3-d6e4755f10da.png">
<img width="1260" alt="Screenshot 2023-04-16 at 22 50 54" src="https://user-images.githubusercontent.com/49609496/232338771-e4bc0c92-2061-43c1-9e91-43e4d36a10be.png">
