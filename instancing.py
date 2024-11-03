

"""@file 333.cpp
 * @author Xiao Xiniang
 * @brief a program for defining classes
 * @version 0.1
 * @date 2024-11-03
 *  @copyright Copyright (c) 2024
 """
"""@brief instance these classes"""
from second_test import Teacher_t
from second_test import Student_t
from second_test import Course_t
Teacher1=Teacher_t("Isnel",30,"General English")
Teacher2=Teacher_t("Easter",36,"Advanced Mathmatucs")
Course1=Course_t("General English",Teacher1)
Course2=Course_t("Advanced Mathmatucs",Teacher2)
Student1=Student_t("Penelope",18,"大一")
Student2=Student_t("Aizel",20,"大三")
Student3=Student_t("Elodie",19,"大二")
Course1.addStudent(Student1)
Course1.addStudent(Student2)
Course2.addStudent(Student3)
Course1.showCaseInfo()
Course2.showCaseInfo()