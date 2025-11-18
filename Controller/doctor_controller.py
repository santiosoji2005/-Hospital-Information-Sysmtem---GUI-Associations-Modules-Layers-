from Model.doctor_crud import DoctorCRUD

class DoctorController:
    def __init__(self, hospital_controller):
        self.hospital_controller = hospital_controller

    def add_doctor(self, hospital_name, name, speciality, dni):
        hospital = self.hospital_controller.get_hospital(hospital_name)
        if hospital is None:
            raise ValueError("El hospital no existe.")
        return DoctorCRUD.add_doctor(hospital, name, speciality, dni)
