# Retail Store ETL - Data Engineering

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#prerequisites"> ➤ Prerequisites</a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#dataset"> ➤ Dataset</a></li>
    <li><a href="#roadmap"> ➤ Roadmap</a></li>
    <!--<li><a href="#experiments">Experiments</a></li>-->
    <li><a href="#results-and-discussion"> ➤ Results and Discussion</a></li>
    <li><a href="#contributors"> ➤ Contributors</a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  This project involves creating a data architecture/ data model for a made-up whisky retail shop that will enable the shop managers to make decisions based on their data.
  
  The architecture includes various components that will make the decision-making process for the managers as easy as possible.
</p>

<!-- PREREQUISITES -->
<h2 id="prerequisites"> :fork_and_knife: Prerequisites</h2>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br>
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try) <br>

<!--This project is written in Python programming language. <br>-->
The following open source packages are used in this project:
* Pandas                    
* Numpy                     
* Beautifulsoup4            
* Requests                  

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<h2 id="folder-structure"> :cactus: Folder Structure</h2>

    code
    .
    │
    ├── retail_store
    │   ├── raw_data
    │   │   ├── phone
    │   │   │   ├── 
    │   │   │   └── 
    │   │   ├── watch
    │   │       ├── 
    │   │       └── 
    │   │
    │   ├── transformed_data
    │   │   ├── 
    │   │   │   ├── 
    │   │   │   └── 
    │   │   ├── 
    │   │       ├── 
    │   │       └── 
    │   │
    │   ├── scrape.py
    │   ├── example.py
    │   ├── README.md
    │   │    ├── 
    │   │    ├── 
    
<!-- DATASET -->
<h2 id="dataset"> :floppy_disk: Dataset</h2>
<p> 
  The Whisky dataset was obtained by webscraping from the world’s leading specialist online retailer for fine whiskies and spirits, with three London shops and a raft of award-winning events.

 The Website is publicly available. Please refer to [The Whisky Exchange](https://www.thewhiskyexchange.com/).

  The following table shows the attributes of the data set.
</p>

<p align="center">
  <img src="images/Activity Table.png" alt="Table1: 18 Activities" width="45%" height="45%">
</p>

<p> 
  Other secondary datasets such as employees, customers, payments and countries
  were randomly generated i.e. synthetic

  The following table shows the attributes of the data set.
</p>

<p align="center">
  <img src="images/Activity Table.png" alt="Table1: 18 Activities" width="45%" height="45%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ROADMAP -->
<h2 id="roadmap"> :dart: Roadmap</h2>

<p align="justify"> 
  I have developed a central databse, data warehouse and created various visualizations that will assist in quick decision making, predictions, and overall understanding of the organization’s situation.

  The goals of this project include the following:
<ol>
  <li>
    <p align="justify"> 
      Webscrape product data from the <a href="https://www.thewhiskyexchange.com/">The Whisky Exchange</a> website.
    </p>
  </li>
  <li>
    <p align="justify"> 
      Generate random data for product id, employees, payments and countries.
    </p>
  </li>
  <li>
    <p align="justify"> 
      Design a Central RDBMS and apply normalization.
    </p>
  </li>
  <li>
    <p align="justify"> 
      Load the data into the central RDBMS.
    </p>
  </li>
  <li>
    <p align="justify"> 
      Get into the shoes of the analyst - come up with visualizations that  could be used for decision making in the organization.
    </p>
  </li>
</ol>
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- RESULTS AND DISCUSSION -->
<h2 id="results-and-discussion"> :mag: Results and Discussion</h2>

<p align="justify">
  The overall accuracy score of personal and impersonal models are shown in the following tables. Some of the results we observed are similar to the results obtained by Weiss et.al and they are discussed below: <br>
</p>
<p align="justify">
<ul>
  <li>
    Are we growing as a company in terms of profits or not?. <br>
  </li>
  <li>
    From which counties do most of the customers come from?
  </li>
  <li>
    From which counties do most of the customers come from?
  </li>
  <li>
    Are there any interesting patterns as to when customers like to buy whiskey? If so what are they?
  </li>
  <li>
    Which products do people usually buy?
  </li>
  <li>
    Which products produce the most profit?
  </li>
  <li>
     Some key take-aways based on my results are listed below:
  </li>
  <li>

  </li>
</ul>
</p>

<p align="center">
  <img src="images/Personal and Impersonal Table.png" alt="Table 3 and 4" width="75%" height="75%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CONTRIBUTORS -->
<h2 id="contributors"> :scroll: Contributors</h2>

<p>
  :mortar_board: <i>The following are the participants in this project </i> <br> <br>
  
  :boy: <b>Grivine Ochieng Otieno</b> <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/grivine/">Grivine Ochieng</a> <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Twitter: <a href="https://twitter.com/Grivine_O">@Grivine_O</a> <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: <a href="https://github.com/Grivine-19">Grivine-19</a> <br>
</p>
<br>
✤ <i>This is a project concept borrowed from <a href="https://www.linkedin.com/in/bar-dadon/">Bar Dadon</a> from his project series on Medium <a href="https://medium.com/towardsdev/data-engineering-project-retail-store-part-1-web-scraping-a99ac5d6d44c">Data Engineering Project — Retail Store Part 1 — Web Scraping</a><i>