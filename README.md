<br/>
<p align="center">
  <a href="https://github.com/FlynV/vlr-map-veto-scraper">
    <img src="images/logo.png" alt="Logo" width="250" height="250">
  </a>

  <h3 align="center">VLR Map Veto Scraper</h3>

  <p align="center">
    Tired of going through VLR matches to find out what's a team weak map? Or their strong map? This tool does it AUTOMATICALLY.
    <br/>
    <br/>
    <br/>
    <br/>
    <a href="https://github.com/FlynV/vlr-map-veto-scraper/releases">Download Executable</a>
    .
    <a href="https://github.com/FlynV/vlr-map-veto-scraper/issues">Report Bug</a>
    .
    <a href="https://github.com/FlynV/vlr-map-veto-scraper/issues">Request Feature</a>
  </p>
</p>

![License](https://img.shields.io/github/license/FlynV/vlr-map-veto-scraper) 

## About

As an assistant coach, I found it tedious to go through an opponent team's matches to find their weak map and their strong map. So I created this tool that scrapes recent (25 to 50) games veto from VLR.GG.
The tool gets first map bans and first map picks, and it is open source, so feel free to expand it.  

Head to Releases Tab to download an excutable, or proceed below.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Demo 

<img src="images/demo.svg" alt="Logo" width="1200" height="800">


### Requirements

To get started with the code on this repo, you need to either clone or download this repo into your machine as shown below;

```sh
git clone https://github.com/FlynV/vlr-map-veto-scraper
```

Before you begin playing with the source code, you might need to install dependencies, just as shown below;

```sh
pip3 install -r requirements.txt
```


## Usage

1. Run the script. (following instructions below or just running the executable from Releases Tab.)

```sh
py map.py
```

2.  A prompt will appear asking for a TEAM ID from VLR.GG

```sh
https://www.vlr.gg/team/2593/fnatic
```
In the example above, FNATIC's team ID is 2593.


3. Press enter and give it a bit to generate a CSV file.

4. Please let the script finish so it closes the selenium driver itself, if not finished or closed aburptly: make sure to close all Mozilla tasks through task manager. 


## Contributing



### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/FlynV/vlr-map-veto-scraper/blob/main/LICENSE.md) for more information.

## Follow Me

```sh
https://twitter.com/FlynVAL
```
