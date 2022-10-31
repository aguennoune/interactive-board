# Markdown Files

Whether you write your book's content in Jupyter Notebooks (`.ipynb`) or
in regular markdown files (`.md`), you'll write in the same flavor of markdown
called **MyST Markdown**.
This is a simple file to help you get started and show off some syntax.

## What is MyST?

MyST stands for "Markedly Structured Text". It
is a slight variation on a flavor of markdown called "CommonMark" markdown,
with small syntax extensions to allow you to write **roles** and **directives**
in the Sphinx ecosystem.

For more about MyST, see [the MyST Markdown Overview](https://jupyterbook.org/content/myst.html).

## Sample Roles and Directives

Roles and directives are two of the most powerful tools in Jupyter Book. They
are kind of like functions, but written in a markup language. They both
serve a similar purpose, but **roles are written in one line**, whereas
**directives span many lines**. They both accept different kinds of inputs,
and what they do with those inputs depends on the specific role or directive
that is being called.

Here is a "note" directive:

```{note} 
The only good advice..**Perfect the Visuals**
```

It will be rendered in a special box when you build your book.

Here is an inline directive to refer to a document: {doc}`markdown-notebooks`.


## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

```{bibliography}
```

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).

## About This Role

```{admonition} About This Role
This role will give you the opportunity to deliver high added value data
& analytics projects and build high quality an innovative solutions for our
clients within a growing service company.
```

## What you will do?
* Analyze complex client's request with full autonomy
* Assist businesses in the decision-making process for Data Driven projects
* Optimize data exploration using Machine Learning techniques
* Clean and prepare the data with the Data Scientists
* Analyze and interpret data to extract complex relationships and trends
* Adapt and integrate analytics models into the client's IS environment
* Assist the IT teams in all phases of the production, maintenance and update of the models developed
* Contribute to the design of the technical solution chosen to collect, analyze data, and display the results obtained
* Offer innovative solutions in the Big Data field
* Provide internal trainings to new joiners when needed
* Manage a project from A to Z
* Support to the Team Lead/Manager regarding client relationship, business development and internal projects

## DATA PROJECTS
* Data: Web scraping/ API/ own data
1. EDA/data analysis
2. Data visualization
3. Collaboration data project
4. Explainer blogs/articles

## PROJECTS WHAT'S INCLUDED

```{tableofcontents}
**PROJECT 1**
* EDA ON GROCERIES DATA

1. Objectives:
- Pattern findings in food consumption
- Seasonality in a year
- Before vs. after COVID
- Men vs. women
- What people usually buy together (basket analysis)
- Customer segmentation

2. Dataset:
Example: Kaggle Groceries dataset
(Or your own groceries bills :p)

3. Tools: R/Python, arules package

**PROJECT 2**
* WEB SCRAPING FINANCIAL NEWS - STOCK MARKET SENTIMENT

1. Objectives:
- Obtain financial news as text
- Visualize sentiment scores of your favourite companies

2. Dataset:
Example: Kaggle Groceries dataset
(Or your own groceries bills :p)

3. Tools: Python, beautifulsoup & NLTK package [Example](https://nickmccullum.com/stock-market-sentiment-analysis-python)

**PROJECT 3**
* DATA VIZ - CO2/GREENHOUSE GAS EMISSION

1. Objectives:
- Visualize greenhouse gas emission trends over time & cross countries

2. Dataset:
[Our World in Data](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions)

3. Tools: Tableau/PowerBI

**PROJECT 4**
* TEAM PROJECT - COLLABORATE WITH LOCAL AGENCIES/FRIENDS

1. Objectives:
- Analyse survey data about your interest topic
- Or contact and request data from a local organisation
```

```{note}
DON'T FORGET to write a blog post about it!
```

```{tip} Using Web scraping
**AutoScraper**: A Smart, Automatic, Fast and Lightweight Web Scraper for Python - Check the link here [AutoScraper](https://github.com/alirezamika/autoscraper)
```

## Alternativelly, you can use

```{tip} Using Diffbot
**Diffbot**: Check the link here [Diffbot](https://www.diffbot.com/)
```

## The use of the API

```{tip} Using API such as
**Mixed Analytics**: API Connector for Google Sheets - Check the link here [Mixed Analytics](https://mixedanalytics.com/api-connector/)
```

## Other data resources

```{tip} Using awesome-public-datasets
**Lists of all of great resources including all kinds of data**: Check the link here [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)
```

```{note} 
Lets say it again..**Visuals Matter A lot**
```

