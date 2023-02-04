class Notebook(object):
    def __init__(self, iteminstance):
        self.lista = [iteminstance]

    def show(self):
        print('Container1 list:')
        # Adding code to list each element


class Binder(object):
    def __init__(self, iteminstance):
        self.lista = [iteminstance]

    def show(self):
        print('Container2 list:')
        # Adding code to list each element


class Note(object):
    def __init__(self, txt):
        pass
    # Adding code

    # create Notebook instance and store Note instance in 'lista' list argument


common_element = Note(5)

a = Notebook(Note(5))
a.show()

# assign the same Note instance to different container, Binder instance
b = Binder(a.lista[0])
b.show()

c = Binder(common_element)

# check if both containers include the same object
print(a.lista == b.lista)

# change content of the Note instance via Notebook instance
a.lista[0].content = 10

# check if content has changed in both Notebook and Binder instances
a.show
