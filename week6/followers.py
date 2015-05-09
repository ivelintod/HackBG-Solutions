from graph import DirectedGraph
import requests
import json


class Followers:

    def __init__(self, user, graph_level):
        self.user = user
        self.graph_level = graph_level
        self.graph = DirectedGraph()
        self.count = 0

    def make_request_for_following(self, user):
        req = requests.get('https://api.github.com/users/{}/following?client_id=0b3e4375406c41dc35d9&client_secret=3bd22641e8ac794765f8bdf59c193c6b9bf3b2e8'.format(user))
        json_info = req.json()
        return json_info

    def make_request_for_followers(self, user):
        req = requests.get('https://api.github.com/users/{}/followers?client_id=0b3e4375406c41dc35d9&client_secret=3bd22641e8ac794765f8bdf59c193c6b9bf3b2e8'.format(user))
        json_info = req.json()
        return json_info

    def to_JSON_followers(self, user):
        with open('{} followers.json'.format(user), 'w') as username_info:
            json.dump(self.make_request_for_followers(user), username_info)

    def to_JSON_following(self, user):
        with open('{} following.json'.format(user), 'w') as username_info:
            json.dump(self.make_request_for_following(user), username_info)

    def JSON_loads_followers(self, user):
        with open('{} followers.json'.format(user), 'r') as username_info:
            contents = username_info.read()
            info = json.loads(contents)
            return info

    def JSON_loads_following(self, user):
        with open('{} following.json'.format(user), 'r') as username_info:
            contents = username_info.read()
            info = json.loads(contents)
            return info

    def populate_forward(self, user):
        self.to_JSON_following(user)
        initial_user_following = self.JSON_loads_following(user)
        for users in initial_user_following:
            self.graph.add_edge(user, users['login'])

    def populate_forward_followers(self, user):
        self.to_JSON_followers(user)
        initial_user_followers = self.JSON_loads_followers(user)
        for users in initial_user_followers:
            self.graph.add_edge(user, users['login'])

    def populate(self, user):
        level_iterators = []
        for user in self.graph.graph.keys():
            level_iterators += self.graph.graph[user]
        for member in level_iterators:
            self.populate_forward(member)
        self.count += 1
        while self.count < self.graph_level:
            self.populate(user)

    def populate_followers(self, user):
        level_iterators = []
        for user in self.graph.graph.keys():
            level_iterators += self.graph.graph[user]
        for member in level_iterators:
            self.populate_forward_followers(member)
        self.count += 1
        while self.count < self.graph_level:
            self.populate_followers(user)

    def do_you_follow(self, user):
        self.graph.graph = {}
        self.populate_forward(self.user)
        print(self.graph.get_graph_dict())
        return self.graph.path_between(self.user, user)

    def do_you_follow_indirectly(self, user):
        self.graph.graph = {}
        self.count = 1
        self.populate_forward(self.user)
        self.populate(self.user)
        self.count = 0
        print(self.graph.get_graph_dict())
        return self.graph.path_between(self.user, user)

    def does_he_she_follow(self, user):
        self.graph.graph = {}
        self.populate_forward_followers(self.user)
        print(self.graph.get_graph_dict())
        return self.graph.path_between(self.user, user)

    def does_he_she_follow_indirectly(self, user):
        self.graph.graph = {}
        self.count = 1
        self.populate_forward_followers(self.user)
        self.populate_followers(self.user)
        self.count = 0
        print(self.graph.get_graph_dict())
        return self.graph.path_between(self.user, user)

    def who_follows_you_back(self):
        who_is_followed_by_followers = []
        self.count = 1
        self.populate_forward(self.user)
        self.populate(self.user)
        self.count = 0
        followed_by_followers = self.graph.graph.values()
        for followers in followed_by_followers:
            for follower in followers:
                who_is_followed_by_followers.append(follower)
        self.graph.graph = {}
        self.populate_forward(self.user)
        who_i_follow = [follower for follower in self.graph.graph[self.user]]
        self.graph.graph = {}
        self.populate_forward_followers(self.user)
        who_follows_me = [follower for follower in self.graph.graph[self.user]]
        co_list = [follower for follower in who_follows_me if follower in who_i_follow or follower in who_is_followed_by_followers]
        return co_list

def main():
    f = Followers('ivelintod', 3)
    '''print(f.do_you_follow('lucifer666'))
    print(f.do_you_follow('VladislavAt'))
    print(f.do_you_follow('vassi95'))
    print(f.do_you_follow_indirectly('vassi95'))
    print(f.do_you_follow_indirectly('VladislavAt'))'''
    #print(f.do_you_follow_indirectly('RadoRado'))
    #print(f.does_he_she_follow('lucifer666'))
    #print(f.does_he_she_follow_indirectly('RadoRado'))
    print(f.who_follows_you_back())
if __name__ == '__main__':
    main()
