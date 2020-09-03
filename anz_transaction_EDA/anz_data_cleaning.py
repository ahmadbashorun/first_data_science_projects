import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

nan_value = ["missing", "Missing", "MISSING", "NA","Na", "-", "None"]
df = pd.read_csv(r"C:\Users\user\Documents\Books\Tech resources\DS and ML\ML via DS course\Project 1\ANZ dataset.csv", na_values= nan_value)

#Inspecting data and dealing with empty values
anz_df = df.copy()
anz_df.columns
anz_df.isnull().sum()

anz_df.dropna(axis = "columns", how = "all", inplace=True)
anz_df.dropna(axis = "index", how = "all", inplace=True)
anz_df.drop(["bpay_biller_code"], axis=1, inplace=True)
(len(anz_df.columns))
anz_df["merchant_code"].value_counts(dropna=False)

anz_df["merchant_code"] = (anz_df["merchant_code"].replace(0, np.nan))
anz_df.dropna(axis="columns", how="all", inplace=True)



# working with datetimes
(anz_df['date'])
anz_df['date'] = pd.to_datetime(anz_df['date']) 
anz_df['date'] = pd.to_datetime(anz_df['date'])

anz_df.loc[1, "date"].day_name()

anz_df["date"] = df["date"]
anz_df['date'] = pd.to_datetime(anz_df['date']) 
anz_df["day_name"] = anz_df["date"].dt.day_name()
anz_df["month_name"] = anz_df["date"].dt.month_name()
anz_df['week_number_of_year'] = anz_df['date'].dt.week

anz_df['week_number_of_year'] = ['week' + " "] + anz_df['week_number_of_year'].astype(str)

#viewing the timespan of the data
anz_df["date"].max() - anz_df["date"].min()

#Analysis of transactions by month
aug_df = anz_df[anz_df["month_name"] == "August"]
sept_df = anz_df[anz_df["month_name"] == "September"]
oct_df = anz_df[anz_df["month_name"] == "October"]

#sum of monthly and weekly transactions
monthly_amount=anz_df.groupby(['month_name'])['amount'].agg(['sum'])
m_amount=monthly_amount.sort_values(by='sum',ascending=False)
#print(m_amount)
# October has the highest amount of transactions followed by August then September.

weekly_amount = anz_df.groupby(["week_number_of_year"])[["amount","month_name"]].agg(
    {"amount":"sum", "month_name": "max"})
w_amount=weekly_amount.sort_values("amount",ascending=False)
# week 42 in october has the highest amount 

summary_df = anz_df.groupby(["month_name"]).describe()

# frequecy of specific transactions
anz_df["txn_description"].value_counts(dropna=False)
aug_df["txn_description"].value_counts(dropna=False)
sept_df["txn_description"].value_counts(dropna=False)
oct_df["txn_description"].value_counts(dropna=False)

# average monthly and weekly transaction amount
avg_amount = anz_df.groupby(["month_name"])[["amount", "balance"]].agg({"amount": "mean", "balance": "mean"}) 
avg_monthly = avg_amount.sort_values(by="amount", ascending = False)
#Customers made about 196 transactions on average in October
#then 185 and 182 in August and September respectively

avg_week_amount = anz_df.groupby(["week_number_of_year"])[["amount","month_name", "balance"]].agg(
    {"amount":"mean", "month_name": "max", "balance":"mean"})
avg_amount=avg_week_amount.sort_values("amount",ascending=False)


# analysis of the customers
cust = anz_df['first_name'].value_counts()
freq_cust = cust.sort_values().nlargest(10)
cust_df = pd.DataFrame({"Name":["Micheal", "Diana", "Jessica", "Joseph", "Jeffrey","Richard","Kimberly",
                        'Tonya', "Susan", "Christopher" ],
                        "No_of_txn":[746,578,408,391,388,364,343,292,282,263] })
#cust_df shows the ten most valuable customers based on number of transactions

#VISUALIZATIONS
#sns.set_style("whitegrid")
#sum_month_plot = sns.barplot(x="month_name", y= "amount", data=anz_df, palette="husl",
#                             estimator = sum, hue="week_number_of_year")
#sum_month_plot.set_title("TOTAL TRANSACTION VALUE PER MONTH")
#sum_month_plot.set_xlabel("Month")
#sum_month_plot.set_ylabel("Amount")


#avg_month_plot = sns.barplot(x="month_name", y= "amount", data=anz_df, palette='rainbow', 
#            estimator = np.mean)
#avg_month_plot.set_title("AVERAGE TRANSACTION VALUE PER MONTH")
#avg_month_plot.set_xlabel("Month")
#avg_month_plot.set_ylabel("Amount")


#hp = anz_df.pivot_table(index="merchant_state", columns= "month_name", values="amount")
#corr = anz_df.corr()
#city_heatmap = sns.heatmap(hp, cmap="YlOrRd")
#city_heatmap.set_title("SUMMARY OF TRANSACTION PER CITY")
#city_heatmap.set_xlabel("Month")
#city_heatmap.set_ylabel("State")


#age_count=sns.countplot(x="age", data=anz_df, palette="rainbow")
#age_count.set_title("AGE COUNT")

#gender_count = sns.countplot(anz_df["gender"], palette="Set2")
#gender_count.set_title("GENDER COUNT")

#state_count = sns.countplot(y="merchant_state" ,data=anz_df, palette=("inferno"))
#state_count.set_title("CITY COUNT")
#state_count.set_ylabel("State")

#plt.figure(figsize=(8,4))
#txn_desc_count = sns.countplot(anz_df["txn_description"], palette="Set3",  )
#txn_desc_count.set_title("FREQUENCY OF TRANSACTION TYPES")
#txn_desc_count.set_xlabel('Transaction description')

sns.set_style("darkgrid")
week32_df = anz_df[anz_df["week_number_of_year"]== "week 32"]

#random_week= sns.barplot(x="day_name",y="amount", data=week32_df, palette="pastel")
#random_week.set_title("Transaction Volume in an average week.")
#random_week.set_xlabel('Day')
#random_week.set_ylabel("Amount")

#plt.figure(figsize=(10,5))
#cust_plot = sns.barplot(y="Name", x="No_of_txn", data=cust_df, palette="viridis")
#cust_plot.set_title("Customers With Highest Number of Transactions")
#cust_plot.set_xlabel("Number of transactions")
















