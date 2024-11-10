from binary_search_tree import *

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
        pass
    def build_tree_from_csv(self, file_path): #Reads patient data from a CSV file and populates the BST.
        #need to do the file reading stuff 
        pass
    def visualize_tree(self): #Visualizes the BST using Graphviz.
        # need to do the vs code plug in stuff 
        pass
    def _add_nodes(self, dot, node): #A helper method that recursively adds nodes and edges to the Graphviz object.
        pass
