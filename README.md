## Requirements
1. Download Git bash
https://git-scm.com/downloads

2. Get Python3
https://www.python.org/downloads/
- Add python to PATH  (windows)
- get Pip
- download this file and run it using python
https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py


## Installation
1. ```git clone https://github.com/EmanAbbas/tamkeentraining.git```
2. ```cd .. ```
### Linux ,Mac:
- ```virtualenv  env```
- ```source env/bin/activate```
### Windows:
```virtualenv  env```
```source env/Scripts/activate```

3. ```cd [project_folder]```

4. ```sudo pip install -r requirements.txt```
5. ```python manage.py migrate```
6. ```python manage.py runserver ```

Ctrl+C to exit environment

###  Heroku app link
'tamkeen4st.herokuapp.com'


## To view admin site 

```python manage.py createsuperuser```