from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PrescriptionParser
from parser_patient_deatils import PatientParser

POPPLER_path = r'C:/poppler-23.01.0/Library/bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path,file_format):
    #file_path=r'docs/prescription/pre_1.pdf'
    pages = convert_from_path(file_path, poppler_path=POPPLER_path)
    document_txt =''
    if len(pages)>0:
        page = pages[0]
        pre_process_img = util.preprocess_image(page)
        text = pytesseract.image_to_string(pre_process_img, lang='eng')
        document_txt = '\n'+text


    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_txt).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientParser(document_txt).parse()
    else:
        raise Exception(f'Invalid File Format: {file_format}')
    return extracted_data
if __name__=='__main__':
    data = extract('../resources/patient_details/pd_2.pdf','patient_details')
    print(data)