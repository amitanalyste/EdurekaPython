class TestClass:
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("destructor")


if __name__ == "__main__":
    obj = TestClass()
    del obj