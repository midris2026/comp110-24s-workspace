"""Dictionary Functions."""

__author__ = "730569217"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values."""
    inverted = {}
    dictionary_list: list[str] = list()
    for key in dictionary:
        if dictionary[key] in dictionary_list:
            raise KeyError("")
        dictionary_list.append(dictionary[key])

    for key in dictionary:
        i = dictionary[key]
        inverted[i] = key
    return inverted        
        

def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color that appears the most."""
    ccounter: dict[str, int] = {}
    clist: list[str] = []

    for names in dictionary:
        color: str = dictionary[names]
        ccounter[color] = 0
        clist.append(color) 

    for colors in clist:
        if colors in ccounter:
            ccounter[colors] += 1

    biggest_num: int = 0
    favorite_color: str = ""
    for key in ccounter:
        if ccounter[key] > biggest_num:
            favorite_color = key
            biggest_num = ccounter[key]
    return favorite_color


def count(list1: list[str]) -> dict[str, int]:
    """How many times a key is in the dictionary."""
    result_dict: dict[str, int] = {}
    for value in list1:
        if value in result_dict:
            result_dict[value] += 1
        else:
            result_dict[value] = 1

    return result_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Alphabetizing the list."""
    result_dict: dict[str, list[str]] = {}
    for word in list1:
        first_letter = word[0].lower()
        if 'a' <= first_letter <= 'z':
            if first_letter in result_dict:
                result_dict[first_letter].append(word)
            else:
                result_dict[first_letter] = [word]

    return result_dict    
    

def update_attendance(dictionary: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance."""
    if day in dictionary and student not in dictionary[day]:
        dictionary[day].append(student)
    else:
        dictionary[day] = [student]