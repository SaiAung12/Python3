class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_number):
    print("Number of students in {} school has set to {}.".format(self.name, self.numberOfStudents))
    self.numberOfStudents = new_number

  def __repr__(self):
    print("A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name = self.name, numberOfStudents = self.numberOfStudents))

new_school = School("BEHS4", "High", "500")

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name,"Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}.format(pickupPolicy = self.pickupPolicy)"


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    if isinstance(sportsTeams, list):
      self.sportsTeams = sportsTeams
    else:
      return "Error"
  def getSportsTeams(self):
    return self.sportsTeams
    
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)
