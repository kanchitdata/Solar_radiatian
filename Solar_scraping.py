import pandas as pd

url = "https://suvpm.sc.su.ac.th/realtimesolar"

dfs = pd.read_html(url)
dfs_main = pd.DataFrame(dfs[0])

# "Solar Radiation"
# "UV Index"
# "Relative humidity"
# "Temperature"

sr = float(dfs_main.iloc[0, 1])
uv_id = float(dfs_main.iloc[1,1])
rhu = float(dfs_main.iloc[2,1])
tem = float(dfs_main.iloc[3, 1])

creation_table = str(dfs[1][0])
creation_table_split = creation_table.split()

date = creation_table_split[4]
time = creation_table_split[5]

# Solar_df = pd.DataFrame(columns=["Solar Radiation", "UV Index", "Relative humidity", "Temperature", "Data", "Time"])

Solar_df = pd.read_csv("main_Solar_df.csv")
Solar_data = pd.Series([sr, uv_id, rhu, tem, date, time],
                       index=["Solar Radiation", "UV Index", "Relative humidity", "Temperature", "Data", "Time"])

Solar_df = pd.concat([Solar_df, Solar_data.to_frame().T], ignore_index=True)

Solar_df.to_csv("main_Solar_df.csv", index=False)

