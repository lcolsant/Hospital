
class Patient(object):
    pat_id = 0
    def __init__(self, name, allergies, bed_num=0):
        
        self.name = name
        self.pat_id = Patient.pat_id
        self.allergies = allergies
        self.bed_num = bed_num

        Patient.pat_id+=1
        
    def display(self):
        print "pat_id:{}".format(self.pat_id)
        print "name:{}".format(self.name)
        print "allergies:{}".format(self.allergies)
        print "Bed number:{}".format(self.bed_num)
        return self

class Hospital(object):
    def __init__(self,name,capacity):
        patients = []        
        self.patients = patients
        self.name = name
        self.capacity = capacity
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(1, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self,patient):
        if len(self.patients)>=self.capacity:
            print 'Sorry, we are at maximum capacity'
        else: 
            #assign bed number
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]   
                    self.beds[i]["Available"] = False
                    break
            self.patients.append(patient)
            print "Patient #{}, {} admitted to bed #{}".format(patient.pat_id,patient.name, patient.bed_num)
        return self

    def discharge(self, patient_id):
        #free up bed first
        for patient in self.patients:
            if patient.pat_id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break
        #now remove patient
        self.patients.remove(patient)
        print 'patient:{}, has been removed.'.format(patient.name)
        return self

    def pat_show(self):
        print 'number of patients:{}'.format(len(self.patients))
        for i in self.patients:
            print i.name
        return self

patient1 = Patient('lee','none')
patient2 = Patient('kris','peanut')
patient3 = Patient('lilian','hay fever')
# patient1.display()

hospital1 = Hospital('good samaritan',200)
hospital1.admit(patient1)
hospital1.admit(patient2)
hospital1.admit(patient3)
# hospital1.pat_show()
hospital1.discharge(2)
hospital1.pat_show()



