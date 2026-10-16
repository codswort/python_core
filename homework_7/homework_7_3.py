class Doctor:
    def treat(self):
        print("Доктор")

class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")

class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")

class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит общее исследование и назначает специалистов")

    def doctor_for_patient(self, patient):
        if patient.get_treatment_plan() == 1:
            patient.set_doctor(Surgeon())
        elif patient.get_treatment_plan() == 2:
            patient.set_doctor(Dentist())
        else:
            patient.set_doctor(Therapist())

        patient.get_doctor().treat()

class Patient:
    def __init__(self, treatment_plan):
        self.__treatment_plan = treatment_plan
        self.__doctor = None

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def get_doctor(self):
        return self.__doctor

    def get_treatment_plan(self):
        return self.__treatment_plan

print("Пациет 1:")
patient = Patient(1)
therapist = Therapist()
therapist.doctor_for_patient(patient)

print("\nПациет 2:")
patient = Patient(2)
therapist = Therapist()
therapist.doctor_for_patient(patient)

print("\nПациет 3:")
patient = Patient(3)
therapist = Therapist()
therapist.doctor_for_patient(patient)
