'''
- Các lớp được xây dựng liên quan đến character bao gồm Person, Student, Teacher, Player.
- Sử dụng lập trình hướng đối tượng kế thừa đa cấp: Person->Studen->Player và Person->Teacher.
'''
init python:
    class Person:
        """lớp người"""
        def __init__(self, character, name,point, sex, age, biography):
            self.__c = character
            self.__name = name
            self.__point = point
            self.__sex = sex
            self.__age = age
            self.__biography = biography

        @property
        def c(self):
            return self.__c
        @c.setter
        def c(self,new_c):
            self.__c = new_c
        #-----name-----
        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self,new_name):
            self.__name = new_name

        #-----sex-----
        @property
        def sex(self):
            return self.__sex
        @sex.setter
        def sex(self,new_sex):
            self.__sex = new_sex

        #-----sacrificed-----
        @property
        def sacrificed(self):
            return self.__sacrificed
        @sacrificed.setter
        def sacrificed(self,new_sacrificed):
            self.__sacrificed = new_sacrificed
        #-----biography-----
        @property
        def biography(self):
            return self.__biography
        @biography.setter
        def biography(self,new_biography):
            self.__biography = new_biography

        #-----point-----
        @property
        def point(self):
            return self.__point

        @point.setter
        def point(self, new_point):
            self.point = new_point




    class Student(Person): # kế thừa lớp cha là Person
        """Lớp học sinh"""
        def __init__(self, character, name, point, sex, age, biography, MSSV, Degree, Class):
            Person.__init__(self,character, name, point, sex, age, biography)
            self.__MSSV = MSSV
            self.__Degree = Degree
            self.__Class = Class




        #-----------------Student-------------------------
    class Teacher(Person):
        """Lớp người"""
        def __init__(self,character, name,point, sex, age, biography,MSGV, Degree, Subjects):
            Person.__init__(self,character, name,point, sex, age, biography)
            self.__MSGV = MSGV
            self.__Degree = Degree
            self.__Subjects = Subjects


        #---------------------Player-----------------------
    class Player(Student):  #kế thừa lớp Student

        def __init__(self, character, name, point, sex, age, biography, MSSV, Degree, Class, health, intelligence,draw):
            Student.__init__(self,character, name, point, sex, age, biography,MSSV, Degree, Class)
            self.__health = health
            self.__intelligence = intelligence
            self.__draw = draw
    class Calendar(object):
        """Lịch"""
        def __init__(self, Session, Sessions, Day):
            self.Session = Session
            self.Sessions = Sessions
            self.Day = Day

        @property
        def output(self):
            return str(self.Sessions[self.Session]) + " ngày thứ "+ str(self.Day)

        def addtime(self, values):
            self.Session += values
            if self.Session > 3:
                self.Session -= 3 # Session = 3 => tối => remake về sáng = Chức năng sleep
                self.Day +=1


    class Place():
        """Vị trí"""
        def __init__(self, x, y, name, IsActive):
            # với tòa độ là (x,y), tên và tình trạng hoạt động True = đã đc mở ngược là chưa mở
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
