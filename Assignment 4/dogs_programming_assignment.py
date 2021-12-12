'''
  Programming Assignment For Module 5
  In this assignment you are going to define and use the object type called Dog.
  There won't be any interactive input for this program.

  Use the given program below.
  I have marked the places that you need to write your code with 'ADD CODE.'
  Don't change anything else in the given program below.

  Finally, the output of your program should be the following 15 lines as they appear below:
Breed               Count
=========================
Pitbull                 2
Great Dane              1

Total number of dogs: 4

Name: Chewy     Age: 2Week(s)   Breed: Pitbull
Name: *No Name* Age: 3Year(s)   Breed: Great Dane
Name: Fido      Age: 20Day(s)   Breed: Pitbull
Name: *No Name* Age: 2Month(s)  Breed: Unknown

Note: Chewy's age has been updated from 2W to 4W

Note: could not find a dog named Winston in the dog list
'''


class Dog:
    total_nbr_of_dogs = 0
    breed_type_count = {}  # count of each known breed type encountered

    @classmethod
    def update_total(cls):
        # ADD CODE
        cls.total_nbr_of_dogs += 1  # add 1 to the total number whenver new dog is created

    @classmethod
    def get_total(cls):
        # ADD CODE
        return cls.total_nbr_of_dogs

    @classmethod
    def update_breed_count(cls, breed):
        # ADD CODE
        if breed in cls.breed_type_count.keys():
            # add 1 if breed already in dictionary
            cls.breed_type_count[breed] += 1
        else:
            # initate a new breed in dictionary
            cls.breed_type_count[breed] = 1

    @classmethod
    def print_breed_type_count(cls):
        field_sep = ' '*15
        header = 'Breed' + field_sep + 'Count'
        line = '='*len(header)
        # Note: the print below prints the 2 header lines in the output
        print(f"{header}\n{line}")

        # ADD CODE
        for key, item in cls.breed_type_count.items():
            # key is left aligned and item right aligned
            print(f"{key : <12} {item :>12}")

    def __init__(self, param1, param2='Unknown', param3='*No Name*'):
        '''
         There are 3 formal parameters.
         They are listed in the order that they appear in formal parameter list below.
           age: A string of the following format:
                a positive_integer followed by a single character [Dd, Ww, Mm, Yy].
                Examples: '5Y': 5 years old,  '6w': 6 weeks old
                No need to do any error checking for the validity of the age
           breed: A string. Lower/upper/mixed cases should be considered the same.
                Example:'Great Dane' is same as 'great dane'
                If no breed is given, the dog's breed should be set to default value 'Unknown'
           name: a string. The name is case sensitive, don't change it.
                Example: "Fido' and 'fido' would be different dog names
                If no name is given, the dog's name should be set to default value'*No Name*'
        '''
        # ADD CODE
        self.age = param1.upper()
        self.breed = param2.title()
        self.name = param3

        Dog.update_total()  # update the total number of dogs as a new instance is created
        if self.breed != 'Unknown':
            Dog.update_breed_count(self.breed)

    def __str__(self):
        '''
         Override the __str__() so when print(dog) is called, it produces an output with following format:
         Name: dog-name Age: dog-age exactly as displayed below Breed: dog-breed capitalized
         Name: Chewy    Age: 2Week(s)   Breed: Pitbull
        '''
        # ADD CODE
        str1 = f"{'Name: ' + self.get_name() :<16}" + \
            f"{'Age: ' + self.get_age() :<16}" + f"{'Breed: ' + self.breed :<16}"
        return(str1)

    def get_age(self):
        # ADD CODE
        dict1 = {'W': 'Week(s)', 'D': 'Day(s)',
                 'M': 'Month(s)', 'Y': 'Year(s)'}
        return f"{self.age[0:-1]}{dict1[self.age[-1]]}"

    def update_age(self, age):
        # ADD CODE
        # No need to do any error checking for 'age', assume it is valid
        self.age = age.upper()

    def get_name(self):
        # ADD CODE
        return self.name


# The following is a helper function being called from main(). It is NOT a member of class Dog


def update_dog_age_and_print(dog_list, name, age):
    '''
     Update the 'age' for the dog with the given 'name' in my dog list, and output the following:
     Note: dog-name's age has been updated from old-value to new-value
     If the dog is not in the my dog list, output the following:
     Note: could not find a dog named dog-name in the dog list
    '''
    # ADD CODE
    for dog in dog_list:
        if name == dog.get_name():
            previous_age = dog.age
            dog.update_age(age)
            print(
                f"\nNote: {name}'s age has been updated from {previous_age} to {dog.age}")
            break
    else:
        print(f'\nNote: could not find a dog named {name} in the dog list')


def main():
    '''
     ADD CODE to create the following 4 dog instances:
     first dog: Dog('2W', 'Pitbull', 'Chewy')
     second dog: Dog('3Y', 'Great Dane')
     third dog: Dog('20D', 'PITBUll', 'Fido')
     fourth dog: Dog('2m')
    '''
    dogs = [('2W', 'Pitbull', 'Chewy'), ('3Y', 'Great Dane'),
            ('20D', 'PITBUll', 'Fido'), ('2m',)]
    my_dogs = []
    for dog in dogs:
        my_dogs.append(Dog(*dog))

    Dog.print_breed_type_count()

    print("\nTotal number of dogs: {}\n".format(Dog.get_total()))

    # print the info about all my dogs
    for d in my_dogs:
        print(d)

    update_dog_age_and_print(my_dogs, 'Chewy', '4w')

    update_dog_age_and_print(my_dogs, 'Winston', '5d')


if __name__ == "__main__":
    main()
