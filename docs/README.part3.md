# SI 100B Project: Who is Flying over? - Week 3

In this week, you are building a web interface for controlling how your crawler and LED behave. Essentially, you are required to write a simple web server that could serve web pages that could be accessed through the web browser. Web development nowadays is a quite complicated thing. However, in this project you are only required to implement the simplest functionality and since we are using Python, you have many handy tools like Flask that could aid you to write a working application in a short period of time.

## Basics of HTTP and HTML

### HTTP

HTTP, or the Hyper-text Transfer Protocol, is the underlying protocols used by web server and your web browsers to transfer data. Generally, how the HTTP works is that the user agent (your web browser) initalize a connection to the web server and it send information including what resource on the server it want to access (the URL, like `http://sist.shanghaitech.edu.cn/`) and how it want to access the resource (e.g., to retrive it or to modify it? Formally, it is called method. Examples includes `GET` and `POST`). After recieve the request from the user agent, the server will send back resources the user want along with a status code indicating the status of the request (is it successful? If an error occurred, is it the problem of the server or the client?). 

An example of HTTP request / response is given below:

The client (user agent) send out the following request

```http
GET / HTTP/1.1
Host: www.example.com
User-Agent: curl/7.54.0
```

The server will typically reply with the following

```http
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Thu, 16 Jul 2020 12:42:13 GMT
Content-Type: text/html; charset=utf-8

<html>
<head>
<title>Welcome</title>
</head>
<body>
<p>It works!</p>
</body>
</html>
```

This conversation is basically for the client trying to get the `/` directory of the server `www.example.com`. The server reply with a `200` status code indicating the request is successful and the content of the requested resource is attached below the headers as `<html>....</html>`. Other possible status codes includes`400` indicating the client’s request could not be processed,  `404` indicating the resource could not be found on the server and `500` indicating an error occurred inside the server when processing the request.

For more information about HTTP, consult [Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) or the [W3School](https://www.w3schools.com/whatis/whatis_http.asp).

### HTML

HTTP solves the problem of transferring a file from a computer to another. HTML, or the **H**yper **T**ext **M**arkup **L**anguage, solves the problem of encoding the style information of a web page. It represent the documentation as a tree of labels.

// TBA

For more information about the HTML, consult [Wikipedia](https://en.wikipedia.org/wiki/HTML) or [W3School](https://www.w3schools.com/whatis/whatis_html.asp).

## Building Your Web Server

In this part of the project, you are writing a simple web control panel for your crawler. For the web server, we are using a lightweight web framework called Flask. Your Pi should have Flask installed. If it is not installed, run `pip3 install flask` in your terminal.

First, read the [documentation](https://flask.palletsprojects.com/en/1.1.x/) of Flask. Learn how to do the following things:

* How to serve the request sent from the client for a specific path? For example, if a request is requesting the path `\public` on your server and another one is requesting `\confidential` on your server, how could you distinguaish them and send different response?
* How to serve the different request methods? For example, one request is sent to your server for the path `\public` with a `GET` method and another one with a `POST` method, how could you distinguatish them and send different response?
* How to render a HTML template in Flask? How to create a simple template in Flask?
* How to get the form data the user send to your server in a `POST` request? What data type is it?

Then read this [documentation](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started), this [documentation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form) and other online resources. Learn how to do the following things:

* How to specify the title of a web page? How to add a paragraph to a webpage? How to add a title to a web page?
* How to desgin a form on a web page? How to add text box to your form? How to add an option to your form?
* How to send the content of the form to the server? What HTTP methods are generally used for those requests? In flask, how will you handle the request containing a form?

Prepare your answer in your project report of this week.

Let’s get down to the real work. You are filling the `web_server\server.py` file this week. The skeclon of this file is provided. The script is already good for run except that you will get a HTTP `500` error every time you access a page on it. You can run it by `python3 web_server\server.py` and open the page it serves by openning `http://<pi-ip>:8999` in your browser. Walk through the script, make sure you understand the meaning of each part of the code.

Then, you need to implement the control panel at `http://<pi-ip>:8999/config`. The control panel should support tunning the following parameter:

* The central coordinate and the range of the data the crawler is going to crawl;
* The frequency of fetching data from the FlightRadar24 website;
* The way how your LED works. For example, change between different scheme of working or simply change the frequency of how it blinks.

Your control panel should display the parameters currently in use to the vistitor and present a simple form to the user which allows the user to change those parameters. Change in the parameters should be reflected on the behavior of the LED and crawler when the next time you are fetching data from FlightRadar24. You need to think about how to transfer the changed parameters to the crawler (hint below) and which part of your crawler should be changed.

Once you finish your implemantation, run `python3 main.py`, verify if your server works and whether the changes in those parameters will influence the behavior of your crawler and LEDs.

**Hint on implementation**: You may have noticed that the web server and the crawler works seperately in different process in this implementation. One problem brought to us is how should we send the changed parameters between those two process. Linux provided multiple ways for you to do such kind of information transferring (formally, it is called IPC). We name a few hints of how to do it in this project (in the order from the simplest to hardest):

* Use a file. Serailize the parameters to a universal format (like JSON), store it somewhere on the file system. Let the crawler to check the parameter change in the file periodically;
* Use the IPC primitives provided by the Python `multiprocessing` module. Read `main.py`, understand how it create two processes. Then read the documentation of the  `multiprocessing` module. You can figure out what primitive to use and how to use it;
* Use the UNIX socket. You can also use the UNIX domain socket provided by Linux. Refer the manual page and some kind of system programming guide if you want to try this approach;
* Use some kind of key-value store. This is a totally overkill for this project. However, many large-scale web project will use this approach. This requires you to set up some kind of key-value store database like `redis` on your machine and use it for data transferring.

You are required to explain which approach you take (or any other approach you used) to the TA.