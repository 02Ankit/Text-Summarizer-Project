# create local package setup.py 
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project" #git repo name 
AUTHOR_USER_NAME = "02Ankit" # git hub user name 
SRC_REPO = "textSummarizer" # src/project name 
AUTHOR_EMAIL = "02abhijeetdewangan@gmail.com" # email

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A simple text summarizer NLP Application using Python and NLTK",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir=  {"":"src"},
    packages = setuptools.find_packages(where="src") 
)