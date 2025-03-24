## Short description
This is a personal project designed to send desktop notifications at slightly randomized times. Inside the app, times of reminders can be added, edited, and saved. The program can run while minimized and send a reminder with a set message at specified times. This was concieved to help me during long class sessions where it's difficult to focus the whole time. The purpose of the randomization is so that I'm not necessarily watching the clock. the notifications were designed to act as a nudge away from distractions.

## Current state
I've started over from scratch because I wanted to redesign several main elements of the program. As a result, this current pushed version is lacking in features compared to the previous, but I'm much more confident in the foundations I'm building. Right now the program handles 3 simple tasks, all in the terminal: sending a toast, adding a time with correct json formatting to remindtimes.json, and reading back those times. As long as the program is running, it does send toasts at the correct time, but it currently spams them for a period of 1 second. Remindtimes.json stores the requested time and the randomized actual time, so that the program can display the time the user requested even when that's not the exact time the toast will be sent. 

### Most recent update:

March 24, 2025:
I'm going to push this version now despite the fact that it needs more refinement to be properly functional. I'm proud of the strides I've made in the total redesign of this program, and I want this progress to be displayed since I include this repository in the github portfolio I use when applying for jobs.                                                                                            

## More info
- project_notes.md contains an informal log of my thoughts and updates to the program. it's also where I'm currently logging my plans for new features.





