class Student:
  def data(self):
    self.name = str(input("Enter student's name :"))
    self.reg_no = (input("Enter registration number :"))
    self.age = int(input("Enter student's age :"))
    self.gender = str(input("Enter student's gender :"))
    self.branch = str(input("Enter student's branch :"))
    self.semester = int(input("Enter semester :"))

  def display(self):
    print(f"\n Name: {self.name}\n Reg. no: {(self.reg_no)}\n Age: {(self.age)}\n Gender:{self.gender}\n Branch: {self.branch}\n Semester: {self.semester}")

class StudentResultInfo(Student):
  def init(self, totalMarks, percentage, grade):
    self.totalMarks = totalMarks
    self.percentage = percentage
    self.grade = grade

  def displayData(self):
    print("\n\n INFORMATION OF STUDENTS")
    self.display()
    print(f"\n RESULTS \n\n Total marks: {(self.totalMarks)}\n Percentage: {(self.percentage)} % Grade: {self.grade}")

std1 = StudentResultInfo(1000, 97, 'A+')
std1.data()
std1.display()
std1.displayData()

#####################################################################

class PDFs:
  def _init_(self, creator, description, size):
    self.creator = creator
    self.description = description
    self.size = size

  def displayInfo(self):
    print("Created by:",self.creator)
    print("Description:", self.description)
    print("File size (in KBs):", self.size)

  def sizeLimit(self):
    if self.size > 300:
      print("Size exceeds threshold.\n")
    else:
      print("Size is within the threshold.\n")

class Pictures(PDFs):
  def _init_(self, creator, description, size, dimension):
    super()._init_(creator, description, size)
    self.dimension = dimension

  def displayPicInfo(self):
    self.displayInfo()
    print("Dimensions (in pixels):", self.dimension)

  def dimensionLimit(self):
    if self.dimension>3000:
      print(" high dimension!\n")
    else:
      print(" dimensions are fine.\n")
      
pdf1 = PDFs("123XYZ", "123ABC", 15.2)
pdf1.displayInfo()
pdf1.sizeLimit()
print()
img = Pictures("XYZ", "ABCD", 75928, 2758)
img.displayPicInfo()
img.dimensionLimit()


#################################################################################

class Vehicle:
    def _init_(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def cap(self):
        return self.capacity * 150

class Bus(Vehicle):
    def _init_(self, name, mileage, capacity=80):
        Vehicle._init_(self, name, mileage, capacity)
        self.finalAmount = Vehicle.cap(self) * 2.2

    def busFare(self):
        print(f"Total Fare : {self.finalAmount}")

car1 = Vehicle("Swift", 40, 10)
print(f"Car Fare : {car1.cap()}")
bus1 = Bus("Airavata", 20, 60)
bus1.busFare()
