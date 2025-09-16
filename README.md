#CODTECH-TASK-1

COMPANY : CODTECH IT SOLUTIONS

NAME : AJAY NEGI

INTERN ID : CT08DY1001

DOMAIN : PYTHON PROGRAMMING

DURATION : 8 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

This project is a simple weather visualization dashboard built using Python, the OpenWeatherMap API, and Matplotlib. It allows users to fetch real-time weather data for a specified city and displays it in both numerical and graphical formats. The dashboard focuses on key weather parameters such as temperature, "feels like" temperature, humidity, and general weather conditions. The project demonstrates how to integrate external APIs with Python, handle data in JSON format, and create clear, professional visualizations for end-users.

The script starts by sending an HTTP request to the OpenWeatherMap API using the requests library. Users need to provide a valid API key and the city for which they want the weather data. The API request uses HTTPS to ensure secure communication. Upon successful response, the script extracts important weather details, including the current temperature, perceived temperature (feels like), humidity, and a textual weather description such as “clear sky” or “light rain.” These values are printed to the console for immediate reference, making it easy to verify the data before visualization.

Once the data is retrieved, the project uses Matplotlib to create two types of visualizations. First, a bar chart compares the current temperature and "feels like" temperature, providing an intuitive visual understanding of how the weather actually feels. The chart uses distinct colors for clarity, labels for the axes, and appropriate scaling to make the differences between values clear. Second, a pie chart illustrates the humidity percentage, highlighting how much moisture is present in the air compared to the remaining atmospheric composition. The use of contrasting colors and percentage labels makes this visualization easy to interpret at a glance.

To enhance readability and aesthetics, the dashboard includes titles, subtitles, and additional text annotations. A main figure title displays the city name, while supplementary text provides context such as the current weather description. Layout adjustments ensure that charts do not overlap, and the overall figure is formatted neatly for presentation. This approach combines numerical information with clear visual representation, making it ideal for educational purposes, quick weather checks, or even embedding into larger projects such as personal dashboards or IoT weather stations.

The script also includes robust error handling to account for common issues such as incorrect API keys, network problems, or unavailable city data. Specific exceptions handle HTTP errors, connection issues, timeouts, and other unexpected request failures, providing informative messages to the user. This ensures that the program is both reliable and user-friendly, even in the case of failures.

From a technical perspective, this project highlights best practices in API integration, JSON data handling, and data visualization using Python. It demonstrates how small scripts can combine real-time data access and graphical display to create interactive, informative dashboards. Future improvements could include adding multiple cities in a single dashboard, incorporating more weather metrics such as wind speed or air pressure, and exporting visualizations as images or interactive web dashboards.

In conclusion, this project serves as a practical example of using Python to fetch, process, and visualize real-time weather data, combining programming, API interaction, and visualization skills. It is lightweight, educational, and highly adaptable, providing a foundation for anyone interested in creating personal weather tools, learning data visualization, or exploring real-time API applications in Python.




#OUTPUT

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/63bb7aea-c430-442e-841d-55f54377e41f" />
