my_dict = {}
my_list = []
#my_dict["model"]
print("before try block")

# gracefully handling exception
#try:
#    print("statement before")
#    my_dict["model"]
#    print("statement after")
#except KeyError:
#    print("Caught Exception")

#print("after try block")

# caught exception and re-arise

#try:
#    my_dict['model']
#except KeyError:
#    print("Caught Exception,re-arise")
#    raise

# caught exception and retrieve information about it

#try:
#    my_dict['model']
#except KeyError as e:
#        print(e.__class__)
#        print(str(e))
#        print("Caught exception,printed info")

# catch multiple exceptions    

#try:
#    my_dict['model']
#    my_list[0]
#except (KeyError,IndexError):
#    print("handled multiple exceptions")


#try:
#    my_dict['model']
#    my_list[0]
#except KeyError:
#    print("handled Keyerror exceptions")
#except IndexError:
#    print("Handled Index error exception")

# catch exception and finally section always executed

#try:
#    my_dict['model']
#except KeyError:
#    print("handled Keyerror exceptions")
#finally:
#    print("This is always executed")    

# except exception

try:
    my_dict['model']
    print("a different statement")
except Exception:
    print("handled Keyerror exceptions")


