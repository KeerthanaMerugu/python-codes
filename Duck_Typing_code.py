class PyCharm:
    def execute(self):
        print("compiling")
        print("running")
class MyEditor:
    def execute(self):
        print("spell check")
        print("compiling")
        print("running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide1=PyCharm()
ide2=MyEditor()
l1=Laptop()
l2=Laptop()
l1.code(ide1)
l2.code(ide2)