# Test-driven development (TDD), also called test-driven design,
# is a method of implementing software programming that interlaces unit testing,
# programming and refactoring on source code.
from backend.src.parser_prescription import PrescriptionParser
import pytest
@pytest.fixture()
def doc_1():
    document_text = '''
    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC



    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times'''
    return PrescriptionParser(document_text)
@pytest.fixture()
def doc_2():
    document_text='''
    Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times
'''
    return PrescriptionParser(document_text)
@pytest.fixture()
def doc3_empty():
    return PrescriptionParser('')
def test_get_name(doc_1,doc_2,doc3_empty):

    assert doc_1.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2.get_field('patient_name') == 'Virat Kohli'
    assert doc3_empty.get_field('patient_name') == None

def test_get_address(doc_1,doc_2):

    assert doc_1.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2.get_field('patient_address') == '2 cricket blvd, New Delhi'

def test_get_medicines(doc_1,doc_2):
    assert doc_1.get_field('patient_medicines') == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert doc_2.get_field('patient_medicines') == '| Omeprazole 40 mg'

def test_get_direction(doc_1,doc_2):
    assert doc_1.get_field('patient_directions') == ('Prednisone, Taper 5 mg every 3 days,\n'
 '    Finish in 2.5 weeks a\n'
 '    Lialda - take 2 pill everyday for 1 month')
    assert doc_2.get_field('patient_directions') == 'Use two tablets daily for three months'

def test_get_refill(doc_1,doc_2):
    assert doc_1.get_field('patient_refill') == '2'
    assert doc_2.get_field('patient_refill') == '3'


def test_parse(doc_1,doc_2,doc3_empty):
    record_maria = doc_1.parse()
    assert record_maria['patient_name'] == 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['patient_medicines'] == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert record_maria['patient_directions'] == ('Prednisone, Taper 5 mg every 3 days,\n'
                                                     '    Finish in 2.5 weeks a\n'
                                                     '    Lialda - take 2 pill everyday for 1 month')
    assert record_maria['patient_refill'] == '2'

    record_virat = doc_2.parse()
    assert record_virat['patient_name'] == 'Virat Kohli'
    assert record_virat['patient_address'] == '2 cricket blvd, New Delhi'
    assert record_virat['patient_medicines'] == '| Omeprazole 40 mg'
    assert record_virat['patient_directions'] == 'Use two tablets daily for three months'
    assert record_virat['patient_refill'] == '3'

    record_empty = doc3_empty.parse()

    assert record_empty == {
        'patient_name':None,
        'patient_address':None,
        'patient_medicines':None,
        'patient_directions':None,
        'patient_refill':None
    }





