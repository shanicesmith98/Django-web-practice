class Bucketlist:
    def __init__(self, name="Guest"):
        self.__name = name
        self.__movie_list = []

    def add_movie(self, title):
        return self.__movie_list.append(title)

    def remove_movie(self, title):
        return self.__movie_list.remove(title)

    def get_movie_list(self):
        return self.__movie_list

    def get_bucketlist_name(self):
        return self.__name

    def get_bucketlist_length(self):
        return len(self.__movie_list)