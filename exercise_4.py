import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import bootcamp_utils as buts
sns.set()

df_1973 = pd.read_csv('data/grant_1973.csv',comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv',comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')
df_1973 = df_1973.rename(columns={'yearband':'year'})
df_1973['year'] = 1973
df_1975['year'] = 1975
df_1987['year'] = 1987
df_1991['year'] = 1991
df_2012['year'] = 2012

df_1973 = df_1973.rename(columns={'beak length':'beak length (mm)',
                                  'beak depth':'beak depth (mm)'})
df_1975 = df_1975.rename(columns={'Beak length, mm':'beak length (mm)',
                                  'Beak depth, mm':'beak depth (mm)'})
df_1987 = df_1987.rename(columns={'Beak length, mm':'beak length (mm)',
                                  'Beak depth, mm':'beak depth (mm)'})
df_1991 = df_1991.rename(columns={'blength':'beak length (mm)',
                                  'bdepth':'beak depth (mm)'})
df_2012 = df_2012.rename(columns={'blength':'beak length (mm)',
                                  'bdepth':'beak depth (mm)'})
# Concatenate dataframes
df_concat = pd.concat([df_1973, df_1975, df_1987, df_1991, df_2012],
            ignore_index=True)

# Remove duplicates
df_concat_duprem = df_concat.drop_duplicates(subset={'band','species','year'})

# Slice fortis and scandens 1987 beak depths, generate ecdf, and plot
fortis_1987 = df_concat_duprem[(df_concat_duprem['year']==1987)
                          & (df_concat_duprem['species']==('fortis'))]
fortis_x, fortis_ecdf = buts.ecdf(fortis_1987['beak depth (mm)'])

scandens_1987 = df_concat_duprem[(df_concat_duprem['year']==1987)
                          & (df_concat_duprem['species']==('scandens'))]
scandens_x, scandens_ecdf = buts.ecdf(scandens_1987['beak depth (mm)'])

plt.plot(fortis_x, fortis_ecdf, marker='.',linestyle='none')
plt.plot(scandens_x, scandens_ecdf, marker='.', linestyle='none')
plt.xlabel('ECDF')
plt.legend(['Fortis 1987 beak depth', 'Scandens 1987 beak depth'], loc = 'lower right')
plt.show()

# Slice fortis and scandens 1987 beak depths, generate ecdf, and plot
fortis_1987 = df_concat_duprem[(df_concat_duprem['year']==1987)
                          & (df_concat_duprem['species']==('fortis'))]
fortis_x, fortis_ecdf = buts.ecdf(fortis_1987['beak length (mm)'])

scandens_1987 = df_concat_duprem[(df_concat_duprem['year']==1987)
                          & (df_concat_duprem['species']==('scandens'))]
scandens_x, scandens_ecdf = buts.ecdf(scandens_1987['beak length (mm)'])

plt.plot(fortis_x, fortis_ecdf, marker='.',linestyle='none')
plt.plot(scandens_x, scandens_ecdf, marker='.', linestyle='none')
plt.xlabel('ECDF')
plt.legend(['Fortis 1987 beak length', 'Scandens 1987 beak length'], loc = 'lower right')
plt.show()

# Plot beak depth vs. beak length

plt.plot(fortis_1987['beak depth (mm)'], fortis_1987['beak length (mm)'],marker='.', linestyle='none')
plt.plot(scandens_1987['beak depth (mm)'], scandens_1987['beak length (mm)'], marker='.',linestyle='none')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.legend(['Fortis 1987','Scandens 1987'])
plt.show()
