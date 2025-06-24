python-multi-test/
├── app/
│   └── calculator.py
├── tests/
│   ├── test_addition.py
│   ├── test_subtraction.py
│   └── test_division.py
├── requirements.txt
└── Jenkinsfile

    def add(a, b): return a + b
def subtract(a, b): return a - b
def divide(a, b): return a / b if b != 0 else None

from app.calculator import add

def test_add():
    assert add(3, 4) == 7

from app.calculator import subtract

def test_subtract():
    assert subtract(10, 3) == 7

from app.calculator import divide

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) is None
