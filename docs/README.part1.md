# SI 100B Project: Who is Flying over? - Week 1

In this week, we are finishing the very first yet important task in this project - get reliable data source of the flight nearby. There are multiple approaches to solve the problem including set up your own radio reciever to pick up the ADB-S signals which the air traffic controllers used to track the location of the airplanes they are in charge of.

However, setting up radio reciever is beyond the scope of this course. In this project, an alternative way is used. We are getting the data from websites that provide real-time flight data feed. What those websites do is distributing the radio recievers all cross the world in a crowdsourcing way to pick up the ADB-S signal and distribute the data via the internet. The most widely used two of its kind are FlightRadar24 (https://www.flightradar24.com/) and FlightWare (https://flightaware.com/live/ ). Those two website provides almost identical coverage in the vancity of Shanghai.

## The Data Source

The first thing to do for writing a web crawler is to determine what requests you want to send and how you will parse the response from the server. Generally, each website will have a slightly different schema of request and response. It is the job of the authors of the crawler to explore the patterns in request and response. However, since almost all those request and response are using the same protocol, HTTP, the underlying principle is the same.

In this section, you are going to explore the schema of request and response of **any one** of FlightRadar24 or FlightWare. The techniques required to crawl the two websites are almost the same, and the difficulty is similar. You can choose any one of them to get start with. Some people may encounter some connectivity issue with one of those two website, in this case, just switch to another.

Many well-written high-level packages are there for you to send request to a HTTP server and get response from it (called HTTP client library formally) in Python. The `requests`, which could be installed with PyPI, is the most commonly used and is recommended for this project. Some other packages, like `urllib3`, provide the same functionality but is more complicated to use. If you are a real power user, you can even set up a raw TCP connection to the server with the `socket` package and generate/parse HTTP request/response yourself. Before you start, you are to understand how to use your tools. Read the documentation of [`requests`](https://requests.readthedocs.io/en/master/) or another other HTTP client libray you choose to use, answer the following questions:

*  How to send a HTTP `GET` request to a URL, for example, the home page of ShanghaiTech?
* What format of URL does the package accept? Is `https://www.shanghaitech.edu.cn/` a legal URL? How about `sist.shanghaitech.edu.cn`?
* How to determine if the request is successful?
* How to get the response body for a request?

Prepare to explain your answers to those questions to a TA.

### FlightRadar24

Follow this section is you choose to crawl FlightRadar24 for your data. Jump to next section if you are using Flighware.

Now, open FlightRadar24 (linked above) in your browser (a modern version of Chrome, Firefox, Safari and Edges is highly recommended) and open the developer tool of your browser. Wait until the site is fully loaded and starts to display the location of airplanes, go to the `network` tab of your developer tools. Explore the requests your browser sent out and response from the server. Determine which part of the requests is related to the dynamic updating the the page to show the up-to-date list of airplanes in a certain area. Then do the following things:

- Write down the URL of the requests and take a guess of what each part of the parameters means;
- Determine the format of the response and find a way to parse it to a structured one that Python could understand;
- Determine the meaning of each field of the response. You can do this by compare the response with the displayed values on the web page.

Write a simple program to verify the your guess in this section and prepare to explain your answers and program to a TA.

**Hint**: you are requesting https://data-live.flightradar24.com/zones/fcgi/feed.js for the flight data. One example request is to https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=31.53,30.90,120.91,122.17&faa=1&satellite=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1. Explore what does each parameter means so that you can gain some clue about how to generate your own request in next section.

### Flightware

Follow this section is you choose to crawl Flightware for your data.

Now, open Flightware (linked above) in your browser (a modern version of Chrome, Firefox, Safari and Edges is highly recommended) and open the developer tool of your browser. Wait until the site is fully loaded and starts to display the location of airplanes, go to the `network` tab of your developer tools. Explore the requests your browser sent out and response from the server. Determine which part of the requests is related to the dynamic updating the the page to show the up-to-date list of airplanes in a certain area. Then do the following things:

- Write down the URL of the requests and take a guess of what each part of the parameters means;
- Determine what method is used for each requests;
- Determine the format of the response and find a way to parse it to a structured one that Python could understand;
- Determine the meaning of each field of the response. You can do this by compare the response with the displayed values on the web page or take a guess of the meaning of the tags in the response from the server.

Write a simple program to verify the your guess in this section and prepare to explain your answers and program to a TA.

**Hint**: You are requesting https://flightaware.com/ajax/vicinity_aircraft.rvt for the flight data. A possible request is to https://flightaware.com/ajax/vicinity_aircraft.rvt?&minLon=109.0283203125&minLat=-8.59954833984375&maxLon=180&maxLat=27.0703125&token=e70b744ef39ffcbc8e52cb8caa9619e55ced9bb1. Explore what does each parameter means so that you can gain some clue about how to generate your own request in next section. If your program simply request this URL, you will sometimes get no data and a HTTP 400 or 500 status code indicating an error. This probably means your token (i.e., the `token` parameter in the request. In the example above, it is `e70b744ef39ffcbc8e52cb8caa9619e55ced9bb1`) has expired and needs you to update it.

There are two ways to update the token. The first one is the easiest. You open a new browser tab and load the Flightware website. Then you can copy down the newly generated token from the dev tool and paste it to your script. The down side of the method is that you need to do it for every few hours before your token expired. Another method is to find the request where the token is responsed from the server and request the URL periodically to update it. This method requires some advanced understanding of web devlopment.

## Implement your Cralwer

Now you have some idea of what requests you need to send to get the list of airplanes in a certain area and the next step is to implement the crawler in this project. Now implement the crawler in the `Fr24Crawler` class in `data_source/fr24_crawler.py`. Your implementation should follow the following specifications:

- `__init__(self, loc, rng)`: `loc` is a tuple of two `float`-typed numbers indicating the coordinate where the user is at. The first item in `loc` (i.e., `loc[0]`) is the latitude of the user and the second item is the longitude of the user. `rng` is a `float`-typed number in nautical miles (nm, 海里). You should include all the airplanes that is less than `rng` nautical miles with the user. In this method, initialize your crawler with those parameter.

- `get_data_once(self)`: This method should perform a batch of requests, parse them and return all the airplane that is in range of `rng` nm of the user at `loc` at this time and store them in a temporary file (for further use in the following sub-project). You are free to design your own data type of storing as long as it contains all the following information of every airplane:

  - The longtitude and the latitude (经纬度) of the airplane;
  - The heading (航向) of the airplane;
  - The altitude (海拔高度) of the airplane;
  - The ground speed (地速), the speed of the airplane related to the ground;
  - The squawk number (应答机编号), registration number (国籍注册号) and flight number (航班号) of the flight;
  - The depature airport and the arrival airport’s IATA code of the airplane.

  Notice that you are required to store the information you get from FlightRadar24 to a temporary file, a common practice on Linux is to store it under `/tmp`. You should give the temporary file with a predictable name so that you can find it in the future when you need to access it. Before you store the file, you may need to serialize the data with some format like JSON.

Write a simple program to get the above information with all the information within 20nm to someone on campus of ShanghaiTech with your crawler every 10 seconds and display it in a beautiful way, prepare to explain how the program works to the TAs.

## Submission

You should submit a report on how you design your web crawler, including what tools you used, what requests you sent to the server and how you parse the result from the server and also your code.