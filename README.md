
# Scrapper Challenge
This project is an application challenge, which consists in web scrapping and retrieving data.

The project is completly build in python, with [scrapy](https://scrapy.org) and sqlite database.


## Dependencies 📦

This project uses [poetry](https://python-poetry.org/docs/) to manage all dependencies. Before starting you will need to install
python 3.11 and poetry.


## Setup Your Project 💻

First, clone the project

~~~bash  
  git clone https://github.com/ToledoVitor/scrapper-challenge.git
~~~

Go to the project directory  

~~~bash  
  cd scrapper-challenge
~~~

Set poetry version  

~~~bash  
poetry env use 3.11
~~~

Install dependencies

~~~bash  
poetry install
~~~

Activate your virtual enviroment

~~~bash
poetry shell
~~~


## Run The Spiders 🕷️

As mentioned before, we use scrapy to crawl through pages. To run the spider through command line:

~~~bash
scrapy runspider src/spiders/istock.py
~~~

This will pretty much do all the job. It will start crawling, fetching images, and saving on the database. 

### Optional: Running through Vscode

If you are just like me, and like to run your projects in the vscode debbuger section, you can use this configuration in your launch.json

```json
{
    "version": "0.1.0",
    "configurations": [
        {
            "name": "Python: Launch Scrapy Spider",
            "type": "debugpy",
            "request": "launch",
            "module": "scrapy",
            "args": [
                "runspider",
                "src/spiders/istock.py"
            ],
            "console": "integratedTerminal"
        }
    ]
}
```


## Run The Tests 👾

All the tests are in the tests/ folder. To run the tests through command line:

~~~bash
python -m unittest
~~~


## Considerations 📝

I always like to make some considerations about the choices, libraries, structure and everything that made we get to the final version.

So, here are some topics that I think is worth of talking about:

### About The Spider

This project it`s a very simple solution about a web crawler. This is due to your porpuse of being an application test.

There`s only one spider, name istock.py, which goes through [FreeImages Website](https://www.freeimages.com),
searches for dogs pictures, and saves the 1000 first images URLs in a sqlite database.

The spider don't handle login, since there's no need because off the open search bar.

### About The Tests

Testing spiders are always a good discussion.

The Scrapy library kinda have your own solution about [Spider Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html). It's worth taking a look.

Since the challenge requirements tells to use unittest, I made my own kinda of solution.
There are some real responses saved as samples in the `tests/responses/samples` folder, which obviouslly will not have all pages responses.

In all the tests we created fake responses, using the real samples, and call the spider using that response.
The assertions are made based on the number of images expected to be retrieved.

Remember that the local HTML file may not reflect the latest state online.

### About The Database

Just like the tests, the used database was part of the challenge requirements.
The use of sqlite database can be due to the facility and simplicity of the database management.

When talking about bigger applications, maybe that's not a good choice.
If we are willing to use some sql solution, it's to consider something like [PostgreSQL](http://www.postgresql.org).


## License  

[MIT](https://choosealicense.com/licenses/mit/)
