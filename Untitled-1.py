class Patient:

    def __init__(self, patient_id, name, date_of_birth):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth


    def book_appointment(self):
        print("Appointment booked")

    def view_medical_record(self):
        print("Viewing medical record")

class Doctor:

    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def check_Patient(self):
        print("Checking patient")

    def update_Treatment(self):
        print("Updating treatment plan")

class Appointment:

    def __init__(self, appointment_id, Date, Status):
        self.appointment_id = appointment_id
        self.Date = Date
        self.Status = Status

    def schedule(self):
        print("Appointment scheduled")

    def cancel(self):
        print("Appointment canceled")

class MedicalRecord:

    def __init__(self, record_id, History, Last_update):
        self.record_id = record_id
        self.History = History
        self.Last_update = Last_update

    def add_entry(self):
        print("Adding entry to medical record")

    def view_History(self):
        print("Viewing medical history")

class Treatment:

    def __init__(self, treatment_id, Description, Date):
        self.treatment_id = treatment_id
        self.Description = Description
        self.Date = Date

    def start_treatment(self):
        print("Starting treatment")

    def Complete_treatment(self):
        print("Completing treatment")

class Prescription:

    def __init__(self, prescription_id, Date, Instructions):
        self.prescription_id = prescription_id
        self.Date = Date
        self.Instructions = Instructions

    def create_prescription(self):
        print("Creating prescription")

    def update_prescription(self):
        print("Updating prescription")

class Bill:
    
    def __init__(self, bill_id, Amount, Payment_status):
        self.bill_id = bill_id
        self.Amount = Amount
        self.Payment_status = Payment_status

    def Calculate_total(self):
        print("Calculating total amount")

    def Process_payment(self):
        print("Processing payment")

class Hospital_Room:

    def __init__(self, room_id, Room_Number, Room_type):
        self.room_id = room_id
        self.Room_Number = Room_Number
        self.Room_type = Room_type

    def Assign_room(self):
        print("Assigning hospital room")

    def Release_room(self):
        print("Releasing hospital room")  

class Lab_Test:

    def __init__(self, test_id, Test_name, Result):
        self.test_id = test_id
        self.Test_name = Test_name
        self.Result = Result

    def Request_test(self):
        print("Requesting lab test")

    def Record_result(self):
        print("Recording lab test result") 

class medicine:

    def __init__(self, medicine_id, Name, Dosage):
        self.medicine_id = medicine_id
        self.Name = Name
        self.Dosage = Dosage

    def check_stock(self):
        print("Checking medicine stock")

    def Update_stock(self):
        print("Updating medicine stock")


patient1 = Patient(101, "Abrar", "2005-01-01")
doctor1 = Doctor(201, "Dr Ahmed", "Cardiology")

appointment1 = Appointment(301, "2026-11-18", "Booked")
room1 = Hospital_Room(401, "R101", "Private")

treatment1 = Treatment(501, "Heart Checkup", "2026-11-18")
medicine1 = medicine(601, "Paracetamol", "500mg")

prescription1 = Prescription(701, "2026-11-18", "Take after food")
bill1 = Bill(801, 500, "Pending")

lab1 = Lab_Test(901, "Blood Test", "Normal")
record1 = MedicalRecord(1001, "Patient History", "2026-11-18")


# The patient is connected to the services he receives.
patient1.appointments = [appointment1]
patient1.medical_record = record1
patient1.treatment = treatment1
patient1.prescription = prescription1
patient1.bill = bill1
patient1.lab_test = lab1
patient1.room = room1

# The doctor is responsible for the patient's treatment and tests.
doctor1.appointments = [appointment1]
doctor1.patients = [patient1]
doctor1.treatments = [treatment1]
doctor1.prescriptions = [prescription1]
doctor1.lab_tests = [lab1]

# Abrar and Dr Ahmed are linked through his appointment.
appointment1.patient = patient1
appointment1.doctor = doctor1

# The doctor provides the treatment for Abrar.
treatment1.patient = patient1
treatment1.doctor = doctor1

# The prescription is given by Dr Ahmed and includes Paracetamol.
prescription1.patient = patient1
prescription1.doctor = doctor1
prescription1.medicines = [medicine1]

# Other records belong to Abrar.
bill1.patient = patient1
record1.patient = patient1
lab1.patient = patient1
lab1.doctor = doctor1
room1.patient = patient1


print("Hospital record")
print("---------------")

print(patient1.name, "is a patient.")
print("His date of birth is", patient1.date_of_birth)
print()

print(patient1.name, "is under the care of", doctor1.name)
print(doctor1.name, "works in the", doctor1.specialty, "department.")
print()

print(patient1.name, "has an appointment with", doctor1.name)
print("The appointment date is", appointment1.Date)
print("The appointment is", appointment1.Status.lower())
print("The treatment is", treatment1.Description)
print()

print(patient1.name, "has medical record", record1.record_id)
print("The medical record was last updated on", record1.Last_update)
print()

print(doctor1.name, "prescribed", medicine1.Name, "for", patient1.name)
print("The dosage is", medicine1.Dosage)
print("The instructions are:", prescription1.Instructions)
print()

print(patient1.name, "is staying in room", room1.Room_Number)
print("This is a", room1.Room_type.lower(), "room.")
print()

print(doctor1.name, "requested the", lab1.Test_name, "for", patient1.name)
print("The lab test result is", lab1.Result)
print()

print(patient1.name, "has a", bill1.Payment_status.lower(), "bill")
print("The bill amount is", bill1.Amount)
