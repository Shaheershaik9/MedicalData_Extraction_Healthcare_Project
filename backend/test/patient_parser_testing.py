from backend.src.parser_patient_deatils import PatientParser
import pytest

@pytest.fixture()
def doc_1():
    document_text = '''
    17/12/2020

Patient Medical Record . : :

Patient Information

Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight:
9264 Ash Dr 95
New York City, 10005 a
United States Height:
190
In Case of Emergency
ee oe
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
I i
Chicken Pox (Varicella): Measies:
IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine'''
    return PatientParser(document_text)
@pytest.fixture()
def doc_2():
    document_text='''
    Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

- eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020
'''
    return PatientParser(document_text)

def test_get_name(doc_1,doc_2):

    assert doc_1.get_patient_name() == 'Kathy Crawford'
    assert doc_2.get_patient_name() == 'Jerry Lucas'

def test_phnumber(doc_1,doc_2):
    assert doc_1.get_patient_phNumber() == '(737) 988-0851'
    assert doc_2.get_patient_phNumber() == '(279) 920-8204'

def test_medical_prblms(doc_1,doc_2):
    assert doc_1.get_patient_medical_prblms() == 'Migraine'
    assert doc_2.get_patient_medical_prblms() == 'N/A\n\n7?\nv\n\n17/12/2020'

def test_vachine(doc_1,doc_2):
    assert doc_1.get_patient_vachine() == 'No'
    assert doc_2.get_patient_vachine() == 'Yes'