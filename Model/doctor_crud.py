from Model.doctor import Doctor

class DoctorCRUD:

    @staticmethod
    def add_doctor(hospital, doctor_name, speciality, dni):
        for d in hospital.doctors:
            if d.dni == dni:
                raise ValueError("El doctor con ese DNI ya existe.")
        doctor = Doctor(doctor_name, speciality, dni)
        hospital.doctors.append(doctor)
        return doctor

    @staticmethod
    def find_doctor_by_dni(hospital, dni):
        for doctor in hospital.doctors:
            if doctor.dni == dni:
                return doctor
        return None
