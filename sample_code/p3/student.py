class Score:
    def __init__(self, chinese, english, math, society, nature, note=''):
        self.__chinese = chinese
        self.__english = english
        self.__math = math
        self.__society = society
        self.__nature = nature
        self.__note = note
        
    @classmethod
    def from_tuple(cls, tuple_):
        return cls(*tuple_)
    
    @classmethod
    def copy(cls, obj):
        return cls(
            obj.chinese,
            obj.english,
            obj.math,
            obj.society,
            obj.nature,
            obj.note
        )
    
    @property
    def chinese(self): return self.__chinese
    
    @property
    def english(self): return self.__english
    
    @property
    def math(self): return self.__math
    
    @property
    def society(self): return self.__society
    
    @property
    def nature(self): return self.__nature
    
    @property
    def note(self): return self.__note
    
    
class Student:
    def __init__(self, id, name, score):
        self.__id = id
        self.__name = name
        self.__score = score
        
    @classmethod
    def from_score_tuple(cls, id, name, tuple_):
        return cls(id, name, Score.from_tuple(tuple_))
    
    # Override
    def __str__(self):
        return ('===================\n' +
                'Score of GSAT      \n' +
                '-------------------\n' +
                'Name: %s           \n'%(self.__name) +
                '  Id: %s           \n'%(self.__id) +
                '                   \n' +
                'Chinese: %d        \n'%(self.__score.chinese) +
                'English: %d        \n'%(self.__score.english) +
                '   Math: %d        \n'%(self.__score.math) +
                'Society: %d        \n'%(self.__score.society) +
                ' Nature: %d        \n'%(self.__score.nature) +
                '===================\n'
        )
        
    @property
    def id(self): return self.__id
    
    @property
    def name(self): return self.__name
    
    @property
    def score(self): return Score.copy(self.__score)
    
    @property
    def chinese(self): return self.__score.chinese
    
    @property
    def english(self): return self.__score.english
    
    @property
    def math(self): return self.__score.math
    
    @property
    def society(self): return self.__score.society
    
    @property
    def nature(self): return self.__score.nature
    
    @property
    def note(self): return self.__score.note
    
    
if __name__ == '__main__':
    score_1 = Score(10, 12, 8, 14, 10)
    score_1_copy = Score.copy(score_1)
    print(score_1, score_1_copy, score_1 is not score_1_copy)
    
    student_1 = Student('0000000', 'student_1', score_1)
    print(student_1)
    
    tuple_ = (10, 10, 12, 11, 13)
    score_2 = Score.from_tuple(tuple_)
    student_2 = Student('11111111', 'ooooo', score_2)
    print(student_2)
    
    tuple_ = (11, 8, 12, 11, 10)
    student_3 = Student.from_score_tuple('22222222', 'xxx', tuple_)
    print(student_3)