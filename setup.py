import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='yahoo_finance',
    version='0.0.1',
    author='Alishan Dhukka',
    author_email='alishandhukka@gmail.com',
    description='Package to scrape stock price history from yahoo finance',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/adhukka477/yahoo_finance',
    project_urls = {
        "Bug Tracker": "https://github.com/adhukka477/yahoo_finance"
    },
    license='MIT',
    packages=['yahoo_finance'],
    install_requires=['pandas', 'datetime', 'bs4'],
)
