class Test:
    subject = ""
    score_sheet = []
    pass_percent = 0
    def __init__(self,subject,score_sheet,pass_percent):
        self.subject = subject
        self.score_sheet = score_sheet
        self.pass_percent = pass_percent
class Student:
    __dict = {}
    def take_test(self,answers,test):
        correct_answers = 0
        total_quest = len(test.score_sheet)
        for answer,correct_answer in zip(answers,test.score_sheet):
            if answer == correct_answer:
                correct_answers += 1
        percent = (correct_answers/total_quest) * 100
        if percent >= test.pass_percent:
            self.__dict[test.subject] = f"Passed({percent})"
        else:
            self.__dict[test.subject] = f"Failed({percent})"
    def get_results(self):
        return self.__dict
t1 = Test(subject="Physics",score_sheet=['1B','2C','3A','4D','5A'],pass_percent=50)
s1 = Student()
s1.take_test(answers=['1C','2C','3B','4D','5A'], test=t1)
print(s1.get_results())
