# SI 100B Project: Who is Flying over? - Week 3

From this week on, this project will be divided into two parallel parts. The two parallel sub-projects will require you to finish the same set of functionalities for your crawler and LED controller. However, those two parallel sub-projects, namely easy and advanced, are based on different technology stack thus have different difficulty. You are only required to finish one of them. If you choose the advanced one, you will be rewarded with bonus.

In this week, you are building a web interface for controlling how your crawler and LED behave. Essentially, you are required to write a simple interface for your user, which could allow them to change the behavior of your crawler and LED.

## Easy: Building Command Line Interface

The most straightforward way to build a control panel for beginner is to build a command line interface (CLI). You should have used some sort of CLI in SI100B. The shell on your computer and the interactive Python interpreter are both example of CLI. The easy level of the project require you to build a simple CLI that could change the behavior of your crawler and LED controller.

A simplest CLI program works as follows: it first print out a prompt (命令提示符) asking the user to input a command. Then after the user submits the command with `enter`, the command is parsed by the program and executed. The result of the command is then printed out. Finally, another prompt is printed out, asking the user for a new input.

Read the description above, open a real CLI program (e.g., the interactive Python interpreter), and explore how it works. Answer the following questions:

- How could you get input from the user? What functions can you utilize in Python?
- How could you feed back the result to the user?

Let's get down to implement your controller in function `_main()` of `cli/cli.py`.

Your program should be able to control the following parameters of your crawler and LED:

- The central coordinate and the range of the data that the crawler is going to crawl;
- The frequency of fetching data from the FlightRadar24/FlightAware ;
- The way how your LED works. For example, change among different schemes of working or simply change the frequency of how it blinks.

You need to design a working scheme of how to represent each one of the parameters in your CLI. For example, in our design, we use `set coord 30 104` to ask the program to change the central coordinate to 30N,104E. You are allowed to design your own way of representing each of the commands in your program. You should also include a command in your program to display all the parameters currently in use.

**Hint on implementation**: You may have noticed that the program you are currently writing works separately with your crawler and LED controller. There is no direct way of communicating between them. You should come up with a way to pass on the parameters' change among the CLI program, your crawler and LED controller. Following are some possible ways (in the increasing order of difficulty):

- Use a file. Serialize the parameters to a universal format (like JSON), store it somewhere in the file system. Let the crawler to check the parameter change in the file periodically;
- Use the IPC primitives provided by the Python `multiprocessing` module. Read `main.py` and try to understand how it create two processes. Then read the documentation of the `multiprocessing` module. You can figure out what primitive to use and how to use it;
- Use the UNIX socket. You can also use the UNIX domain socket provided by Linux. Refer to the manual page and some kind of system programming guide if you want to try this approach;
- Use some kind of key-value store. This is a totally overkill for this project. However, many large-scale projects will use this approach. This requires you to set up some kind of key-value store database like `redis` on your machine and use it for data transferring.

Test your CLI by running `main.py` directly. `main.py` will start your cralwer, your LED conrtoller and this CLI for you.

Following is how our CLI program outputs:

```bash
>>> set coord 30 104
Coodinate: 30.0, 104.0
>>> set range 100
Range: 100 nm
>>> show coord
Coodinate: 30.0, 104.0
```

## Advanced: Building Web Server

This section describes the project specification for the advanced project based on web development. Choosing this project require you to learn about some basics of web development through online reading. Web development nowadays is a quite complicated thing. However, in this project you are only required to implement the simplest functionality and since we are using Python, you have many handy tools like Flask that could aid you in writing a working application in a short period of time.

In this part of the project, you are writing a simple web control panel for your crawler. For the web server, we are using a lightweight web framework called Flask. Your Pi should have Flask installed. If it is not installed, run `pip3 install flask` in your terminal.

First, read the [documentation](https://flask.palletsprojects.com/en/1.1.x/) of Flask. Learn how to do the following things:

- How to serve the request sent from the client for a specific path? For example, if a request is requesting the path `/public` on your server and another one is requesting `/confidential` on your server, how could you distinguish them and send different responses?
- How to serve different request methods? For example, one request is sent to your server for the path `/public` with a `GET` method and another one with a `POST` method, how could you distinguish them and send different responses?
- How to render a HTML template in Flask? How to create a simple template in Flask?
- How to get the form data the user sent to your server in a `POST` request? Which data type is it?

Then read this [documentation](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started), this [documentation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form) and other online resources. Learn how to do the following things:

- How to specify the title of a web page? How to add a paragraph to a web page? How to add a title to a web page?
- How to design a form on a web page? How to add text box to your form? How to add an option to your form?
- How to send the content of the form to the server? What HTTP methods are generally used for those requests? In Flask, how will you handle the request containing a form?

Prepare your answer in your project report of this week.

Let’s get down to the real work. You are filling the `web_server/server.py` file this week. The framework of this file is provided. The script is already good for run except that you will get a HTTP `500` error every time you access a page on it. You can run it by `python3 web_server/server.py` and open the page it serves by opening `http://<pi-ip>:8999` in your browser. Walk through the script, and make sure you understand the meaning of each part of the code.

Then, you need to implement the control panel at `http://<pi-ip>:8999/config`. The control panel should support changing the following parameters:

- The central coordinate and the range of the data the crawler is going to crawl;
  - The frequency of fetching data from the FlightRadar24/FlightAware website;
- The way how your LED works. For example, change among different schemes of working or simply change the frequency of how it blinks.

Your control panel should display the parameters currently in use to the visitor and present a simple form to the user which allows the user to change those parameters. Changes of the parameters should be reflected on the behavior of the LED and crawler next time you fetch data from FlightRadar24/FlightAware. You need to think about how to transfer the changed parameters to the crawler (hint below) and which part of your crawler should be changed.

Once you finish your implementation, run `python3 main.py`, verify if your server works and whether the changes in those parameters will influence the behavior of your crawler and LEDs.

**Hint on implementation**: You may have noticed that the web server and the crawler works separately in different processes in this implementation. One problem brought to us is how should we send the changed parameters between those two processes. Linux provides multiple ways for you to do such kind of information transferring (formally, it is called IPC). We name a few hints of how to do it in this project (in the increasing order of difficulty):

- Use a file. Serialize the parameters to a universal format (like JSON), store it somewhere in the file system. Let the crawler to check the parameter change in the file periodically;
- Use the IPC primitives provided by the Python `multiprocessing` module. Read `main.py` and try to understand how it create two processes. Then read the documentation of the `multiprocessing` module. You can figure out what primitive to use and how to use it;
- Use the UNIX socket. You can also use the UNIX domain socket provided by Linux. Refer to the manual page and some kind of system programming guide if you want to try this approach;
- Use some kind of key-value store. This is a totally overkill for this project. However, many large-scale projects will use this approach. This requires you to set up some kind of key-value store database like `redis` on your machine and use it for data transferring.

You are required to explain which approach you take (or any other approach you used) to the TA.

## Submission

You should submit a report on how you design this part of the project and also your code.

