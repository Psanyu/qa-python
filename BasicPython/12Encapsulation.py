class Student:
  def __init__(self, name):
    self.name = name
    print("Protected property using '_' before var name e.g. self.__name")
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())


class Person:
    def __init__(self, name):
        self.__name = name      # private

    def getname(self):         # GETTER — reads the value
        return self.__name

    def setname(self, name):   # SETTER — updates the value
        self.__name = name

p1 = Person("John")
print(p1.getname())    # John       ← reading via getter
p1.setname("Sam")      # updating via setter
print(p1.getname())


class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


# Create an object
S1 = ScoreBoard(0)

# Print the score
print(S1.get_score())
S1.set_score(10)
print(S1.get_score())




