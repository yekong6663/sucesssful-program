"""@file 333.cpp
 * @author Xiao Xiniang
 * @brief a program for defining classes
 * @version 0.1
 * @date 2024-11-03
 *  @copyright Copyright (c) 2024
 """
"""@brief create a Perason-t class"""
class Person_t():
    """
    @biref initialize the Person_t class
    @param self parameter self
    @param name parameter name
    @param age parameter age
    @returen None
    """
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    """
    @biref create a introduction method
    @param self parameter self
    @returen 姓名:{self.name},年龄:{self.age}
    """
    def introducePerson(self):
        return f"姓名:{self.name},年龄:{self.age}"
"""@brief create a Teacher-t class inherited from Person_t class"""
class Teacher_t(Person_t):
    """
    @biref initialize the Teacher_t class
    @param self parameter self
    @param name parameter name
    @param age parameter age
    @param subject parameter subject
    @returen None
    """
    def __init__(self,name:str,age:int,subject:str):
        super().__init__(name,age)
        self.subject=subject
    """
    @biref recreate a introduction method
    @param self parameter self
    @returen 姓名:{self.name},年龄:{self.age},教授科目:{self.subject}
    """
    def introducePerson(self):
        return f"姓名:{self.name},年龄:{self.age},教授科目:{self.subject}"
"""@brief create a Student-t class inherited from Person_t class"""
class Student_t(Person_t):
    """
    @biref initialize the Student_t class
    @param self parameter self
    @param name parameter name
    @param age parameter age
    @param grade parameter grade
    @returen None
    """
    def __init__(self,name:str,age:int,grade:str):
         super().__init__(name,age)
         self.grade=grade
    """
    @biref recreate a introduction method
    @param self parameter self
    @returen 姓名:{self.name},年龄:{self.age},年级:{self.grade}
    """
    def introducePerson(self):
        return f"姓名:{self.name},年龄:{self.age},年级:{self.grade}"

