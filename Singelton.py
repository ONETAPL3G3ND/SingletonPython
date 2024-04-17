def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Logger:
    def __init__(self):
        self.var = None

    def SetVar(self, var):
        self.var = var

    def GetVar(self):
        return self.var



if __name__ == "__main__":
    a = Logger()
    b = Logger()
    f = Logger()
    b.SetVar(3)
    print(a.GetVar()) #3
    f.SetVar("test")
    print(b.GetVar()) #test