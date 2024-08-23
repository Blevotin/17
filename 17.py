def test_function():
    def  inner_function():
        print("Я в области видимости функции test_function")
    a = inner_function()

b = test_function()
g = inner_function()
