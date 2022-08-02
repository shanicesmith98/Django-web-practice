from scripts.base_requests_class import Bucketlist

def test_is_empty_bucketlist():
    test_list = Bucketlist("Fran")
    test_list.add_movie("Carol")
    test_list.remove_movie("Carol")
    assert test_list.get_bucketlist_length() == 0

def test_movie_is_added():
    test_list = Bucketlist("Garnet")
    test_list.add_movie("Jump In")
    assert test_list.get_movie_list() == ["Jump In"]

def test_movie_is_removed():
    test_list = Bucketlist("Garnet")
    test_list.add_movie("Hercules")
    test_list.add_movie("Julia")
    test_list.add_movie("Monster In-Law")
    test_list.remove_movie("Julia")
    assert test_list.get_movie_list() == ["Hercules", "Monster In-Law"]

def test_is_guest_user():
    test_list = Bucketlist()
    assert test_list.get_bucketlist_name() == "Guest"

def test_is_named_user():
    test_list = Bucketlist("Angel")
    assert test_list.get_bucketlist_name() == "Angel"