# Description

It's a (muddle) double fork of
<https://github.com/turfaa/IndonesianKataBakuChecker> and
<https://github.com/berviantoleo/Kata-Baku-Checker-for-PO-File>

The main difference is addition of "padanan kata" or term word checker.
There are many IT related word that left untranslated because the equivalent
word in Indonesian is confusing or not many people familiar with it.
Some effort by government is trying to standardize this IT term by publishing
list of translated IT term in English. Thus, this "padanan kata" checker is
trying to popularizing the usage of said translated IT term.

Reference
- [An article about translating foreign term](http://www.master.web.id/mwmag/issue/01/content/bdt-istilah_asing/bdt-istilah_asing.html)
- [Published IT term by government, as per Instruksi Presiden no 2 th 2001](https://web.archive.org/web/20050112100450/http://vlsm.org/baku-0.txt)

# Usage

```
  python rendra.py -i [Input File] -t po
```

# Improvement Suggestion
- Expand dictionary.
- Create more checkers.
- Improve this readme.


# License

MIT
