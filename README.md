**Palm Springs Collegiate League Baseball Analtics Internship Report**

---

### **1. Introduction**  
The [Palm Springs Collegiate League](https://psclbaseball.com/) (PSCL), hosted by the Palm Springs Power Baseball Team, focuses on providing collegiate baseball players an opporunity for player development as well as assisting any uncommitted players look for a community college or university to play at. My role with the PSCL was as a Baseball Analytics Intern, where I was responsible for tracking, cleaning, and analyzing in-game pitch data using Flightscope camera technology. My role focused on developing an interactive Looker dashboard to assist players and coaches evaluate player pitching/hitting metrics.

---

### **2. Responsibilities**  
#### **Live Game Data Tracking**  
Using FlightScope, I tracked in-game pitch data, (e.g., Pitch Speed, Pitch Launch Angle (Vertical & Horizontal), and Pitch Spin Rate & Direction), which also included batted ball metrics (e.g., Exit Velocity, and Vertical Launch Angle). Based on these metrics and in-game observations, I would tag the pitch type of each recorded pitch. After each game, I uploaded the data to a central folder for further analysis.

#### **Data Cleaning & Standardization**  
Due to environmental challenges and technological limitations, some pitch data would often contain missing values and inconsistencies. My responsibilities included:
- Identifying and removing NaN/null values from datasets.
- Standardizing player names across different datasets to avoid duplication.
- Resolving duplicate player records caused by variations in name formats (e.g., "John Doe" vs. "John Doe (#12)").

I developed a Python script, **Data Cleaning.py**, to automate the data cleaning process and ensure accuracy before analysis.

#### **Data Integration**  
To also include player statistics, I merged FlightScope data with:
- **[HomeTeamsOnline (HTO)](https://www.hometeamsonline.com/teams/Default.asp?s=baseball&u=PALMSPRINGSCOLLEGIAT):** PSCL league website for statistics. Provided standard pitching and batting statistics for each player. 
- **GameChanger:** A scorekeeping app that recorded advanced player statistics based on play-by-play scorekeeping.

Using the **Merge Files.py** script, I combined both of these sources to create a comprehensive dataset that contained both basic and advanced statistics.

#### **[Dashboard Development](https://lookerstudio.google.com/u/0/reporting/489badb7-a77f-4fb5-9505-fa4db8bb8d4f/page/p_p8gi1iux6c/edit)**  
To facilitate visualization and analysis, I developed an interactive Looker Studio dashboard with key features including:
- **Pitching Metrics:** Maximum and average velocity/spin rate tables, pitch distribution pie charts, and pitch result bar graphs.
- **Hitting Metrics:** Tables displaying maximum exit velocity, average launch angle, and average exit velocity for individual players and pitch types.

This dashboard provided a user-friendly interface for coaches and players to track their performance and showcase their metrics to any college scouts.

---

### **3. Challenges and Solutions**  
#### **Extreme Weather Conditions**
The biggest challenge that I came across was the fact that the average temperature in Palm Springs during the summer is 108ºF. This would ultimately cause the FlightScope camera to overheat, which would lead to data loss. As a workaround, I had to:
- Monitor the equipment to minimize downtime.
- Identify and flag missing or incomplete data.

---

### **4. Tools and Technologies Used**  
- **FlightScope** (for data collection)
- **Python** (for data cleaning and merging)
  - I used the Pandas and NumPy libraries
- **Looker Studio** (for dashboard development)
- **HomeTeamsOnline & GameChanger** (for additional statistics)

---

### **5. Internship Outcomes and Impact**  
- The Looker Studio dashboard improved accessibility to performance metrics for both pitchers and hitters.
- Coaches and players would use the dashboard to track performance trends and identify areas for improvement (e.g., a hitter's average vertical launch angle is too low, meaning they're hitting the grounders too often).
- Any college scouts benefited from the visualization tools.

---

### **6. Conclusion**  
This internship provided me with hands-on experience in baseball analytics, data cleaning, and visualization. I not only improved my skills in Python scripting and data cleaning, but also learning how to create dashboards. If I were to do this internship again, I would attempt at creating any machine learning models to predict pitch effectiveness or even pitch type, (in case I or the other interns tagged the pitch wrong), and expanding the dashboard to incorporate the player statistics from HTO and GameChanger.
