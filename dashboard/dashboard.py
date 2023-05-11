import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from pathlib import Path

def create_season_df(df):
    byseason_df = day_df.groupby(by="season").agg({"cnt": "sum"}).reset_index()
    byseason_df.rename(columns={"cnt": "total_users"}, inplace=True)

    return byseason_df

def create_yr_df(df):
    byyr_df = day_df.groupby(by="yr").agg({"cnt": "sum"}).reset_index()

    return byyr_df

def create_holiday_df(df):
    byholiday_df = df.groupby(by="holiday").agg({"cnt": "sum"}).reset_index()
    byholiday_df.rename(columns={"cnt": "sum"}, inplace=True)
    byholiday_df["holiday"].replace({0: "Not a Holiday", 1: "Holiday"}, inplace=True)
    return byholiday_df


def create_weathersit_df(df):
    byweathersit_df = df.groupby(by="weathersit").instant.nunique().reset_index()
    byweathersit_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byweathersit_df


def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:
        st.image("https://github.com/hairulysin/dicoding_DA/blob/main/bikesharing.png")
        

        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Rentang Waktu", 
            min_value=min_date, 
            max_value=max_date,
            value=[min_date, max_date],
            on_change=on_change
        )

    return date

def season(df):
    st.subheader("Season")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.lineplot(
        x="season",
        y="total_users",
        data=df.sort_values(by="season", ascending=False),
        sort=False
    )

    ax.set_title("Analisis Tren Penggunaan Sepeda dalam Setiap Musi", loc="center", fontsize=15)
    ax.set_xlabel("Season")
    ax.set_ylabel("Number of Bike Sharing Users")
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def year(df):
    st.subheader("Year")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=df.sort_values(by="yr", ascending=False), x="yr", y="cnt")
    ax.set_title("Total Bike Sharing Users by Year", loc="center", fontsize=15)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Users")
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def holiday(df):
    st.subheader("Holiday")

    # Mengatur warna
    colors = ["#FFA07A", "#87CEFA"]

    # Membuat pie chart
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        df["sum"],
        labels=df["holiday"],
        colors=colors,
        startangle=90,
        autopct="%1.1f%%",
        textprops={
            "fontsize": 14,
            "fontweight": "bold",
        },
        wedgeprops={
            "linewidth": 1.5,
            "edgecolor": "white",
        },
        radius=0.75,
        pctdistance=0.5,
    )

    # Membuat donut chart
    centre_circle = plt.Circle(
        (0, 0),
        0.5,
        color="white",
        edgecolor="black",
        linewidth=1.5,
        fill=False,
    )

    # Menambahkan lingkaran ke dalam pie chart
    fig.gca().add_artist(centre_circle)

    # Menambahkan judul dan keterangan sumbu
    ax.set_title("Proportion of Bike Sharing Users on Holiday vs. Non-Holiday", fontsize=14, fontweight="bold", pad=20)
    ax.legend(title="", loc="best", fontsize=12)

    # Menampilkan gambar
    st.pyplot(fig)


def weathersit(df):
    st.subheader("Weather Sit")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.pie(
        df["sum"],
        labels=df["weathersit"],
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Percentage of Bike Sharing Users by Weather Condition", fontsize=15)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)



if __name__ == "__main__":
    sns.set(style="dark")

    st.header("Bike Sharing Dashboard :bike:")

    day_df_csv = Path(__file__).parents[1] / 'dashboard/clean_data.csv'

    day_df = pd.read_csv(day_df_csv)

    date = sidebar(day_df)
    if(len(date) == 2):
        main_df = day_df[(day_df["dteday"] >= str(date[0])) & (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[(day_df["dteday"] >= str(st.session_state.date[0])) & (day_df["dteday"] <= str(st.session_state.date[1]))]

    season_df = create_season_df(main_df)
    season(season_df)
    
    year_df = create_yr_df(main_df)
    year(year_df)
    
    holiday_df = create_holiday_df(main_df)
    holiday(holiday_df)
    
    weathersit_df = create_weathersit_df(main_df)
    weathersit(weathersit_df)
    

    year_copyright = datetime.date.today().year
    copyright = "Copyright © " + str(year_copyright) + " | Bike Sharing Dashboard | All Rights Reserved | " + "Made with :heart: by [@hairulysinn](https://www.linkedin.com/in/hairulyasin/)"
    st.caption(copyright)