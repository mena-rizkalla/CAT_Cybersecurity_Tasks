## Level 0
- ssh bandit0@bandit.labs.overthewire.org -p 2220

## level 1
- ssh bandit1@bandit.labs.overthewire.org -p 2220
- password ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## level 2
-  cat /home/bandit1/-
- password 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## level 3
- cat spaces\ in\ this\ filename
 password MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## level 4
- ls -a
- password 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## level 5
- cat /home/bandit4/inhere/-file07
- password 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

## level 6
- find /home/bandit5/inhere/ -type f -size 1033c | cat
- password HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

## level 7
- find / -type f -user bandit7 -size 33c |less
- cat /var/lib/dpkg/info/bandit7.password
- password morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

## level 8
- less data.txt
- password dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

## level 9
- sort data.txt | uniq -u
- password 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

## level 10
-  strings data.txt | grep '==='
- password FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

## level 11
-  base64 -d data.txt
- password dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
