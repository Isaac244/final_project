import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

##DIAGRAMA PARA VER COVID EN LATAM
def covid_times_series(df : pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

##LISTA DE LOS PAISES CON COVID
def top_countries_df_list(df, countries, n):
    global n_top
    n_top = n
    top_countries_df = (
        df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(20)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in countries else "lightblue",
            dest_column_name="color"
        )
    )
    return top_countries_df.head(n_top)



##GRAFICA DE LOS PAISES A VER
def global_bar_latam(df_country : pd.DataFrame):
    sns.barplot(
        data=df_country,
        x="value",
        y="country_region",
        palette=df_country.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");