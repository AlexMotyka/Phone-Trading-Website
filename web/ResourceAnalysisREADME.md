README:
  In order to run resource analysis of the frontend interface through cProfile and Kcachegrind,
  complete the terminal commands listed below:
  
  Install Easy Install and pip:
  
 1) sudo apt-get install python-setuptools python-dev build-essential 
 2) sudo easy_install pip 
 
  Install cProfile with pip:
  
  1) pip install cProfile
  
  Install Valgrind, Kcachegrind, and pyprof2calltree. The latter is needed to run Kcachegrind:
  
  1) sudo apt-get install valgrind
  2) sudo apt-get install kcachegrind
  3) pip install pyprof2calltree
  
  Clone this repo. Run cProfile on web.py from the directory you have cloned this repo.
  In order to organize output based on ncalls, tottime, or cumtime, follow set 2, 3, 
  and 4, respectively:
  
  1) python -m cProfile web.py
  2) python -m cProfile -s numcalls web.py
  3) python -m cProfile -s tottime web.py
  4) python -m cProfile -s cumtime web.py
  
  In order to see a Kcachegrind representation of cProfile analysis, it is necessary to
  output the cProfile results as a binary file by running the following:
  
  1) python -m cProfile -o web.cprof web.py

  To use Kcachegrind, run. A GUI will appear upon running of this command:
  
  1) pyprof2calltree -k -i web.cprof
