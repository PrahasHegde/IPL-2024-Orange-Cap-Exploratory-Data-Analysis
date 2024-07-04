#Imports
import pandas as pd
import plotly.express as px

#Load the dataset
df = pd.read_csv('Orange Cap 2024.csv')
print(df.head()) #Load 1st 5 rows

#Dhoni information
print(df[df['Player'].str.contains("Dhoni")])

#CSK players information
print(df[df['Player'].str.contains('CSK')])

#most 6s in IPL2024
# Sort the DataFrame by the number of sixes in descending order and get the top 10
most_sixes = df.sort_values('6s', ascending=False).head(10)

# Create a bar plot using Plotly
fig1 = px.bar(most_sixes, x='Player', y='6s', title='Most Number of Sixes By Players')

# Show the plot
fig1.show()

#most 4s in IPL2024
most_fours = df.sort_values('4s', ascending=False).head(10)
fig2 = px.bar(most_fours, x='Player', y='4s', title='Most Number of Fours By Players')
fig2.show()

#most balls faced(BF)
most_balls_faced = df.sort_values('BF', ascending=False).head(10)
fig3 = px.bar(most_balls_faced, x='Player', y='BF', title='Most Number of Balls Faced By Players', labels={'BF':'Balls Faced🏏'})
fig3.show()

#most 4s and 6s (stack)
fig4 = px.bar(df.head(20), x='Player', y=['4s', '6s'], title='Most Number 6s and 4s By Players', barmode='stack')
fig4.show()

#most4s and 6s (Group)
fig5 = px.bar(df.head(20), x='Player', y=['4s', '6s'], title='Most Number 6s and 4s By Players', barmode='group')
fig5.show()


#Balls faced vs Runs scored scatter plot
fig6 = px.scatter(df.head(20), x='BF', y='Runs', color='Player', title='Balls Faced Vs Runs Scored', labels={'BF':'Balls Faced'})
fig6.show()


#Players With 200+ Strike Rate (Faced min. 50 Balls)
good_strike_rate = df[(df['BF'] > 50) & (df['SR'] > 200)]
fig7 = px.bar(good_strike_rate, x='Player', y='SR', title="Players With 200+ Strike Rate (Faced atleast 50 Balls", labels={'SR':'Strike Rate'})
fig7.show()

#players with most 0s
ducks = df.sort_values('0', ascending=False).head(10)
fig8 = px.bar(ducks, x='Player', y='0', labels={'0':'🦆'}, title='Players With Most 🦆s',color = 'Player')
fig8.show()

#top scorers for RCB
top_rcb_scorer = df[df['Player'].str.contains('RCB')]
fig9 = px.bar(top_rcb_scorer,x = 'Player',y='Runs',title='RCB top scoerer')
fig9.show()

#top scorers for MI
top_mi_scorer = df[df['Player'].str.contains('MI')]
fig10 = px.bar(top_mi_scorer,x = 'Player',y='Runs',title='MI top scoerer')
fig10.show()

#most 50s and 100s in IPL2024
fifty_tons = px.bar(df.head(20), x='Player', y=['50', '100'], title='Most Number 50 and 100 By Players', barmode='group')
fifty_tons.show()


#player average for SRH
srh_avg = df[df['Player'].str.contains('SRH')]
fig11 = px.bar(srh_avg, x='Player', y='Ave', title="SRH Players With average")
fig11.show()

#matches played for KKR
macthes_played_kkr = df[df['Player'].str.contains('KKR')]
fig12 = px.bar(macthes_played_kkr,x='Player', y='Mat',title='Matches plaued for KKR',color='Mat')
fig12.show()