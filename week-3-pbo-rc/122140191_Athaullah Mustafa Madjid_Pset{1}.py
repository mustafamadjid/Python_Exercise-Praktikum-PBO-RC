from random import sample

class Father:
    def __init__(self):
        self.father_type = input("Enter the father's blood type : ").upper()
 

class Mother:
    def __init__(self):
        self.mother_type = input("Enter the mother's blood type : ").upper()
    
 

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        

    def child_blood_type(self):
        temp_list = list(self.father_type + self.mother_type)
        
        child_allele = ""
        
        child_allele_sample = sample(temp_list,2)
        for i in child_allele_sample:
            child_allele += i
        
        
        print(f"Child's allele  : {child_allele}")
        
        child_blood_type = {
            "AA" : "A",
            "AO" : "A",
            "AB" : "AB",
            "BB" : "B",
            "BO" : "B",
            "OO" : "O",
            "OA" : "A",
            "BA" : "AB",
            "OB" : "B",
            "AO" : "A"
        }
        
        for allele,child_blood in child_blood_type.items():
            if child_allele == allele:
                print(f"Child's Blood Type   : {child_blood}")

            
c = Child()
c.child_blood_type()


