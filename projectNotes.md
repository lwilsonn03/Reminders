# Update Log
### Update September 2, 2024:
I haven't intended to abandon this project but I also haven't worked on it in a long time. I hope to pick it back up when time permits. This log unfortunately will not cover the beginning of the development of this program since I was much less aware of the value of documentation, even for personal use.

From what I remember, I worked on this program Fall 2023 primarily and it has been dormant since. I can't remember the reasons I chose to use certain libraries or why I implemented certain specific design elements. Hopefully, I'll mitigate this in the future by writing a bit each time I revisit this program.

---

### Update Oct 18, 2024:
I'm working on this on my laptop right now, which runs windows 10. I started this on my desktop that runs windows 11. This program relies on windows 11 toast to send notifications, and now I'm realizing this code might not even work on a lot of windows machines. I plan to reinvestigate how to send desktop notifications and, if applicable, add support for both windows 10 and 11. Not sure how easy it would be to incorperate linux distributions or macs into this, but I'll check this out soon.

---

### Update October 23, 2024:
The app works on a very basic level again.I've migrated from windows 11 toast to desktop-notifier which claims to support multiple OSs. I don't know how to test that, but my primary concern is polishing the program to work on windows(specifically my personal machines), then extending OS compatability. I think I'm entering a time period where I will be able to make small updates periodically.

---

### February 3, 2025:
Though I haven't worked on this project in months, it's been in the back of my mind. I'm going to try to learn JSON enough to make it work for this project, which will be an upgrade from a text file. My focus today is first ensuring this works as I remember it to, then I'll work on implementing a JSON encoding of the reminder times. 

---

### February 18, 2025:
I'm wanting to start from scratch. Looking at my own code feels overwhelming. I'm going to start from scratch, focusing on creating a functional terminal version before adding ui. Hopefully this is the right move, but if not, thank you git.

---

### February 28, 2025:

Taking a long flight today. Might be able to code depending on how cramped it is.

---

### March 1, 2025:

Made significant progress understanding json and how I want the program to be designed. Thinking I'll use github's release tagging system to retroactively create a release of the program before I started redesigning it and one for the new redesign. Not done coding today yet, but right now this program sends toasts, accepts times and randomizes/formats them for the json file, and can show the user the times listed in the json file. Toasts are currently not sent at the listed times but I'm going to work on that right now.                                                                                                                                                                                                     

---

### March 18, 2025:
I've made some progress overall and I think I've forgotten to write something in these notes once or twice. Today I've worked on get_next_time(), time_checker(), and time_as_seconds_integer(). notif() successfully runs as an asyncio task, however when it's time to be notified, the system sends waaaay too many toasts.

---

### March 24, 2025:
I'm going to push this version now despite the fact that it needs more refinement to be properly functional. I'm proud of the strides I've made in the total redesign of this program, and I want this progress to be displayed since I include this repository in the github portfolio I use when applying for jobs.

---

# immediate plans:
- correct number of notifications
- deleting times without directly editing json file

# future functionality:
- simple tkinter gui
- checking for inconsistencies and improvements to the code

# file structure:
- main: initiates and closes program
- notifs: handles toasts and sends them out at correct times
- dateandtime: handles user entry of time data and enters it to the json file
- util: broad utilities
- test: seperate file for testing