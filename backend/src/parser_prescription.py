from praser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):

    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
         return {
                 'patient_name': self.get_field('patient_name'),
                 'patient_address': self.get_field('patient_address'),
                 'patient_medicines': self.get_field('patient_medicines'),
                 'patient_directions': self.get_field('patient_directions'),
                 'patient_refill': self.get_field('patient_refill')
                }

    def get_field(self,field_name):

        pattern_dict = {
                        'patient_name':{'pattern': 'Name:.(.*)Date','flags':0},
                        'patient_address':{'pattern': "Address:(.*)\n", 'flags':0},
                        'patient_medicines':{'pattern': "Address:[^\n]*(.*)Directions", 'flags':re.DOTALL},
                        'patient_directions':{'pattern': "Directions:(.*)Refill", 'flags' : re.DOTALL},
                        'patient_refill':{'pattern': "Refill:.(.*).times", 'flags' : re.DOTALL},

                        }

        pattern_obj=pattern_dict.get(field_name)
        if pattern_obj:
            matches= re.findall(pattern_obj['pattern'],self.text,flags=pattern_obj['flags'])
            if len(matches) > 0:
                return matches[0].strip()



if __name__=='__main__':

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

    p = PrescriptionParser(document_text)
    print(p.parse())