from Model.doctor_crud import DoctorCRUD

class SearchController:
    def __init__(self, hospital_controller):
        self.hospital_controller = hospital_controller

    def search_by_dni(self, dni):
        for hospital in self.hospital_controller.get_all():
            doctor = DoctorCRUD.find_doctor_by_dni(hospital, dni)
            if doctor:
                return doctor, hospital
        return None
