Introduction:
Air traffic management is a critical component of modern aviation. The efficient and safe 
management of air traffic requires timely and accurate data about flights and airports. In this 
project, we have designed and implemented an analytical platform to analyze air traffic data 
in almost real-time. The primary objective of this project is to build a solution that allows us 
to monitor air traffic in Poland. The data analysis is implemented in a distributed manner 
using Spark and queuing systems.
To accomplish this objective, we used the Aviationstack API to retrieve real-time flight data 
for various airports in Poland. The data includes information about the airline, flight number, 
departure and arrival times, and flight status. We processed the data using the Python 
programming language and Pandas library to create a data frame that can be easily analyzed 
and visualized. We used Spark to perform distributed data processing to optimize the speed of 
data analysis.
This report summarizes the methods used, the results obtained, and the insights gained from 
the data analysis. We also discuss the limitations of our approach and potential future 
directions for the project.
Data Sources:
The data for this project was obtained from the Aviationstack API 
( https://aviationstack.com/documentation ). The API provides access to real-time flight data 
for airports around the world, including Poland. We used the API to retrieve flight data for the 
following airports in Poland: Warsaw Chopin Airport (WAW), Gdańsk Lech Wałęsa Airport 
(GDN), Katowice International Airport (KTW), Poznań Ławica Airport (POZ), and 
Wrocław–Copernicus Airport (WRO).
The data provided by the API includes information about the airline, flight number, departure 
and arrival times, and flight status. The data is returned in JSON format, which we parsed 
using the Python programming language and the Requests library. We used the Pandas library 
to create a data frame from the parsed data, which we then used for our data analysis.
In addition to the Aviationstack API, we also used Spark to perform distributed data 
processing. Spark is an open-source data processing framework that provides a fast and 
flexible way to process large datasets. We used Spark to process the flight data and optimize 
the speed of data analysis.
Overallf the Aviationstack API provided us with a robust data 
source and efficient data processing framework that allowed us to perform real-time data 
analysis of air traffic in Poland
Data processing:
The raw data for the air traffic in Poland was obtained from the AviationStack API, which 
provides real-time flight information, including flight numbers, airlines, departure and arrival 
airports, and flight status. The API was accessed using the requests library in Python, with the 
relevant parameters being passed in the params dictionary.
Once the data was obtained, it was processed using the pandas library in Python, which 
provides powerful data manipulation and analysis capabilities. The raw data was converted 
into a Pandas DataFrame, which allows for easy filtering and aggregation of the data.
In order to obtain a comprehensive view of air traffic in Poland, data was collected for all 
possible airport combinations for departure and arrival. The resulting DataFrame contains 
information on the flight date, airline, flight number, flight status, departure airport, and 
arrival airport.
To avoid exceeding the API rate limit, a 10-second delay was added between each API call.
The resulting data can be used to analyze various aspects of air traffic in Poland, such as the 
busiest airports, the most popular airlines, and the most common flight routes
While the current implementation of the analytical platform has achieved the initial objective 
of monitoring air traffic in Poland in real-time, there are several areas for potential future 
work.
One area for improvement could be to incorporate more data sources and expand the analysis 
beyond just flight data. This could include incorporating weather data, flight route data, and 
passenger data to provide a more comprehensive view of air traffic in Poland.
next is some results of our run the code 
![image](https://user-images.githubusercontent.com/115592344/219494305-d8508fbf-2ad6-4240-93f5-be09cbd371f5.png)
![image](https://user-images.githubusercontent.com/115592344/219494426-1c0b952c-efde-4278-acc2-62d419389bba.png)
