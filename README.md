# WHERE THERE'S RAIN THERE'S THUNDER 🔥🔥😵‍💫 by madeinguatemala


## Roster and Roles:  
|                                        | PMWN       | DAS        |  DKL       | DMC      |
| -------------------------------------- | ---------- | ---------- | ---------- | -------- |
| Flask setup and routing                |            |    **X**   |            |   **X**  |
| Construct Database Organization        |            |    **X**   |            |          |
| Front-end (JS)                         |    **X**   |            |   **X**    |   **X**  |
| Front-end (Bootstrap + CSS)            |   **X**    |            |   **X**    |          |
| Build HTML Templates                   |    **X**   |            |            |   **X**  |
| Final Testing and Bug Fixing           |    **X**   |    **X**   |   **X**    |   **X**  |

## Description:
<mark style="background: #BBFABBA6;">JOY ACROSS BORDERS 🔥🔥😵‍💫</mark> is a interactive platform meant to serve information regarding every country for every type of human from vacation travelers to rogue individuals seeking asylum in foreign land. Our vision of the site is to create an interactive map where clicking on any country in the world will show a general overview of the country, and graphs relating to happiness, life expectancy, etc. Logged in users will be able to set a country as their favorite which will also set their profile picture as the flag of their country. They may also choose to favorite a specific chart, which will become viewable in their collection in their account profile. <mark style="background: #BBFABBA6;">JOY ACROSS BORDERS 🔥🔥😵‍💫</mark>  collections are public. Users will also be able to leave ratings on each country based on factors that are up to their personal discretion, allowing for users to look beyond the numbers and see what fellow humans have to say about each piece of land.

## Install Guide
### Recommended Method: 
We recommend to do this procedure using the Git Clone method. Click the green button in the top right that says "Code". Then, choose "SSH" in the dropdown that appears and copy the URL that is given. Finally, open up your terminal, cd into wherever you desire to hold the folder. Then, type 
```
$ git clone git@github.com:wnzeuton/p04.git
```

### Alternate Method: 
This is an alternate method, if you don't prefer the Git Clone method. Go to the green button in the top right again that says "Code". Then, click "Download Zip". Finally, extract the ZIP file from your downloads and place it in your desired directory. 

Reagardless of which method you choose, navigate to the repo folder and type ```$ pip install -r requirements.txt``` to install required dependencies

## Launch

1. **Navigate to the repository folder**  
   Make sure you are **outside** of the `app` directory.

2. **Run the application**  
   Use the following command:
   ```bash
   python3 run.py

You should now be able to access the app at 127.0.0.1:5000.
   
### FEATURE SPOTLIGHT
* Clicking on the big globe on the homescreen will spin you into our interactive color-coded map
* Each country on the map can be accessed to view their world happiness report data
* Users can rate each country from 1-5 and access all their ratings in their profile for later referral
* Each country gets an overall rating based on the pool of reviews created by users

### KNOWN BUGS/ISSUES
* Project could not be served on PM's droplet; several seemingly mongo related issues caused app instance to timeout on droplet (at times force shutting ssh connection to droplet)
* Original world happiness report had missing data points for a few countries and didn't include data at all for some countries
* Search button (not bar) on /map has no function
* Takes extensive time to load each country
