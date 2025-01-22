from create_bar_chart_race_data import CreateBarChartRaceData
from raceplotly.plots import barplot
import pandas as pd
import plotly.express as px

create_bar_chart_race_data = CreateBarChartRaceData()
cumulative_votes_by_time_candidate = create_bar_chart_race_data.create_cumulative_votes_by_time_candidate()
covid_19_confirmed = create_bar_chart_race_data.create_covid_19_confirmed()
covid_19_deaths = create_bar_chart_race_data.create_covid_19_deaths()
covid_19_doses = create_bar_chart_race_data.create_covid_19_doses_administered()

early_collected = cumulative_votes_by_time_candidate[cumulative_votes_by_time_candidate["collected_at"] < pd.to_datetime("2024-01-13 17:30:00")]
max_cumulative_votes = early_collected["cumulative_sum_votes"].max()
fig = px.bar(early_collected,
             x="cumulative_sum_votes", y="candidate", color="candidate",
             animation_frame="collected_at", animation_group="candidate",)

vote_raceplot = barplot(early_collected, item_column="candidate", value_column="cumulative_sum_votes",
                        time_column="collected_at", top_entries=3)
fig = vote_raceplot.plot(item_label = "Votes collected by candidate", value_label="Number of votes",
                         frame_duration=50)


max_confirmed = covid_19_confirmed["confirmed"].max()
fig = px.bar(covid_19_confirmed,
             x="confirmed", y="country", color="country", 
             animation_frame="reported_on", animation_group="country",
             range_x=[0, max_confirmed])
fig.update_yaxes(categoryorder="total ascending")
confirmed_raceplot = barplot(covid_19_confirmed, item_column="country", value_column="confirmed",
                             time_column="reported_on")
fig = confirmed_raceplot.plot(item_label = "Confirmed by country", value_label="Number of cases",
                              frame_duration=50)

max_deaths = covid_19_deaths["deaths"].max()
fig = px.bar(covid_19_deaths,
             x="deaths", y="country", color="country", 
             animation_frame="reported_on", animation_group="country",
             range_x=[0, max_deaths])
fig.update_yaxes(categoryorder="total ascending")
deaths_raceplot = barplot(covid_19_deaths, item_column="country", value_column="deaths",
                             time_column="reported_on")
fig = deaths_raceplot.plot(item_label = "deaths by country", value_label="Number of cases",
                              frame_duration=50)

max_doses = covid_19_doses['doses_administered'].max() * 1.5
fig = px.bar(covid_19_doses,
             x='doses_administered',y='country',color='country',
             animation_frame='reported_on',animation_group='country',range_x=[0,3000000000])
fig.update_yaxes(categoryorder="total ascending")
doses_raceplot = barplot(covid_19_doses,item_column='country',value_column='doses_administered',time_column='reported_on')
fig = doses_raceplot.plot(item_label='doses by country',value_label='number of cases',
                          frame_duration=50)
fig.write_html("bar_chart_race_doses.html")