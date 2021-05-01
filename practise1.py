class Creation:
    def __init__(self, title, owners=None):
        self.title = title
        self.owners = owners.copy()

    def __is_valid(self, owners):
        pass


class Asset(Creation):
    def __init__(self, title, owners=None, name=None, released_date=None):
        self.name = name
        self.released_date = released_date
        if not self.__is_valid(owners):
            return f"Invalid owner class"
        super(title, owners)

    def get_owners_count(self):
        pass

    def __is_valid(self, owners):
        if isinstance(owners, list):
            for ob in owners:
                if not isinstance(ob, Researcher):
                    return False
            return True
        else:
            if isinstance(owners, Researcher):
                return True
        return False


class Poem(Creation):
    def __init__(self, title, owners=None, template=None):
        self.template = template
        if not self.__is_valid(owners):
            return f"Invalid owner class"
        super(title, owners)

    def __is_valid(self, owners):
        if isinstance(owners, list):
            for ob in owners:
                if not isinstance(ob, Singer):
                    return False
            return True
        else:
            if isinstance(owners, Singer):
                return True
        return False


class Book(Creation):
    def __init__(self, title, ISBN, owners=None, publishers=None):
        self.ISBN = ISBN
        self.publishers = publishers
        if not self.__is_valid(owners):
            return f"Invalid owner class"
        super(title, owners)

    def __is_valid(self, owners):
        if isinstance(owners, list):
            for ob in owners:
                if not isinstance(ob, Writer):
                    return False
            return True
        else:
            if isinstance(owners, Writer):
                return True
        return False

    def get_owners_count(self):
        pass


class Person:
    def __init__(self, name, email=None, gender=None):
        self.name = name
        self.email = email
        self.gender = gender


class Researcher(Person):
    def __init__(self, name, field, email=None, gender=None, college=None):
        self.field = field
        self.collage = college
        super(name, email, gender)


class Singer(Person):
    def __init__(self, name, email=None, gender=None, template=None):
        self.template = template
        super(name, email, gender)


class Writer(Person):
    def __init__(self, name, writer_code, genres=None, email=None, gender=None):
        self.writer_code = writer_code
        self.genres = genres
        super(name, email, gender)
