
class Course:
    
    def __init__(self,id,name,price,is_cool):
        self.id = id
        self.name = name
        self.price = price
        self.is_cool = is_cool
        
    def __str__(self):
        return f"ID : {self.id} \
            NAME : {self.name} \
            # PRICE {self.price} \
            # IS_COOL {self.is_cool} "
    
    
with open("db.txt", 'r') as file:
    d = file.readlines()
    courses = []
    
    for element in d: 
        item = element.split("#")
        course = Course(item[0].strip(), item[1].strip(),item[2].strip(),item[3].strip())
        courses.append(course)
    
    print(courses[0].__dict__)
    

        
        
    
    