from pandas import read_excel
import os
df1 = read_excel("bases/Athletes.xlsx")
df2 = read_excel("bases/Coaches.xlsx")
df3 = read_excel("bases/EntriesGender.xlsx")
df4 = read_excel("bases/Medals.xlsx")
df5 = read_excel("bases/Teams.xlsx")
os.system("clear")

def proxima():
    input()
    os.system("clear")

print(df1)
proxima()
print(df2)
proxima()
print(df3)
proxima()
print(df4)
proxima()
print(df5)

