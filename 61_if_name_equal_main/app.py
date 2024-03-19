# if a module is run as a standalone program, python gives it a name = __main__

if __name__ == "__main__": 
    print("running this module directly")
else:
    print("running this module indirectly")

