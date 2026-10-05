class school:
    school_name= " Cpa High SChool"
    @staticmethod
    def school_grade(marks):
        if marks >= 90:
            return 'A+'
        else:
            return 'B+'
print (school.school_grade(35))