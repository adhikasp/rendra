# Kata Baku Checker for PO File

## Usage

```
  python check.py -i [Input File] -t po
```


### Without Symbolic Link
If you don't have a root access, you can use this command:
```
./bakuCheck.py <path-to-file>/<filename>
```


## Improvement Suggestion
- Add other common mistakes to the dictionary list `dict.txt`. See the format below.
- Create more checkers.


## Dictionary List
The default dictionary list file is `dict.txt` placed in the root folder of the script. To change the dictionary list file, simply change the `dictFile` constant in the `bakuCheck.py`. The format of this file follow the format below:
```
<correct word 1>|<wrong word 1>
<correct word 2>|<wrong word 2>
<correct word 3>|<wrong word 3>
<correct word 4>|<wrong word 4>
...
<correct word n>|<wrong word n>
```

Although the program automatically detect duplicate entries and treat it as one, it is indeed not a good thing to keep duplicate entries in the dictionary list file. So, I made a simple script `improveDict.py` to delete duplicate entries (leave one of them). Usage :
```
./improveDict.py <src> <dst>
```
where `src` is the current dictionary list file and `dst` is the "improved" dictionary list file.

P.S : even I don't know why I named it "improve" :D

## License
```
Copyright © 2016 Turfa Auliarachman <turfa_auliarachman@rocketmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.
```
