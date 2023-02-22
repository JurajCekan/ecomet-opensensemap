# ecomet-opensensemap
Demonstration use of the **ecomet i2c** measuring card for **Raspberry Pi** and upload data into opensensemap.org site

## Installation
1. Clone the project

```$ git clone git@github.com:JurajCekan/ecomet-opensensemap.git```

2. Step into ecomet-opensensemap directory

```$ cd ecomet-opensensemap```

3. Create copy of config.py-template and name it config.py

```$ cp config.py-template config.py```

4. Edit values in config.py file

```$ vi config.py```

5. Create python virtual environment

```$ python3 -m venv .venv```

6. Activate python virtual environment

```$ source .venv/bin/activate```

7. Update pip

```$ python3 -m pip install --upgrade pip```

8. Install dependecies from requirements.txt

```$ pip install -r requirements.txt```

## Run
1.  Activate python virtual environment

```$ source .venv/bin/activate```

2. Start program
  * As standard user. ( You can stop program by presing ctrl+C )

```$ python3 ecomet-opensensemap.py```

  * Start program in background

```$ python3 ecomet-opensensemap.py &```
