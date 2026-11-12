#import doctors.doctor_detail as d 
from doctors.doctor_detail import *
from patients.details import get_patient_details
from patients.registration import register_patient


patient = get_patient_details()
doctor = get_doctor()
print(patient)
print(doctor)

register_patient("sai",  21)

