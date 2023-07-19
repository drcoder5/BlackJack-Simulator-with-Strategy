'''
Dictionaries containing the strategy behind actions.
'''

strategy = {

    "2": {"17": "Stand", "16": "Stand", "15": "Stand", "14": "Stand", "13": "Stand", "12": "Hit", "11": "Double Down", "10": "Double Down", "9": "Hit", "8": "Hit"},
    "3": {"17": "Stand", "16": "Stand", "15": "Stand", "14": "Stand", "13": "Stand", "12": "Hit", "11": "Double Down", "10": "Double Down", "9": "Double Down", "8": "Hit"},
    "4": {"17": "Stand", "16": "Stand", "15": "Stand", "14": "Stand", "13": "Stand", "12": "Stand", "11": "Double Down", "10": "Double Down", "9": "Double Down", "8": "Hit"},
    "5": {"17": "Stand", "16": "Stand", "15": "Stand", "14": "Stand", "13": "Stand", "12": "Stand", "11": "Double Down", "10": "Double Down", "9": "Double Down", "8": "Hit"},
    "6": {"17": "Stand", "16": "Stand", "15": "Stand", "14": "Stand", "13": "Stand", "12": "Stand", "11": "Double Down", "10": "Double Down", "9": "Double Down", "8": "Hit"},
    "7": {"17": "Stand", "16": "Hit", "15": "Hit", "14": "Hit", "13": "Hit", "12": "Hit", "11": "Double Down", "10": "Double Down", "9": "Hit", "8": "Hit"},
    "8": {"17": "Stand", "16": "Hit", "15": "Hit", "14": "Hit", "13": "Hit", "12": "Hit", "11": "Double Down", "10": "Double Down", "9": "Hit", "8": "Hit"},
    "9": {"17": "Stand", "16": "Hit", "15": "Hit", "14": "Hit", "13": "Hit", "12": "Hit", "11": "Double Down", "10": "Double Down", "9": "Hit", "8": "Hit"},
    "10": {"17": "Stand", "16": "Hit", "15": "Hit", "14": "Hit", "13": "Hit", "12": "Hit", "11": "Double Down", "10": "Hit", "9": "Hit", "8": "Hit"},
    "A": {"17": "Stand", "16": "Hit", "15": "Hit", "14": "Hit", "13": "Hit", "12": "Hit", "11": "Double Down", "10": "Hit", "9": "Hit", "8": "Hit"},

}

strategy2 = {

    "2": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Double or Stand", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "3": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Double or Stand", ("A",6): "Double Down", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "4": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Double or Stand", ("A",6): "Double Down", ("A",5): "Double Down", ("A",4): "Double Down", ("A",3): "Hit", ("A",2): "Hit"},
    "5": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Double or Stand", ("A",6): "Double Down", ("A",5): "Double Down", ("A",4): "Double Down", ("A",3): "Double Down", ("A",2): "Double Down"},
    "6": {("A",9): "Stand", ("A",8): "Double or Stand", ("A",7): "Double or Stand", ("A",6): "Double Down", ("A",5): "Double Down", ("A",4): "Double Down", ("A",3): "Double Down", ("A",2): "Double Down"},
    "7": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Stand", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "8": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Stand", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "9": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Hit", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "10":{("A",9): "Stand", ("A",8): "Stand", ("A",7): "Hit", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},
    "A": {("A",9): "Stand", ("A",8): "Stand", ("A",7): "Hit", ("A",6): "Hit", ("A",5): "Hit", ("A",4): "Hit", ("A",3): "Hit", ("A",2): "Hit"},

}
