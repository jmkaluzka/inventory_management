# Installation 

`pip install virtualenvwrapper` to install the virtualenvwrapper if not installed yet
`which virtualenvwrapper.sh` to locate the virtualenvwrapper.sh
`source` + result of previous command - to add the command to the shell startup file
`mkvirtualenv inv -r requirements.txt --python=/usr/bin/python3` to create new virtualenvwrapper (will be atomatically activated - normally `workon inv`) with all requirements -change `/usr/bin/python3` to your python path 

`make install` to migrate database models and create superuser

# Apply changes in models
`make migrate`

# Playing with database
`make orm`

# Starting project
`make run` to run the project