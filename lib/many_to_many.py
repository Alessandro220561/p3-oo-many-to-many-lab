class Author:

    all = []

    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        contracts = self.contracts()
        total_royalties = 0

        for contract in contracts:
            total_royalties += contract.royalties

        return total_royalties


class Book:

    all = []

    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise Exception
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
