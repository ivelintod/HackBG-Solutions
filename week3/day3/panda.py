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
        if self._gender == "male":
            return True
        return False

    def isFemale(self):
        if self._gender == "female":
            return True
        return False

    def __hash__(self):
        return hash(self._name + self._email + self._gender)


class PandaAlreadyError(Exception):
    pass


class PandaSocialNewtwork():

    def __init__(self, dict_panda):
        self.dict_panda = {}

    def __str__(self):
        return "Network: {}".format(self.dict_panda)

    def add_panda(self, panda):
        self.panda = panda
        if panda in self.dict_panda:
            raise PandaAlreadyError
        else:
            self.dict_panda[panda] = []

    def has_panda(self, panda):
        return panda in self.dict_panda

    def are_friends(self, panda1, panda2):
        return panda1 in self.dict_panda and panda2 in self.dict_panda

    def make_friends(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            raise Exception("Pandas Already Friends")

        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        self.dict_panda[panda2].append(panda1)
        self.dict_panda[panda1].append(panda2)

    def friends_of(self, panda):
        if panda in self.dict_panda:
            return self.dict_panda[panda]
        return False

    def connection_level(self, start, end):
        if self.are_friends(panda1, panda2):
            visited = set()
            queue = []
            # path_to[x] = y
            # if we go to x through y
            path_to = {}

            queue.append(start)
            visited.add(start)
            path_to[start] = None
            found = False
            path_length = 0

            while len(queue) != 0:
                current_node = queue.pop(0)
                if current_node == end:
                    found = True
                    break

                for neighbour in graph[current_node]:
                    if neighbour not in visited:
                        path_to[neighbour] = current_node
                        visited.add(neighbour)
                        queue.append(neighbour)
            if found:
                while path_to[end] is not None:
                    path_length += 1
                    end = path_to[end]

        print(json.dumps(path_to, sort_keys=True, indent=4))
        return path_length

    #def connection_level(self, panda1, panda2):





ivo = Panda("Ivo", "ivo_b@mail.bg", "male")
gay = Panda("Vlado", "vlado@abv.bg", "male")
gay2 = Panda("Gayster", "imnotgay@gmail.com", "female")
network = PandaSocialNewtwork({})
for panda in [ivo, gay, gay2]:
    network.add_panda(panda)
print(network)
print(network.friends_of(ivo))
print(network.has_panda(ivo))
print (ivo)

