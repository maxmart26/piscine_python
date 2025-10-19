def NULL_not_found(object: any) -> int:
    # Cas : None
    if type(object) is type(None):
        print("Nothing: None <class 'NoneType'>")
        return 0
    if type(object) is float and object != object:
        print("Cheese: nan <class 'float'>")
        return 0
    if type(object) is bool and object is False:
        print("Fake: False <class 'bool'>")
        return 0
    if type(object) is int and object == 0:
        print("Zero: 0 <class 'int'>")
        return 0
    if type(object) is str and object == "":
        print("Empty: <class 'str'>")
        return 0
    print("Type not Found")
    return 1


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
