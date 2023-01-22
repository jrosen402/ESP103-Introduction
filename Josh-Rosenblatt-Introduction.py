class Person:
    def __init__(self,sport,food_favorite,hobbies,hometown):
        self.sport = sport
        self.food_favorite = food_favorite
        self.hobbies = hobbies
        self.hometown = hometown




josh = Person('\nI enjoy tennis. I tore my ACL sophomore year and came back to win state.','\nMy favorite food is Chicken Alfredo.','\nMy hobbies are building computers and keyboards, working out and learning new things.','\nMy hometown is Omaha, Nebraska.')
loop_on=True
while loop_on:
    what_to_know = input('Enter what you would like to know about me - \nsport, favorite food, hobbies, hometown! Enter stop to finish the program.')
    if what_to_know.lower() == 'sport':
        print(josh.sport)

    elif what_to_know.lower() == 'favorite food':
        print(josh.food_favorite)

    elif what_to_know.lower() == 'hobbies':
        print(josh.hobbies)

    elif what_to_know.lower() == 'hometown':
        print(josh.hometown)

    elif what_to_know.lower()=='stop':
        print('Thank you for taking the time to get to know me!')
        loop_on =False
        break

    else:
        what_to_know = input('Enter what you would like to know about me - \nsport, favorite food, hobbies, hometown! Enter stop to finish the program.')




