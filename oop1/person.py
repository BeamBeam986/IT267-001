class person:
    conutry = "Thailand" #calss variable
    def __init__(self,name,gender,profession,hours) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours

    def work(self):
        print(f"{self.name}is woring as a {self.profession}")

    def study(self):
        print(f"{self.name} study for {self.hours}hour(s)")
    def show(self) -> None:
        print(f"Name: {self.name} Gnder:{self.gender} Profession :{self.profession} study: {self.study}")

#
jessa = person("Jeassa","Male","Software Engineer",10)
jessa.show()
jessa.work()
jessa.study()

#Personjon
jon = person("Jon","male","Doctor",15)
jon.show()
jon.work()
jon.study()

lalisa = person("larisa","female","koream Singer",13)
lalisa.work()


#assign vale
lalisa.conutry = 'korea'
print('=====')
print(f"Class Variable:{person.country}")
print(f"Instancea Variable: {lalisa.country}")
print(f"Instancea Variable: {jon.country}")