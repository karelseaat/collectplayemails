
# 1 Collectplayemails

This project collects the emails of developers on the google playstore. (this was befor google chnaged the structure of the playstore website)
There are also scripts that will filter out developers that are most likly to engage on the tradearate platform that is also avalable as one of my repos.
After that you have a nice list of emails of people that might wanna use the tradearate platform.

# 2 Structure
nothing of structure here just a few scripts that get all of this done.


# 3.5 Things used
Nothing special but the packages.
Perhaps sqlite, sqlalchemy, python duh and selenium

# 3 How to run it
This software depends on `pipenv` how one does `pipenv` one can find here: [pipenv](https://docs.python-guide.org/dev/virtualenvs/)
Get the selenium webdriver like geckodriver for firefox and put this in the root dir
Run getkeywordsearch.py to fill the database
and run getgoodemails to get the good emails.
update appdata is also doing something but i dont know anymore. (perhaps run it after getkeywordsearch)


# 4 Class diagram

No real classes, no class diagram.

# 5 Packages used:

`selenium`
`sqlalchemy`
`sqlalchemy-utils`
`pylint`
