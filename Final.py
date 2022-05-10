"""
Class: CS230--Section 004
Name: Samantha van Gestel
Description: (Final Project)
I pledge that I have completed the programming assignment independently. 
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px


def get_data():
    df = pd.read_csv("UFO Sightings.csv",
                     header=0,
                     names=['Datetime', 'City', 'State', 'Country', 'Shape', 'Duration(sec)', 'Duration(min)',
                            'comments', 'date posted', 'latitude', 'longitude'])
    return df


def filter_country(df, country_choices):
    if not country_choices:
        df_country_filter = df
    else:
        df_country_filter = df[df["Country"].isin(country_choices)]
    return df_country_filter


def filter_date(df, dates):
    if not dates:
        df_date_filter = df
    else:
        df_date_filter = df[df["Datetime"].isin(dates)]
    return df_date_filter


def line_chart():
    df = get_data()
    st.header("Line Chart: UFO Sightings per year")
    years = []
    for d in df["Datetime"]:
        if len(d) == 16:
            years.append(d[6:10])
        elif len(d) == 15:
            years.append(d[5:9])
        elif len(d) == 14:
            years.append(d[4:8])
    fifties_counter = 0
    sixties_counter = 0
    seventies_counter = 0
    eighties_counter = 0
    nineties_counter = 0
    two_thousands_counter = 0
    twenty_ten_counter = 0
    for y in years:
        if y == "1950":
            fifties_counter += 1
        elif y == "1960":
            sixties_counter += 1
        elif y == "1970":
            seventies_counter += 1
        elif y == "1980":
            eighties_counter += 1
        elif y == "1990":
            nineties_counter += 1
        elif y == "2000":
            two_thousands_counter += 1
        elif y == "2010":
            twenty_ten_counter += 1
    data = [fifties_counter, sixties_counter, seventies_counter, eighties_counter, nineties_counter,
            two_thousands_counter, twenty_ten_counter]
    year = ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
    plt.plot(year, data, color='Green')
    plt.xlabel('Decades')
    plt.ylabel('Frequency')
    st.pyplot(plt, clear_figure=True)


def bar_chart():
    df = get_data()
    st.header("Bar Chart: Duration of Sightings")
    seconds = []
    for d in df["Duration(sec)"]:
        seconds.append(float(d))
    first_range = 0
    second_range = 0
    third_range = 0
    fourth_range = 0
    fifth_range = 0
    sixth_range = 0
    seventh_range = 0
    eighth_range = 0
    ninth_range = 0
    tenth_range = 0
    for s in seconds:
        if s <= 60:
            first_range += 1
        elif s <= 120:
            second_range += 1
        elif s <= 180:
            third_range += 1
        elif s <= 240:
            fourth_range += 1
        elif s <= 300:
            fifth_range += 1
        elif s <= 360:
            sixth_range += 1
        elif s <= 420:
            seventh_range += 1
        elif s <= 480:
            eighth_range += 1
        elif s <= 540:
            ninth_range += 1
        else:
            tenth_range += 1
    data = [first_range, second_range, third_range, fourth_range, fifth_range, sixth_range,
            seventh_range, eighth_range, ninth_range, tenth_range]
    year = ("0-60s", "060-120s", "120-180s", "180-240s", "240-300s", "300-360s", "360-420s", "420-480s", "480-540s", "540s+")
    plt.bar(year, data, color='Purple')
    plt.xlabel('Duration')
    plt.gcf().autofmt_xdate()
    plt.ylabel('Frequency')
    plt.subplots_adjust()
    st.pyplot(plt, clear_figure=True)


def pie_chart():
    st.header("Pie Chart: Different Shapes of the Sightings")
    df = get_data()
    shape_options = ['cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball', 'oval', 'rectangle', 'other']
    cylinder_counter = 0
    light_counter = 0
    circle_counter = 0
    sphere_counter = 0
    disk_counter = 0
    fireball_counter = 0
    oval_counter = 0
    rectangle_counter = 0
    other_counter = 0
    for d in df["Shape"]:
        if d == 'cylinder':
            cylinder_counter += 1
        elif d == 'light':
            light_counter += 1
        elif d == 'circle':
            circle_counter += 1
        elif d == 'sphere':
            sphere_counter += 1
        elif d == 'disk':
            disk_counter += 1
        elif d == 'fireball':
            fireball_counter += 1
        elif d == 'oval':
            oval_counter += 1
        elif d == 'rectangle':
            rectangle_counter += 1
        else:
            other_counter += 1
    data = [cylinder_counter, light_counter, circle_counter, sphere_counter,
            disk_counter, fireball_counter, oval_counter, rectangle_counter, other_counter]
    fig = px.pie(values=data, names=shape_options, title='Described Shapes of UFO Sightings', color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig)


def page0():
    col1, col2, col3 = st.columns([2, 2, 2])
    col2.image("alien.jpg", use_column_width=True)
    st.title("UFO Sightings")
    st.header("Samantha van Gestel - Final Project")
    st.write("Hello everyone and welcome to my final project! I chose the data set about UFO sightings and "
             "have created maps, charts, and a timeline to show you all of the information on the different "
             "reported sightings. Please select a button on the left to go to a new page displaying the different "
             "data tools.")


def page1():
    st.title("Map of UFO Sightings")
    df = get_data()
    col1, buffer, col2 = st.columns([9, 1, 20])
    countries = []
    for c in df["Country"]:
        if c not in countries:
            countries.append(c)
    with col1:
        st.header("Filter by Country")
        country_choices = st.multiselect("Select a country", countries)

    with col2:
        st.header("Map of UFO Sightings")
        df_country_filter = filter_country(df, country_choices)
        df2 = pd.DataFrame(df_country_filter[["latitude", "longitude"]])
        df2 = df2.apply(pd.to_numeric, errors='coerce')
        df2 = df2.dropna()
        st.map(df2)


def page2():
    st.title("Have you seen a UFO?")
    line_chart()
    st.write("As time goes on, more and more people are reporting UFO sightings.")
    bar_chart()
    st.write("A majority of the UFO Sightings are really quick or much longer.")
    pie_chart()
    st.write("A lot of the sightings are described as having an unknown (other) shape.")


def page3():
    st.title("Timeline of UFO Sightings")
    df = get_data()
    date = []
    for c in df["Datetime"]:
        date.append(c)
    date = list(set(date))
    st.header("Filter by Date")
    dates = st.multiselect("Select a date", date)
    st.header("Description of UFO Sightings")
    df_date_filter = filter_date(df, dates)
    df2 = pd.DataFrame(df_date_filter[["Datetime", "comments", "City", "Country"]])
    st.write(df2)


def main():
    st.sidebar.title("Page Options")
    selection = st.sidebar.radio("Please select a page to explore!", ["Home", "Map", "Charts", "Timeline"])
    if selection == "Home":
        page0()
    if selection == "Map":
        page1()
    if selection == "Charts":
        page2()
    if selection == "Timeline":
        page3()


main()
