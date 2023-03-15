class School:
    schoolName = "East High"
    location = "Salt Lake City"
    schoolType = "High School"

    def schoolInfo(self):
        enter_name = input("Enter your school's name: ")
        enter_location = input("Enter your school's location: ")
        enter_type = input("Enter what kind of school you go to: ")
        if (enter_location == self.location and enter_type == self.schoolType):
            print("Welcome to, {}!".format(enter_name))
        else:
            print("Doesn't look like you go to this school")

#Child class teacher
class Teacher(School):
    county = "Salt Lake County"
    basePay = 45.00
    classes = 12

    def schoolInfo(self):
        enter_name = input("Enter your school's name: ")
        enter_county = input("Enter the county your school is in: ")
        enter_type = input("Enter what kind of school you go to: ")
        if (enter_county == self.county and enter_type == self.schoolType):
            print("Welcome to, {}!".format(enter_name))
        else:
            print("Doesn't look like your school is in this area")


if __name__ == "__main__":
    student = School()
    student.schoolInfo()

    professor = Teacher()
    professor.schoolInfo()