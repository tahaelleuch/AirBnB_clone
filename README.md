# AirBnB_clone
Command interpreter to manage the AirBnB objects.
### About this project
The AirBnB_clone is the first step to build our first full web application.
it's a cammand interpreter to manipulate data (input and storing) without an interface or with black interface(like in a shell)
we will focus now on cammand interpreter and file storage

### how it works
*The console:*
 - Displays the prompt (hbnb) and waits for user input.
 - Read the command.
 - lunch the function needed.
 - Print the Error message if the commande is wrong.
 - Quit

### Files repartition
*AirBnB_clone*
 - console.py
 - file.json 
 - tests/ (unittests)
 - models
     -  __ init__.py
     - base_model.py
     - user.py
     - state.py
     - place.py
     - city.py
     - amenity.py
     - review.py
     - engine
         -    __ init__.py
         -  file_storage.py
### Console functions
*AirBnB_clone*
  - do_EOF
  - do_quit
  - do_create 
  - do_update
  - do_all
  - do_show
  - do_destroy
  - emptyline 
  - postloop

### Bugs
No Known Bugs.
### AUTHOR
Mouhamed Charfi : GitHub/medcharfi96
Taha Elleuch : GitHub/tahaelleuch

