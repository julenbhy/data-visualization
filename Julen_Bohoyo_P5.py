import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import json



# Cargar la capa temática
natalidad = "nuevos_casos_de_cancer_por_cada_100.000_personas_por_comunidades_autonomas.json"
map_data = gpd.read_file(natalidad)
map_data.head()

'''

fig = plt.figure(figsize=(15, 10))
fig.suptitle('CANCER DATA REPRESENTATION (Data source: GLOBOCAN 2020)', fontsize=16)

# Multiple bar plot
type = ['Breast', 'Prostate', 'Lung', 'Colorrectum', 'Cervix uteri', 'Stomach', 'Liver', 'Corpus uteri', 'Ovary', 'Thyroid']
incidence = [47.8, 30.7, 22.4, 19.5, 13.3, 11.1, 9.5, 8.7, 6.6, 6.6]
mortality = [13.6, 7.7, 18.0, 9.0, 7.3, 7.7, 8.7, 1.8, 4.2, 0.43]

ax = fig.add_subplot(221)
x = np.arange(len(type))  # labels to numbers
width = 0.35  # the width of the bars
rects1 = ax.bar(x - width/2, incidence, width, label='Incidence')
rects2 = ax.bar(x + width/2, mortality, width, label='Mortality')

ax.set_title('Estimated number of incident cases and deaths worldwide, both sexes, all ages', pad=30)
ax.set_ylabel('ASR (World) per 100 000')
ax.set_xlabel("Cancer type")
ax.set_xticks(x, type, rotation='vertical') #numbres to labels
ax.legend()
#ax.bar_label(rects1, padding=3) # number of each bar
#ax.bar_label(rects2, padding=3)



# Piechart
ax = fig.add_subplot(222)
type = ['Breast', 'Lung', 'Colorrectum', 'Prostate', 'Stomach', 'Liver', 'Cervix uteri', 'Other']
new_cases = [11.7, 11.4, 10.0, 7.3, 5.6, 4.7, 3.1, 46.0]
ax.pie(new_cases, labels=type, radius=1.3, autopct='%1.0f%%', pctdistance=0.6, labeldistance=1.1)
ax.set_title('Incidence of Lung and Bronchus caner worldwide by years, both sexes, all ages', pad=30)



# Scatterplot
ax = fig.add_subplot(223)
years = range(1975, 2019)
incidence = [52.2, 55.4, 56.7, 57.8, 58.6, 60.6, 62.0, 63.3, 63.5, 65.5, 64.6, 65.8, 67.9, 68.1, 67.6, 68.1, 69.2, 69.5, 67.8, 67.2, 66.8, 66.5, 66.6, 67.5, 65.8, 64.1, 64.2, 64.0, 64.8, 62.2, 63.0, 62.3, 62.1, 60.4, 60.0, 57.7, 56.3, 55.3, 54.1, 53.3, 52.0, 51.4, 50.1, 46.9]
ax.scatter(years, incidence, marker='.')

ax.set_title('Incidence of Lung and Bronchus caner worldwide by years, both sexes, all ages', pad=30)
ax.set_ylabel('ASR (World) per 100 000')
ax.set_xlabel("Year")
ax.grid()



#fig.tight_layout(pad=4.0)
fig.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.85, wspace=0.6, hspace=1)
plt.show()
'''
