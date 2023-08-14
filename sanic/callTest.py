class OPPO:
    def __init__(self,name) -> None:
        self.name = name

    def __call__(self,age):
        print(self.name," 本分！！！！ AND Age is： ",age)

oppoer = OPPO("卢俊")

oppoer(22)


print(callable(oppoer))