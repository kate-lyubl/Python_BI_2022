# Python_BI_2022

In this work, programs were implemented that simulate the UNIX utilities. 

1. __wc__: reads either standard input or a list of computer files and generates one or more of the following statistics: newline count (`-l`), word count (`-w`), and byte count (`-c`).
2. __ls__: lists computer files and directories. With `-a` hidden files are shown
3. __sort__: prints the lines of its input in sorted order
4. __rm__: removes objects such as computer files or directories (with `-r`)
5. __cat__: reads file, writing it to standard output

# Download programs
`$ git clone https://github.com/kate-lyubl/Python_BI_2022.git --branch homework_8`

# How to use programs
Before using programs you have to run `$ chmod +x *.py` command.
1. `./wc.py [-l] [-c] [-w] <filename>`
2. `./ls [-a] <path>`
3. `./sort <filename>`
4. `./rm [-r] <path>`
5. `./cat <filename>`

# Examples
`$ ./wc.py example.txt`
\
2 7 38


`$ ./wc.py example.txt -l`
\
4


`$ ./wc.py example.txt -w`
\
7


`$ ./wc.py example.txt -c`
\
39


`$ ./ls`
\
ls.py
\
README.md
\
wc.py
\
example.txt
\
sort.py
\
cat.py
\
rm.py


`$ ./sort.py example.txt`
\
Hello, World!
\
This 
\
an example file
\
is


`$ ./cat.py example.txt`
\
Hello, World!
\
This 
\
is
\
an example file


`$ ./rm.py example.txt`
`$ ./ls.py`
\
ls.py
\
README.md
\
wc.py
\
sort.py
\
cat.py
\
rm.py

