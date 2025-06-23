python.py/
├── Jenkinsfile
├── requirements.txt   # optional
└── tests/
    ├── test_sample.py
    ├── test_math.py
    └── test_strings.py
    
test_sample.py
    def test_basic():
    assert 2 + 2 == 4

    
    test_math.py
def test_subtract():
    assert 5 - 3 == 2

    

    test_strings.py 
def test_uppercase():
    assert 'hello'.upper() == 'HELLO'

    
