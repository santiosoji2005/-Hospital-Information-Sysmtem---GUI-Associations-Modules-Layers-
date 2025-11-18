from Model.hospital_crud import HospitalCRUD

class HospitalController:
    def __init__(self):
        self.hospital_crud = HospitalCRUD()

    def create_hospital(self, name):
        return self.hospital_crud.create_hospital(name)

    def get_hospital(self, name):
        return self.hospital_crud.find_hospital(name)

    def get_all(self):
        return self.hospital_crud.list_hospitals()
