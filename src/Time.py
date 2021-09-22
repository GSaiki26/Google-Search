## Libs
from time import strftime, localtime

## Methods
## Method to get the localtime.
def GetTime() -> str:
    t = localtime() ## Get the time tuple.
    return strftime('%H:%M:%S', t) ## Return the current time.