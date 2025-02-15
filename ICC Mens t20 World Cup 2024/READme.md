# ICC Men's T20 World Cup 2024 Analysis

## Overview
This project is a comprehensive analysis of the **ICC Men's T20 World Cup 2024** using Python, Streamlit, and data visualization libraries like Matplotlib and Seaborn. The goal of this project is to provide insights into match outcomes, player performances, batting and bowling statistics, and other key metrics from the tournament. The analysis is presented in an interactive and visually appealing web application built using Streamlit.

The app is divided into four main sections:
1. **Matches Analysis**: Insights into match results, win percentages, toss outcomes, and venue performance.
2. **Player Performance Analysis**: Top run-scorers, wicket-takers, strike rates, economy rates, and consistent performers.
3. **Batting Performance Analysis**: Team batting performance, partnerships, boundary frequency, and dot ball analysis.
4. **Bowling Performance Analysis**: Impact of dot balls on scoring rates and other bowling metrics.

---

## Features
### 1. **Matches Analysis**
- **Most Wins**: Identifies the team(s) with the most wins in the tournament.
- **Win Percentage**: Calculates and visualizes the win percentage of each team.
- **Toss Impact**: Analyzes how often the toss winner wins the match.
- **Venue Performance**: Highlights the most common venues for winning matches.
- **Batting vs Fielding**: Examines the win percentage when teams choose to bat or field after winning the toss.

### 2. **Player Performance Analysis**
- **Top Run Scorers**: Displays the top 10 run-scorers in the tournament.
- **Top Wicket-Takers**: Lists the top 10 wicket-takers.
- **Strike Rates**: Shows players with the highest strike rates (minimum 150 runs).
- **Economy Rates**: Highlights bowlers with the best economy rates (minimum 150 balls bowled).
- **Consistent Performers**: Identifies consistent batters and bowlers based on their average performance.

### 3. **Batting Performance Analysis**
- **Runs Per Over**: Analyzes which teams score the most runs per over.
- **Batting Position Impact**: Examines how batting positions affect run-scoring.
- **Successful Partnerships**: Identifies the most successful batting partnerships.
- **Boundary Impact**: Measures the frequency of boundaries and their impact on total scores.
- **Dot Ball Analysis**: Calculates the percentage of dot balls for each team.

### 4. **Bowling Performance Analysis**
- **Dot Ball Impact**: Analyzes how dot balls affect the opposition's scoring rate.

---

## Technologies Used
- **Python**: The core programming language used for data analysis and visualization.
- **Streamlit**: A powerful framework for building interactive web applications.
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations.
- **Seaborn**: A statistical data visualization library built on top of Matplotlib.
- **CSV Files**: The data is stored in two CSV files (`matches.csv` and `deliveries.csv`), which contain match and ball-by-ball details.

---

## How to Run the Project
### Prerequisites
1. Install Python (version 3.8 or higher).
2. Install the required libraries using the `requirements.txt` file.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/ZainFaisal005/DataCraft-Analysis-Vault/tree/main/ICC%20Mens%20t20%20World%20Cup%202024.git
   cd ICC%20Mens%20t20%20World%20Cup%202024
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

---

## Deployment on Hugging Face
The app is deployed on **Hugging Face Spaces**, making it accessible to anyone with an internet connection. You can explore the live app by clicking the link below:

👉 **[Live App on Hugging Face](https://huggingface.co/spaces/ZainFaisal/ICC-Mens-t20-World-Cup-2024-ANALYSIS)**

---

## Data Sources
The project uses two main datasets:
1. **`matches.csv`**: Contains match-level data, including teams, toss decisions, winners, and venues.
2. **`deliveries.csv`**: Contains ball-by-ball data, including runs scored, wickets taken, and bowler/striker details.

These datasets are assumed to be preprocessed and cleaned before being used in the analysis.

---

## Project Structure
```
icc-t20-world-cup-2024-analysis/
├── app.py                # Main Streamlit application code
├── matches.csv           # Match-level dataset
├── deliveries.csv        # Ball-by-ball dataset
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
```

---

## Key Insights
1. **Team Performance**: Teams with higher win percentages often perform better in high-pressure situations.
2. **Player Impact**: Consistent performers and players with high strike rates significantly influence match outcomes.
3. **Toss Advantage**: Winning the toss and choosing to field first often leads to a higher chance of winning.
4. **Boundary Impact**: Teams with a higher percentage of boundaries tend to score more runs overall.
5. **Dot Ball Impact**: Bowlers who bowl more dot balls can effectively restrict the opposition's scoring rate.

---

## Future Enhancements
1. **Interactive Filters**: Add filters to allow users to explore data for specific teams, players, or venues.
2. **Advanced Visualizations**: Include more advanced visualizations like heatmaps and radar charts.
3. **Machine Learning**: Predict match outcomes or player performances using machine learning models.
4. **Live Data Integration**: Fetch live data from APIs to keep the analysis up-to-date.

---

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or feedback, feel free to reach out:
- **Email**: zainfaisal280@gmail.com
- **GitHub**: [ZainFaisal005](https://github.com/ZainFaisal005)
- **LinkedIn**: [Zain Faisal](www.linkedin.com/in/zain-faisal-593b05239)

---

Thank you for exploring the **ICC Men's T20 World Cup 2024 Analysis** project! 🏏

👉 **[Explore the Live App on Hugging Face](https://huggingface.co/spaces/ZainFaisal/ICC-Mens-t20-World-Cup-2024-ANALYSIS)**

---