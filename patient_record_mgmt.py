# Benjamin Guth 

from binary_search_tree import *
import csv

class PatientRecord: 

    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id 
        self.name = name 
        self.ago = age
        self.diagnosis = diagnosis 
        self.blood_pressure = blood_pressure 
        self.pulse = pulse 
        self.body_temperature = body_temperature


class PatientRecordManagementSystem :

    def __init__(self): #Initializes the patient record management system with an empty BST.
        self.patient_record_management_BST = BinarySearchTree()
        
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        new_patient_record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        node_of_that = Node(new_patient_record.patient_id, new_patient_record)
        self.patient_record_management_BST.insert(node_of_that)

    def search_patient_record(self, patient_id):
        return self.patient_record_management_BST.search(patient_id).value
        
    def delete_patient_record(self, patient_id):
        self.patient_record_management_BST.remove(patient_id)
        
    def display_all_records(self): #Displays all patient records in the BST using inorder traversal.
        #need to build that command first on the bst
        
        my_inorder_list = self.patient_record_management_BST.inorder_traversal()

        for a_p in my_inorder_list:
            print (a_p)

        return my_inorder_list
        
    def build_tree_from_csv(self, file_path): #Reads patient data from a CSV file and populates the BST.
        #need to do the file reading stuff 
        # reading the cvs file
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)
            # PatientID,Name,Age,Diagnosis,BloodPressure,Pulse,BodyTemperature
            # consider adding a check here rather than just a line skip

            # one line at a time create a patientrecord
            for line in csv_reader:
                #print(line)
                #current_patient = PatientRecord(line)
                self.add_patient_record(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                # 10,Professor X,29,Pneumonia,130/85,75,37.3
                # might need to split this up for this to work
                #add the patient to the tree
                
        return True
        

    def visualize_tree(self): #Visualizes the BST using Graphviz.
        # need to do the vs code plug in stuff 
        pass
    def _add_nodes(self, dot, node): #A helper method that recursively adds nodes and edges to the Graphviz object.
        pass


# file_path 
# "data/patient_records.csv"