import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="ICC Men's T20 World Cup 2024 Analysis", layout="wide")

# Load data
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stSelectbox>div>div>select {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 5px 10px;
    }
    .stTitle {
        font-size: 50px;
        font-weight: bold;
        color: yellow;
        text-transform: uppercase;
        background-color: black;
        border: 5px solid yellow;
        padding: 5px 10px;
        display: inline-block;
        border-radius: 10px;
        width: 1000px;
    }
    .stHeader {
        font-size: 40px;
        font-weight: bold;
        color: skyblue;
        text-transform: uppercase;
        background-color: black;
        border: 2px solid blue;
        padding: 5px 10px;
        display: inline-block;
        border-radius: 10px;
        width: 900px;
    }
    .spacing {
        margin-top: 50px;
        margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<div class='stTitle'>ICC Men's T20 World Cup 2024 Analysis</div>", unsafe_allow_html=True)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# Matches Analysis
st.markdown("<div class='stHeader'>1. Matches Analysis</div>", unsafe_allow_html=True)

# 1.1 Which team won the most matches?
st.markdown("<div class='stHeader'>1.1. Which team won the most matches?</div>", unsafe_allow_html=True)
win_counts = matches['winner'].value_counts()
max_wins = win_counts.max()
teams_with_most_wins = win_counts[win_counts == max_wins].index.tolist()
teams_str = ", ".join(teams_with_most_wins)
st.write(f"Teams with the most wins: {teams_str} ({max_wins} wins)")

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 1.2 Win percentage of each team
st.markdown("<div class='stHeader'>1.2. What is the win percentage of each team?</div>", unsafe_allow_html=True)
all_teams = pd.concat([matches['team1'], matches['team2']])
total_matches = all_teams.value_counts()
team_wins = matches['winner'].value_counts()
win_percentage = (team_wins / total_matches) * 100
win_percentage_sorted = win_percentage.sort_values(ascending=False)
win_percentage_sorted = win_percentage_sorted[win_percentage_sorted > 0]

fig, ax = plt.subplots(figsize=(16, 10))
sns.barplot(x=win_percentage_sorted.index, y=win_percentage_sorted, ax=ax, palette="viridis")
ax.set_title('Win Percentage of Each Team', fontsize=20, weight='bold')
ax.set_xlabel('Teams', fontsize=16, weight='bold')
ax.set_ylabel('Win Percentage', fontsize=16, weight='bold')
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right', fontsize=14, weight='bold')
ax.set_yticklabels(ax.get_yticklabels(), fontsize=14, weight='bold')
ax.set_ylim(0, 100)
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 1.3 Toss outcome and match result
st.markdown("<div class='stHeader'>1.3. How does the toss outcome affect the match result?</div>", unsafe_allow_html=True)
toss_match_outcome = matches[matches['toss_winner'] == matches['winner']]
toss_win_and_match_win_count = toss_match_outcome.shape[0]
total_matches_count = matches.shape[0]
st.write(f"Toss winner also won the match {toss_win_and_match_win_count} times out of {total_matches_count} matches.")

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 1.4 Most common venues for winning
st.markdown("<div class='stHeader'>1.4. What are the most common venues for winning?</div>", unsafe_allow_html=True)
venue_wins = matches.groupby('venue')['winner'].value_counts().sort_values(ascending=False)
most_common_venue = venue_wins.idxmax()[0]
st.write(f"The most common venue for winning: {most_common_venue}")

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 1.5 Win percentage after choosing to bat or bowl
st.markdown("<div class='stHeader'>1.5. How often do teams win after choosing to bat or bowl?</div>", unsafe_allow_html=True)
chosen_to_bat = matches[(matches['toss_decision'] == 'bat') & (matches['toss_winner'] == matches['winner'])]
chosen_to_field = matches[(matches['toss_decision'] == 'field') & (matches['toss_winner'] == matches['winner'])]
batting_win_percentage = (chosen_to_bat.shape[0] / matches.shape[0]) * 100
fielding_win_percentage = (chosen_to_field.shape[0] / matches.shape[0]) * 100
st.write(f"Percentage of wins after choosing to bat: {batting_win_percentage:.2f}%")
st.write(f"Percentage of wins after choosing to field: {fielding_win_percentage:.2f}%")

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 1.6 Team performance batting first vs chasing
st.markdown("<div class='stHeader'>1.6. How does team performance vary between batting first and chasing targets?</div>", unsafe_allow_html=True)
batting_first = matches[matches['toss_decision'] == 'bat']
chasing_target = matches[matches['toss_decision'] == 'field']
batting_first_win_percentage = (batting_first[batting_first['winner'] == batting_first['team1']].shape[0] / batting_first.shape[0]) * 100
chasing_win_percentage = (chasing_target[chasing_target['winner'] == chasing_target['team2']].shape[0] / chasing_target.shape[0]) * 100
st.write(f"Win percentage batting first: {batting_first_win_percentage:.2f}%")
st.write(f"Win percentage chasing target: {chasing_win_percentage:.2f}%")

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# Player Performance Analysis
st.markdown("<div class='stHeader'>2. Player Performance Analysis</div>", unsafe_allow_html=True)

# 2.1 Top Run Scorers
st.markdown("<div class='stHeader'>2.1. Top Run Scorers of the Tournament</div>", unsafe_allow_html=True)
top_run_scorers = deliveries.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=top_run_scorers.values, y=top_run_scorers.index, ax=ax, palette='viridis')
ax.set_title('Top Run-Scorers of the Tournament', fontsize=20, weight='bold')
ax.set_xlabel('Runs Scored', fontsize=16, weight='bold')
ax.set_ylabel('Players', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.2 Top Wicket-Takers
st.markdown("<div class='stHeader'>2.2. Top Wicket-Takers of the Tournament</div>", unsafe_allow_html=True)
top_wicket_takers = deliveries[deliveries['wicket_type'].notnull()].groupby('bowler').size().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=top_wicket_takers.values, y=top_wicket_takers.index, ax=ax, palette='plasma')
ax.set_title('Top Wicket-Takers of the Tournament', fontsize=20, weight='bold')
ax.set_xlabel('Wickets Taken', fontsize=16, weight='bold')
ax.set_ylabel('Bowlers', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.3 Players with the Highest Strike Rates
st.markdown("<div class='stHeader'>2.3. Players with the Highest Strike Rates (Runs > 150)</div>", unsafe_allow_html=True)
balls_faced = deliveries.groupby('striker').size()
runs_scored = deliveries.groupby('striker')['runs_off_bat'].sum()
strike_rate = (runs_scored / balls_faced) * 100
filtered_strike_rate = strike_rate[runs_scored > 150]
top_strike_rates = filtered_strike_rate.sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=top_strike_rates.values, y=top_strike_rates.index, ax=ax, palette='coolwarm')
ax.set_title('Players with the Highest Strike Rates (Runs > 150)', fontsize=20, weight='bold')
ax.set_xlabel('Strike Rate', fontsize=16, weight='bold')
ax.set_ylabel('Players', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.4 Players with the Best Economy Rates
st.markdown("<div class='stHeader'>2.4. Players with the Best Economy Rates (Minimum 150 Balls)</div>", unsafe_allow_html=True)
balls_bowled = deliveries.groupby('bowler').size()
runs_conceded = deliveries.groupby('bowler')['runs_off_bat'].sum() + deliveries.groupby('bowler')['extras'].sum()
economy_rate = (runs_conceded / (balls_bowled / 6))
filtered_economy_rate = economy_rate[balls_bowled >= 150]
best_economy_rates = filtered_economy_rate.sort_values().head(10)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=best_economy_rates.values, y=best_economy_rates.index, ax=ax, palette='viridis')
ax.set_title('Players with the Best Economy Rates (Min 150 Balls Bowled)', fontsize=20, weight='bold')
ax.set_xlabel('Economy Rate', fontsize=16, weight='bold')
ax.set_ylabel('Bowlers', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.5 Consistent Batters
st.markdown("<div class='stHeader'>2.5. Consistent Batters</div>", unsafe_allow_html=True)
consistent_batsmen = deliveries.groupby(['match_id', 'striker'])['runs_off_bat'].sum().groupby('striker').mean().sort_values(ascending=False).head(10)
consistent_batsmen = consistent_batsmen.reset_index().rename(columns={"striker": "Batsman", "runs_off_bat": "Striking Rate"})
st.dataframe(consistent_batsmen)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.6 Consistent Bowlers
st.markdown("<div class='stHeader'>2.6. Consistent Bowlers</div>", unsafe_allow_html=True)
consistent_bowlers = deliveries[deliveries['wicket_type'].notnull()].groupby(['match_id', 'bowler']).size().groupby('bowler').mean().sort_values(ascending=False).head(10)
consistent_bowlers = consistent_bowlers.reset_index().rename(columns={"bowler": "Bowler", 0: 'Consistency in Economy'})
st.dataframe(consistent_bowlers)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 2.7 Player Performances in Powerplay, Middle Overs, and Death Overs
st.markdown("<div class='stHeader'>2.7. Player Performances in Powerplay, Middle Overs, and Death Overs</div>", unsafe_allow_html=True)
powerplay = deliveries[deliveries['ball'].between(0.1, 6.6)]
middle_overs = deliveries[deliveries['ball'].between(7.1, 15.6)]
death_overs = deliveries[deliveries['ball'].between(16.1, 20.6)]
powerplay_performance = powerplay.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False)
middle_overs_performance = middle_overs.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False)
death_overs_performance = death_overs.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False)
top10_powerplay = powerplay_performance.head(10).sort_values(ascending=False)
top10_middle_overs = middle_overs_performance.head(10).sort_values(ascending=False)
top10_death_overs = death_overs_performance.head(10).sort_values(ascending=False)
fig, axes = plt.subplots(3, 1, figsize=(12, 18))
sns.barplot(x=top10_powerplay.values, y=top10_powerplay.index, ax=axes[0], palette="Blues_d")
axes[0].set_title('Top 10 Players in Powerplay', fontsize=20, weight='bold')
axes[0].set_xlabel('Runs Scored', fontsize=16, weight='bold')
axes[0].set_ylabel('Player', fontsize=16, weight='bold')
sns.barplot(x=top10_middle_overs.values, y=top10_middle_overs.index, ax=axes[1], palette="Greens_d")
axes[1].set_title('Top 10 Players in Middle Overs', fontsize=20, weight='bold')
axes[1].set_xlabel('Runs Scored', fontsize=16, weight='bold')
axes[1].set_ylabel('Player', fontsize=16, weight='bold')
sns.barplot(x=top10_death_overs.values, y=top10_death_overs.index, ax=axes[2], palette="Reds_d")
axes[2].set_title('Top 10 Players in Death Overs', fontsize=20, weight='bold')
axes[2].set_xlabel('Runs Scored', fontsize=16, weight='bold')
axes[2].set_ylabel('Player', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# Batting Performance Analysis
st.markdown("<div class='stHeader'>3. Batting Performance Analysis</div>", unsafe_allow_html=True)

# 3.1 Teams score the most runs per over
st.markdown("<div class='stHeader'>3.1. Teams score the most runs per over</div>", unsafe_allow_html=True)
team_runs = deliveries.groupby('batting_team')['runs_off_bat'].sum()
team_balls = deliveries.groupby('batting_team').size()
runs_per_over = team_runs / (team_balls / 6)
most_runs_per_over = runs_per_over.sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=most_runs_per_over.values, y=most_runs_per_over.index, ax=ax, palette='viridis')
ax.set_title('Runs Per Over for Each Team', fontsize=20, weight='bold')
ax.set_xlabel('Runs Per Over', fontsize=16, weight='bold')
ax.set_ylabel('Teams', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.2 Batting Performance vary by batting position
st.markdown("<div class='stHeader'>3.2. Batting Performance vary by batting position</div>", unsafe_allow_html=True)
deliveries['ball_number'] = deliveries.groupby(['match_id', 'batting_team']).cumcount() + 1
batting_positions = deliveries.groupby('ball_number')['runs_off_bat'].sum()
balls_faced_positions = deliveries.groupby('ball_number').size()
runs_per_ball_position = batting_positions / balls_faced_positions
runs_per_ball_position_df = runs_per_ball_position.reset_index()
runs_per_ball_position_df.columns = ['Batting Position', 'Runs Per Ball']
fig, ax = plt.subplots(figsize=(14, 8))
sns.lineplot(data=runs_per_ball_position_df, x='Batting Position', y='Runs Per Ball', marker='o', color='purple', linewidth=2.5, ax=ax)
ax.set_title('Average Runs Per Ball by Batting Position', fontsize=20, weight='bold')
ax.set_xlabel('Batting Position (Cumulative Balls Faced)', fontsize=16, weight='bold')
ax.set_ylabel('Average Runs Per Ball', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.3 Most Successful Batting Partnerships
st.markdown("<div class='stHeader'>3.3. Most Successful Batting Partnerships</div>", unsafe_allow_html=True)
partnerships = deliveries.groupby(['match_id', 'striker', 'non_striker'])['runs_off_bat'].sum()
successful_partnerships = partnerships.groupby(['striker', 'non_striker']).sum().sort_values(ascending=False).reset_index()
top_partnerships = successful_partnerships.head(10)
top_partnerships['partnership'] = top_partnerships['striker'] + ' & ' + top_partnerships['non_striker']
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(data=top_partnerships, x='runs_off_bat', y='partnership', ax=ax, palette='viridis')
ax.set_title('Top 10 Successful Partnerships in the Tournament', fontsize=20, weight='bold')
ax.set_xlabel('Total Runs Scored', fontsize=16, weight='bold')
ax.set_ylabel('Partnership', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.4 Frequency of Boundaries Affect the Overall Score
st.markdown("<div class='stHeader'>3.4. Frequency of Boundaries Affect the Overall Score</div>", unsafe_allow_html=True)
boundaries = deliveries[deliveries['runs_off_bat'].isin([4, 6])]
team_boundaries = boundaries.groupby('batting_team').size()
team_total_runs = deliveries.groupby('batting_team')['runs_off_bat'].sum()
boundary_percentage = (team_boundaries / team_total_runs) * 100
boundary_percentage = boundary_percentage.reset_index()
boundary_percentage.columns = ['batting_team', 'boundary_percentage']
boundary_percentage = boundary_percentage.sort_values(by='boundary_percentage', ascending=False)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(data=boundary_percentage, x='boundary_percentage', y='batting_team', ax=ax, palette='coolwarm')
ax.set_title('Percentage of Runs from Boundaries by Team', fontsize=20, weight='bold')
ax.set_xlabel('Boundary Percentage', fontsize=16, weight='bold')
ax.set_ylabel('Team', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.5 Percentage of Balls are Dot Balls
st.markdown("<div class='stHeader'>3.5. Percentage of Balls are Dot Balls</div>", unsafe_allow_html=True)
dot_balls = deliveries[deliveries['runs_off_bat'] == 0]
team_dot_balls = dot_balls.groupby('batting_team').size()
dot_ball_percentage = (team_dot_balls / team_balls) * 100
dot_ball_percentage = dot_ball_percentage.reset_index()
dot_ball_percentage.columns = ['batting_team', 'dot_ball_percentage']
dot_ball_percentage = dot_ball_percentage.sort_values(by='dot_ball_percentage', ascending=False)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(data=dot_ball_percentage, x='dot_ball_percentage', y='batting_team', ax=ax, palette='YlGnBu')
ax.set_title('Percentage of Dot Balls by Team', fontsize=20, weight='bold')
ax.set_xlabel('Dot Ball Percentage', fontsize=16, weight='bold')
ax.set_ylabel('Team', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.6 Relationship between Strike Rate and Average Runs per Over for Different Batsmen
st.markdown("<div class='stHeader'>3.6. Relationship between Strike Rate and Average Runs per Over for Different Batsmen</div>", unsafe_allow_html=True)
batsman_runs = deliveries.groupby('striker')['runs_off_bat'].sum()
batsman_balls = deliveries.groupby('striker').size()
strike_rate = (batsman_runs / batsman_balls) * 100
batsman_runs_per_over = batsman_runs / (batsman_balls / 6)
strike_rate_runs_per_over = pd.DataFrame({'Strike Rate': strike_rate, 'Runs per Over': batsman_runs_per_over})
fig, ax = plt.subplots(figsize=(12, 8))
plt.scatter(strike_rate_runs_per_over['Strike Rate'], strike_rate_runs_per_over['Runs per Over'], alpha=0.8, color='b')
ax.set_title('Relationship between Strike Rate and Runs per Over', fontsize=20, weight='bold')
ax.set_xlabel('Strike Rate', fontsize=16, weight='bold')
ax.set_ylabel('Runs per Over', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# 3.7 How do different batting orders (opening vs. middle order) affect total scores?
st.markdown("<div class='stHeader'>3.7. How do different batting orders (opening vs. middle order) affect total scores?</div>", unsafe_allow_html=True)
deliveries['batting_order'] = deliveries['ball_number'].apply(lambda x: 'Opening' if x <= 24 else 'Middle Order')
order_runs = deliveries.groupby('batting_order')['runs_off_bat'].sum()
fig, ax = plt.subplots(figsize=(10, 6))
bars = plt.bar(order_runs.index, order_runs.values, color=['skyblue', 'lightgreen'])
ax.set_title('Total Runs by Batting Order', fontsize=20, weight='bold')
ax.set_xlabel('Batting Order', fontsize=16, weight='bold')
ax.set_ylabel('Total Runs', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# Bowling Performance Analysis
st.markdown("<div class='stHeader'>4. Bowling Performance Analysis</div>", unsafe_allow_html=True)

# 4.1 The Impact of Dot Balls on the Opposition's Scoring Rate
st.markdown("<div class='stHeader'>4.1. The Impact of Dot Balls on the Opposition's Scoring Rate</div>", unsafe_allow_html=True)
deliveries['is_dot'] = deliveries['runs_off_bat'].apply(lambda x: 1 if x == 0 else 0)
dot_ball_impact = deliveries.groupby('match_id')['is_dot'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
plt.scatter(dot_ball_impact.index, dot_ball_impact * 100, color='red', alpha=0.5)
ax.set_title('Impact of Dot Balls on Scoring Rate', fontsize=20, weight='bold')
ax.set_xlabel('Match ID', fontsize=16, weight='bold')
ax.set_ylabel('Dot Ball Percentage (%)', fontsize=16, weight='bold')
st.pyplot(fig)

# Add spacing
st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

# Thank You
st.markdown("<div class='stTitle'>Thank You So Much</div>", unsafe_allow_html=True)