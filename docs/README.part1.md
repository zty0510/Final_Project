# SI 100B Project: Who is Flying over? - Week 1

In this week, we are finishing the very first yet important task in this project - get reliable data source of the flight nearby. There are multiple approaches to solve the problem including set up your own radio reciever to pick up the ADB-S signals which the air traffic controllers used to track the location of the airplanes they are in charge of.

However, setting up radio reciever is beyond the scope of this course. In this project, an alternative way is used. We are getting the data from a website called FlightRadar24 (https://www.flightradar24.com) with a web crawler. What this website do is distributing the radio recievers all cross the world in a crowdsourcing way to pick up the ADB-S signal and distribute the data via the internet. It have a good coverage in Shanghai.

## Determine the Data Source

The first thing to do for writing a web crawler is to determine what requests you want to send and how you will parse the response from the server.

Now, open FlightRadar24 (linked above) in your browser (a modern version of Chrome, Firefox, Safari and Edges is highly recommended) and open the developer tool of your browser. Wait until the site is fully loaded and starts to display the location of airplanes, go to the `network` tab of your developer tools. Explore the requests your browser sent out and response from the server. Determine which part of the requests is related to the dynamic updating the the page to show the up-to-date list of airplanes in a certain area. Then do the following things:

- Write down the URL of the requests and take a guess of what each part of the parameters means;
- Determine the format of the response and find a way to parse it to a structured one that Python could understand;
- Determine the meaning of each field of the response. You can do this by compare the response with the displayed values on the web page.

Write a simple program to verify the your guess in this section.

**Hint**: you are requesting https://data-live.flightradar24.com/zones/fcgi/feed.js for the flight data. One example request is to https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=31.53,30.90,120.91,122.17&faa=1&satellite=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1. Explore what does each parameter means so that you can gain some clue about how to generate your own request in next section.

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