import re

class Panda():
    def __init__(self, name, email, gender):
        self._name = name
        self.set_email(email)
        self._gender = gender


    def __str__(self):
        return "Panda's name, email and gender are {}, {}, {}".format(self._name, self._email, self._gender)

    def __repr__(self):
        return "Panda('{}' - '{}'' - '{}')".format(self._name, self._email, self._gender)

    def name(self):
        return self._name

    def set_email(self, email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            raise ValueError
        self._email = email

    def __eq__(self, other):
        equal_names = self._name == other._name
        equal_emails = self._email == other._email
        equal_genders = self._gender == other._gender
        return equal_names and equal_emails and equal_genders

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return self._gender == "female"

    def __hash__(self):
        return hash(self._name + self._email + self._gender)


class PandaAlreadyError(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class SocialNetwork:

    def __init__(self):
        self.network = {}
        self.count_levels = 1
        self.visited = []

    def __str__(self):
        return str(self.network)

    def add_panda(self, panda):
        if panda not in self.network.keys():
            self.network[panda] = []
        else:
            raise PandaAlreadyError

    def has_panda(self, panda):
        flag = panda in self.network.keys()
        return flag

    def make_friends(self, panda1, panda2):
        if panda1 not in self.network.keys():
            self.add_panda(panda1)
        elif panda2 not in self.network.keys():
            self.add_panda(panda2)
        elif panda1 and panda2 not in self.network.keys():
            self.add_panda(panda1)
            self.add_panda(panda2)
        if panda2 not in self.network[panda1]:
            self.network[panda1].append(panda2)
        if panda1 not in self.network[panda2]:
            self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        flag = panda1 in self.network.keys() and panda2 in self.network[panda1]
        return flag

    def friends_of(self, panda):
        if panda in self.network.keys():
            return self.network[panda]
        else:
            return False

    def connection_level(self, panda1, panda2):
        if panda1 not in self.network.keys() or panda2 not in self.network.keys():
            return False
        else:
            if panda2 in self.network[panda1]:
                return self.count_levels
            else:
                self.count_levels += 1
                self.visited.append(panda1)
                for panda in self.network[panda1]:
                    if panda not in self.visited:
                        return self.connection_level(panda, panda2)



p1 = Panda('Ivo', 'alo@exa.com', 'male')
p2 = Panda('Ivo', 'loa@exa.com', 'male')
p3 = Panda('Rado', 'lqlql@avwa.com', 'male')
p4 = Panda('Vlad', 'slab@slab.bg', 'female')
p5 = Panda('Ceco', 'gei@geivoe.bg', 'female')

sn = SocialNetwork()
sn.add_panda(p1)
sn.make_friends(p1, p2)
sn.make_friends(p2, p3)
sn.make_friends(p4, p5)
print(sn.connection_level(p1, p5))
