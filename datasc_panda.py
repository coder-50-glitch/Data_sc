import pandas

mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

import pandas as pd

mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
