# SI 100B Project: Who is Flying over? - Week 4

This week, we are going to visualize the data you crawled from FlightRadar24/FlightAware. Python and many third-party packages of it provide many excellent tools for you to do data processing and draw plots. `numpy` and `matplotlib` are the most used two of all available. In this part, you are going to utilize those two tools to do data aggregation over the data you crawled and display the result in plots in a web page on your web server in real time.

## Before You Start

Read the [documentation](https://matplotlib.org/contents.html) of `matplotlib`, find out how to do the following things:

- How to create a plot?
- How to draw line graph (折线图), histogram (直方图), bar chart (条形图) and pie chart (饼状图)?
- How to change the legend, x-axis label and y-axis label of a graph?
- How to save the plot as an image?

**For students who want to finish the advanced project**, go back to the documentation of Flask, find out how to do the following things:

- How to serve image with Flask?
- How to add a route (that handles new URLs) to Flask?
- How to render a HTML template with Flask with parameters?

Write a simple program to plot the function $y= x^2$ (x from -1 to 1 ) with `matplotlib` and save the plot as a PNG-formatted image. Prepare to explain your answers to those questions and your simple program to TAs during check.

## Draw the Plots

### Plot

First you need to draw the plot. Noticing that in week 1, we stored the data from FlightRadar24/FlightAware to a file on the file system, you may need to load the data from the file before you start to draw the plot.

Different people may have different ways to interpret the same set of data. In this project, you are allowed to choose your own way of interpreting the data you get and drawing your own plot. In week 1's project, you have collected a set of data from FlightRadar24/FlightAware which includes the tail number, departure city, destination city, flight number and so on. You can choose a set of them to do data aggregation and plot your own graph of the aggregated data. For example, you could explore the destination of the airplanes by plotting a bar chart of the destination of all the airplanes in sight. Come up with two ways of data aggregation and drawing your plots. Then try to implement them with `matplotlib` and `numpy`. Keep the questions above in your mind when implementing.

### Easy: Display Your Plot

This section is for students who want to finish the easy version of this sub-project.

Having implemented your data analysis and plotted, you now need to display the plot you drew on the screen of your Pi. The plot you drew should update in real time with new data from FlightRadar24/FlightAware.

### Advanced: Display through Web Server

This section is for students who want to finish the advanced version of this sub-project.

Now you have your own way to display the data. Next, you need to display the plot you drew to the user. Keep in mind that your plot should be updated in real time (i.e., after new data arrives from the crawler, the user should be able to see the graphs rendered from the new data instead of the out-of-date one once he/she refreshes).

Thinking about the following questions will help you with your decision making process:

1. When do you update your graph?  When the new data comes, or when the user request comes?
2. How do you store the data used for rendering the graph?
3. How do you store the graph after being rendered by `matplotlib`?
4. How can Flask do to read the graph you stored?

In `web_server/server.py`, continue implementing your web server in function `vis()`, so that the server could display both of the two graphs you created in the last step. To achieve this, you may need to return a HTML document to the browser that includes `<img>` tags (search for how to use it online) to the two graphs and serve the image from another URL. Also, add an additional tag to your HTML document to make the page refreshed every 5 seconds to reflect the up-to-date data (search online for how to do so. It requires you to add a simple tag to your HTML document).

Now start the project and visit `127.0.0.1:5000` on your browser to verify your implementation.

## Bonus: FlightRadar24 Replica

This is a bonus task.

The FlightRadar24 website is quite heavy. Opening it will cost you more than 30 seconds in a slow connection. Now that we have the exact data from FlightRadar24, why not create a light-weight replica of the website locally that runs faster?

This bonus task requires you to create a toy replica of FlightRadar24 to display the data you get from the website on a map.  Finishing it and passing the check will add an additional ** to your overall score.

Hint: you can use existing map APIs provided by service providers like the OpenStreetMap, Amap or Baidu Map to display the map and display the flights you crawled on it. Finishing this task requires some degree of understanding of Javascript and modern web development.

## Submission

You should submit a report on how you design this part of the project and also your code.