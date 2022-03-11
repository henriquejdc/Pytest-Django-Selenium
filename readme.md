Software Quality Control

Pytest & Django
AND
Pytest & Django with Selenium

Utilizado:
- Windows 10
- Pytest 6.2.3
- Django 3.2
- Python 3.9
- Selenium 3.141.0

Implementado:

Pytest & Django
- Setup and Preparing
- Fixtures / Fixture Factory
- Factory Boy / Faker
- Towards Parametrizing Fixtures / Teste Functions


Pytest & Django with Selenium
- Intro Test with Pytest, Selenium and Django
- Taking Screenshots

Instalar:
- pip install -r requeriments.txt

Criar o Banco de Dados:
- python manage.py migrate

Execução:
- pytest # Test all
- pytest -x # Test at failure
- pytest -rP # Test with prints
- pytest tests # Test a folder
- pytest test/test_ex1.py::test_example # Test one test def
- pytest -m "slow" # Test slow
