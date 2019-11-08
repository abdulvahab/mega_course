def some_function(farg, *args):
    print("This is normal arg", farg)
    for arg in args:
        print("This is a argument from *args", arg)
argv = ["hello", "world"]
some_function('Say',*argv)

def another_function(farg, **kwargs):
    print("This is normal arg", farg)
    for key, value in kwargs.items():
        print(key, "=", value)
names = {'AK':'Abdulvahab', 'ARK':'Abdulrehman', 'MK':'Musu', 'FK':'Fatema'}
another_function('Say',**names)
