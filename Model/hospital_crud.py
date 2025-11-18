from Model.hospital import Hospital

class HospitalCRUD:

    def __init__(self):
        self.hospitals = []

    def create_hospital(self, hospital_name):
        if self.find_hospital(hospital_name) is not None:
            raise ValueError("El hospital ya existe.")
        h = Hospital(hospital_name)
        self.hospitals.append(h)
        return h

    def find_hospital(self, hospital_name):
        for h in self.hospitals:
            if h.hospital_name == hospital_name:
                return h
        return None

    def list_hospitals(self):
        return self.hospitals
