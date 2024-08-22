from student import Student

class Department:
    def __init__(self, quota, scoring):
        self.__students = []
        self.__quota = quota
        self.__scoring = scoring
        
    def add_student(self, student):
        self.__students.append(student)
        
    def result(self):
        sorted_score = sorted(self.__students, key=lambda s: -self.__scoring(s))
        admin_list = sorted_score[:self.__quota]
        return [s.id for s in admin_list]
    
    @property
    def students(self): return self.__students[:]
    
    @property
    def quota(self): return self.__quota
    

def scoring_1(student:Student):
    score = student.score
    return (
        score.chinese + 
        score.english +
        score.math    +
        score.society +
        score.nature
    )
    
def scoring_2(student:Student):
    score = student.score
    return (
        score.chinese     + 
        score.english * 2 +
        score.math * 4    +
        score.nature * 2
    )      
    
    
if __name__ == '__main__':
    
    import random
    
    department_1 = Department(6, scoring_1)
    department_2 = Department(5, scoring_2)
    
    score_list = [tuple([random.randint(1,15) for _ in range(5)]) for _ in range(10)]
    student_list = [Student.from_score_tuple(i, i, t) for i, t in enumerate(score_list, 1130926)]
    
    for s in student_list:
        department_1.add_student(s)
        department_2.add_student(s)
        
    print(department_1.result())
    print(department_2.result())