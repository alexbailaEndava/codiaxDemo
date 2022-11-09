## gpt3Apps
A repository containing tools to play with OpenAI's GPT-3's **Davinci** model. In this repository you will find scripts that perform the following actions:
* Simple & Continuous Inference with GPT-3 (**q&a/**)
* Live Q&A with 2 separate bots, one moody and the other one friendly (**q&a/**)
* Code generation, debugging and explanation (**workWithCode/**)
* Text summarization & lyrics composition (**sumarize&compose/**)
* Marketing slogan generator (**slogan_generator/**)
* Semantic Search (**semantic_search/**)
* Keywords & intent extraction from user e-mails (**keywords_extractor/**)

### Prerequisites
In order to be able to use the functionalities in this repository you need to have 'Python 3.9.0' and the latest 'pip' version installed.
* python 3.9.0 -> https://www.python.org/downloads/release/python-390/
* pip -> https://pip.pypa.io/en/stable/installation/
* For complete tutorial -> https://www.digitalocean.com/community/tutorials/install-python-windows-10

This dependencies should be installed in your Python virtual environment, that is created as such:
```
python -m venv venv
```

After creating the environment, you need to activate it by running the 'activate.bat' script, which is located in the 'venv/Scripts/' folder
```
cd venv/Scripts
activate
cd..
cd..
```

In order to have this scripts working on your computer, you need to have the following dependencies installed in your virtual envrionment.
* openai
* pandas == 1.5.1
* notebook
* termcolor == 2.1.0
* colorama == 0.4.6
* transformers == 4.23.1

After activating your virtual environment, use 'pip' to install them in your virtual environment.
```
pip install -r requirements.txt
```
