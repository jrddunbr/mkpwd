# mkpwd Introduction

The mkpwd utility is intended to be useful for creating basic random passwords,
intended for temporary use and one-time keys.

While not necessarily something that is useful for long-term passwords,
it is certainly better than many passwords I have seen over the years.

Recommended usage is for locations where passwords are non-critical and where a
password that would initially be considered would be much worse.

I tend to personally use it for throwaway accounts and for one-time passwords,
or when someone has a difficult time coming up with a password that is
sensible in a security sense. This does not act as a stand-in for a good
password at shorter lengths - if you intend to use this as a regular password, I
would suggest changing some characters to lowercase, adding symbols, or
other techniques to increase the limited entropy of this program.

In general, mkpwd passwords shorter than 16 characters are insufficient.

If you did want to use this as a stand-in for a better password, and you have no
other options, I would say 32-64 for the mkpwd utility, and over 256-512 for the
mknum utility.

# Usage

The ```mkpwd``` and ```mknum``` utilities behave exactly the same, except that
one returns a set of digits and uppercase characters of a specified size, and
the other returns a set of only digits of a specified size. ```mkpwd2``` adds
special characters to ```mkpwd```.

## User Interface Mode

```bash
./mkpwd.py
./mkpwd2.py
./mknum.py
```

After you run this command, it will prompt you for a size. If the size is
negative, it will warn you and quit without doing anything. Otherwise, it will
print a string to stdout and exit.

### Shell Mode

```bash
./mkpwd.py $SIZE
./mkpwd2.py $SIZE
./mknum.py $SIZE
```

When you specify a size argument (in this case, the variable SIZE), it prints a
string to stdout. If the size is less than 1, it just prints the error to stderr
instead of stdout so that scripts can ignore the error and continue. If there is
an error, it also returns 1.
