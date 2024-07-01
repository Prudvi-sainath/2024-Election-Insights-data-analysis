import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/Prudv/OneDrive/Desktop/ns/all_table_data.csv'
df = pd.read_csv(file_path)

df['Margin'] = pd.to_numeric(df['Margin'].str.replace(',', ''), errors='coerce')
df['Total Votes'] = pd.to_numeric(df['Total Votes'], errors='coerce')

reports_dir = 'C:/Users/Prudv/OneDrive/Desktop/ns/reports1'
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

# Insight 1. Total Seats Won by Each Party
seats_by_party = df['Party'].value_counts().reset_index()
seats_by_party.columns = ['Party', 'Total_Seats_Won']
plt.figure(figsize=(10, 6))
plt.bar(seats_by_party['Party'], seats_by_party['Total_Seats_Won'], color='skyblue')
plt.xlabel('Party')
plt.ylabel('Total Seats Won')
plt.title('Total Seats Won by Each Party')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'total_seats_won.png'))
plt.close()

# Insight 2. Vote Margin Analysis - Top 10 Closest Contests
closest_contests = df.nsmallest(10, 'Margin')
plt.figure(figsize=(10, 6))
plt.barh(closest_contests['Parliament Constituency'], closest_contests['Margin'], color='orange')
plt.xlabel('Margin of Votes')
plt.ylabel('Parliament Constituency')
plt.title('Top 10 Closest Contests')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'closest_contests.png'))
plt.close()

# Insight 3. Voter Turnout Analysis (Assuming 'Total Votes' can be used to approximate turnout)
turnout_by_state = df.groupby('Parliament Constituency')['Total Votes'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(turnout_by_state['Parliament Constituency'], turnout_by_state['Total Votes'], color='green')
plt.xlabel('Parliament Constituency')
plt.ylabel('Total Votes')
plt.title('Voter Turnout by Parliament Constituency')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'voter_turnout.png'))
plt.close()

# Insight 4: Representation by Party
party_counts = df['Party'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=party_counts.index, y=party_counts.values, palette='viridis', legend=False)
plt.title('Number of Seats Won by Each Party')
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'party_representation.png'))
plt.close()

# Insight 5: Largest Vote Margin
largest_margin = df.loc[df['Margin'].idxmax()]
plt.figure(figsize=(10, 6))
sns.barplot(x=[largest_margin['Party']], y=[largest_margin['Margin']], palette='viridis', legend=False)
plt.title(f'Largest Vote Margin: {largest_margin["Margin"]}')
plt.ylabel('Vote Margin')
plt.xlabel('Party')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'largest_vote_margin.png'))
plt.close()

# Insight 6: Smallest Vote Margin
smallest_margin = df.loc[df['Margin'].idxmin()]
plt.figure(figsize=(10, 6))
sns.barplot(x=[smallest_margin['Party']], y=[smallest_margin['Margin']], palette='viridis', legend=False)
plt.title(f'Smallest Vote Margin: {smallest_margin["Margin"]}')
plt.ylabel('Vote Margin')
plt.xlabel('Party')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'smallest_vote_margin.png'))
plt.close()

# Insight 7: Total Votes by Party
total_votes_by_party = df.groupby('Party')['Total Votes'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=total_votes_by_party.index, y=total_votes_by_party.values, palette='viridis', legend=False)
plt.title('Total Votes by Party')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'total_votes_by_party.png'))
plt.close()

# Insight 8: Average Margin by Party
average_margin_by_party = df.groupby('Party')['Margin'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=average_margin_by_party.index, y=average_margin_by_party.values, palette='viridis', legend=False)
plt.title('Average Vote Margin by Party')
plt.xlabel('Party')
plt.ylabel('Average Margin')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'average_margin_by_party.png'))
plt.close()

# Insight 9: Top 10 Candidates by Votes
top_10_votes = df.nlargest(10, 'Total Votes')
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_votes['Winning Candidate'], y=top_10_votes['Total Votes'], palette='viridis', legend=False)
plt.title('Top 10 Candidates by Total Votes')
plt.xlabel('Winning Candidate')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'top_10_candidates_by_votes.png'))
plt.close()

# Insight 10: Top 10 Candidates by Margin
top_10_margin = df.nlargest(10, 'Margin')
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_margin['Winning Candidate'], y=top_10_margin['Margin'], palette='viridis', legend=False)
plt.title('Top 10 Candidates by Vote Margin')
plt.xlabel('Winning Candidate')
plt.ylabel('Vote Margin')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'top_10_candidates_by_margin.png'))
plt.close()

# Insight 11: Bottom 10 Candidates by Margin
bottom_10_margin = df.nsmallest(10, 'Margin')
plt.figure(figsize=(10, 6))
sns.barplot(x=bottom_10_margin['Winning Candidate'], y=bottom_10_margin['Margin'], palette='viridis', legend=False)
plt.title('Bottom 10 Candidates by Vote Margin')
plt.xlabel('Winning Candidate')
plt.ylabel('Vote Margin')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'bottom_10_candidates_by_margin.png'))
plt.close()

# Insight 12: Votes Distribution by Party
plt.figure(figsize=(10, 6))
sns.boxplot(x='Party', y='Total Votes', data=df, palette='viridis')
plt.title('Votes Distribution by Party')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'votes_distribution_by_party.png'))
plt.close()

# Insight 13: Margin Distribution by Party
plt.figure(figsize=(10, 6))
sns.boxplot(x='Party', y='Margin', data=df, palette='viridis')
plt.title('Margin Distribution by Party')
plt.xlabel('Party')
plt.ylabel('Margin')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'margin_distribution_by_party.png'))
plt.close()

# Insight 14: Heatmap of total Votes by Party and Parliament Constituency
pivot_table = df.pivot_table(values='Margin', index='Party', columns='Parliament Constituency', aggfunc='sum', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='.1f', cmap='YlGnBu')  # Use '.1f' for float formatting
plt.title('Heatmap of Total Votes by Party and Parliament Constituency')
plt.xlabel('Parliament Constituency')
plt.ylabel('Party')
plt.tight_layout()
plt.savefig(os.path.join(reports_dir, 'heatmap_total_votes.png'))
plt.close()

print("Visualizations have been saved in the 'reports1' directory.")
