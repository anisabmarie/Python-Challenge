import pandas as pd
poll_df = pd.read_csv ('/Users/anisabraun/Desktop/election_data.csv')
poll_df.head()
#The total number of votes cast
len(poll_df)

#A complete list of candidates who received votes
print(poll_df.groupby(['Candidate'],as_index=False).count())

#The percentage of votes each candidate won
poll_df['Candidate'].value_counts(normalize=True) * 100
poll_df.max()