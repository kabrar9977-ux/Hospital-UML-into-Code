# Hospital UML into Code

This project shows how a hospital UML diagram can be converted into Python classes and objects.

## Description

The program creates a hospital patient, doctor, appointment, treatment, prescription, medicine, room, laboratory test, bill, and medical record.

It also shows the relationships between these objects in simple human-written text.

## Classes

The program contains the following classes:

- `Patient`
- `Doctor`
- `Appointment`
- `MedicalRecord`
- `Treatment`
- `Prescription`
- `Bill`
- `Hospital_Room`
- `Lab_Test`
- `medicine`

## Objects

The program creates one example object for each class:

- Patient: Abrar
- Doctor: Dr Ahmed
- Appointment: 301
- Treatment: Heart Checkup
- Prescription: 701
- Medicine: Paracetamol
- Bill: 801
- Room: R101
- Laboratory Test: Blood Test
- Medical Record: 1001

## Relationships

- A patient has appointments, a medical record, treatment, a prescription, a bill, a lab test, and a room.
- A doctor has patients, appointments, treatments, prescriptions, and lab tests.
- An appointment belongs to a patient and a doctor.
- A treatment belongs to a patient and is given by a doctor.
- A prescription belongs to a patient and is created by a doctor.
- A medicine is included in a prescription.
- A bill, medical record, and lab test belong to a patient.
- A room can be assigned to a patient.

## Requirements

- Python 3

## How to Run

Open a terminal in the project folder and run:

```powershell
python Untitled-1.py
```

## Example Output

```text
Hospital record
---------------
Abrar is a patient.
His date of birth is 2005-01-01

Abrar is under the care of Dr Ahmed
Dr Ahmed works in the Cardiology department.

Abrar has an appointment with Dr Ahmed
The appointment date is 2026-11-18
The appointment is booked
The treatment is Heart Checkup

Abrar has medical record 1001
The medical record was last updated on 2026-11-18

Dr Ahmed prescribed Paracetamol for Abrar
The dosage is 500mg
The instructions are: Take after food

Abrar is staying in room R101
This is a private room.

Dr Ahmed requested the Blood Test for Abrar
The lab test result is Normal

Abrar has a pending bill
The bill amount is 500
```
