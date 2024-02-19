class People:
    def __init__(display,name, age, interests):
        display.name = name
        display.age = age
        display.interests = interests

    def People(display):
        print(f"My name is {display.name} "
              f" I am {display.age} years old"
              f" and I enjoy {display.interests}")


myobj = People("Seanice Ochieng", "Eighteen", "Content creation")
myobj.People()
myobj2 = People("Peace Kanana", "Eighteen", "Computing and coding")
myobj2.People()
myobj3 = People("Amina Mohammed", "Twenty one", "Cooking and Flight Management")
myobj3.People()
myobj4 = People("Ivy Luseno", "Eighteen", "Medicine(maybe)")
myobj4.People()
myobj5 = People("Zawadi Terres", "Twelve", "Learning a lot!")  
myobj5.People()