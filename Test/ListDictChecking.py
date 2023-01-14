class Notebook(object):
    def __init__(self, iteminstance):
        self.lista = [iteminstance]

    def show(self):
        print('Container1 list:')
        for item in self.lista:
            print(item.content)


class Binder(object):
    def __init__(self, iteminstance):
        self.lista = [iteminstance]

    def show(self):
        print('Container2 list:')
        for item in self.lista:
            print(item.content)


class Note(object):
    def __init__(self, txt):
        self.content = txt

    # create Notebook instance and store Note instance in 'lista' list argument


a = Notebook(Note(5))
a.show()

# assign the same Note instance to different container, Binder instance
b = Binder(a.lista[0])
b.show()

# check if both containers include the same object
print(a.lista == b.lista)


# change content of the Note instance via Notebook instance
a.lista[0].content = 10

# check if content has changed in both Notebook and Binder instances
a.show