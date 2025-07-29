import numpy as np
import pandas as pd
pd.set_option("display.max_columns",None)
df=pd.read_csv("C:\\Users\\Karthik\\OneDrive\\Desktop\\googleplaystore.csv")
print(df)
print("==================================================================")
# 1.Find the total number of Apps in Google Play Store
print("1.Total Number of Apps in Google Play Store=\n",df.shape[0])
print("==================================================================")
# 2.Find the Total Number of Columns in each  of App of Google Play Store
print("2.Total Number of Columns in each of App of google Play Store=\n",df.shape[1])
print("==================================================================")
# 3.Display Top 3 Rows of the Dataset(Default it displays 5 rows)
print("3.Top 3 Rows=>\n",df.head(3))
print("==================================================================")
# 4.Display Last 3 Rows of the Dataset
print("4.Last 3 Rows=>\n",df.tail(3))
print("==================================================================")
# 5.Find the shape of the Dataset
print("5.Shape of the Dataset\n",df.shape)
print("===================================================================")
# 6.Get the information about our Dataset
print("6.Information about our Dataset like no.of cols,no.of rows,memory reg=>\n")
df.info()
print("===================================================================")
# 7.Get the statistical information about Google Play Store
print("7.The Statistical (or) Descriptive information about Google Play Store\n",df.describe())
# It gives Statistical (or) Descriptive information of all columns
print("The Statistical (or) Descriptive information about Google Play Store\n",df.describe(include="all"))
print("==================================================================")
# 8.How many total number of apps titles contains "Astrology"
astrology=df[df["App"].str.contains("Astrology")]["App"]
print("8.Total number of app titles contains Astrology= \n",astrology)
print("Total Number of Apps=",len(astrology)) # no.of apps
print("===================================================================")
# 9.Average App Rating of Google Play Store
avg=df["Rating"].mean()
print("9.The Average App Rating of Google Play Store=\n",round(avg,1))
print("===================================================================")
# 10.Find the total number of Unique Category
uni=df["Category"].nunique()
print("10.The total number of Unique Category=\n",uni)
# Display the category names of the dataset
for catnames in df["Category"].unique():
    print(catnames)
print("===================================================================")
# 11.Which Category has the Highest Average Rating from top
hig_rating=df.groupby("Category")["Rating"].mean().sort_values(ascending=False).head(5)
print("11.The Category which has the Highest Average Rating from Top \n",hig_rating)
print("----------------------------------------------------------------------")
# . Which Category has the Highest Average Rating from bottom
hig_rating=df.groupby("Category")["Rating"].mean().sort_values(ascending=False).tail(5)
print("The Category which has the Highest Average Rating from Bottom\n",hig_rating)
print("======================================================================")
# 12.Find the Total number of App having 5 star Rating Apps
star5apps=len(df[df["Rating"]==5])
print("12.The total number of Apps having 5 star Rating \n",star5apps)
print("----------------------------------------------------------------------")
# .Display the Apps having 5 star Rating
for star5 in df[df["Rating"]==5].iterrows():
    print(star5)
print("======================================================================")
# 13.Find the Average values of Reviews
df["Reviews"]=df["Reviews"].replace("3.0M",3.0*1000000)
review=df["Reviews"]=df["Reviews"].astype("float")
mv=df["Reviews"].mean()
print("13.The average values of Reviews=\n",mv)
print("======================================================================")
# 14.Find the total number of FREE and PAID apps
apps=df["Type"].value_counts()
print("14.The total number of FREE and PAID apps in Dataset\n ",apps)
print("======================================================================")
# 15.Find out which app has Maximum Review
appname=df[df["Reviews"].max()==df["Reviews"]]["App"]
print("15.The App which has Maximum Review:\n",appname)
print("========================================================================")
# 16.Display top 5 Apps having Highest Reviews.
app5=df["Reviews"].sort_values(ascending=False).head().index
indices=df["Reviews"].sort_values(ascending=False).head().index
App5=df.iloc[indices]["App"]
print("16.Top 5 Apps having Highest Reviews:\n",App5)
print("===========================================================================")
# 17.Find the Average Rating of Free and Paid Apps.
feendpaid_avg=df.groupby("Type")["Rating"].mean()
print("17.Average Rating for Free and Paid Apps:\n",feendpaid_avg)
print("==============================================================================")
# 18.Display all the Paid Apps from Google Play Store.
paid_apps=df[df["Type"]=="Paid"]
paid_app_names=paid_apps["App"]
print("18. The Paid Apps in Google Play Store: \n",paid_app_names)
print("========================================================================")
#  19.Display top and bottom music apps
music=df[df["Genres"]=="Music"].tail(3)
music_app=df[df["Genres"]=="Music"].head(3)
print("19.The Bottom 3 Music Apps:\n",music)
print("------------------------------------------------------------------------")
print("The Top 3 Music Apps:\n",music_app)
print("==========================================================================")
# 20.Display the Statistical info about  Music apps
app=df[df["Genres"]=="Music"].describe()
print("20.The Statistical info about Music App:\n",app)
print("===================================================================================")
# 21.Finding the Apps with Maximum Size in Google Play Store.
apps_max_size=df[["App","Size"]].head(10)
print("21.Apps with Maximum Size in Google Play Store:\n",apps_max_size)
print("==========================================================================")
# 22.Displaying all the apps in the Education Category with a rating above 4.5.
eduaction_apps=df[(df["Genres"]=="Education")& (df["Rating"]>4.5)]
education=eduaction_apps[["App","Rating"]]
print("22.The education apps having more than 4.5 Rating\n",education)
print("===========================================================================")
# 23.Finding the number of apps in each Category of Google Play Store.
category_counts=df["Category"].value_counts()
print("23.Counting the number of Apps in each Category:\n",category_counts)
print("===========================================================================")
# 24.Finding the Most Expensive Paid app in Google Play Store.
most_expensive_app=df[df["Type"]=="Paid"].sort_values(by="Price",ascending=False).head(1)
app1=most_expensive_app[["App","Price"]]
print("24.The Most Expensive App in Google Play store:\n",app1)
print("==============================================================================")
# 25.Grouping the apps by category and finding the average rating for each app of Google Play Store.
category_avg_rating=df.groupby("Category")["Rating"].mean().sort_values(ascending=False)
print("25.The average rating of each App in Google Play Store:\n",category_avg_rating)
print("==========================================================================================")
print(" **************************** THE END ******************************")