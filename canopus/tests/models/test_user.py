class TestUser(object):
    def test_fullname(self, user):
        assert user.fullname() == "{0} {1}".format(user.first_name, user.last_name)

        # Strips first and last name
        user.first_name = "John "
        user.last_name = " Smith "
        assert user.fullname() == "John Smith"

    def test_fullname_last_name_first(self, user):
        fullname = user.fullname(last_name_first=True)
        assert fullname == "{1}, {0}".format(user.first_name, user.last_name)
