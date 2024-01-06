class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# Использование iterators для создания бесконечного цикла
def infinite_loop():
    while True:
        yield 1

iterator = infinite_loop()

for number in iterator:
    print(number)