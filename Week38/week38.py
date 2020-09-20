import numpy as np

filename = '..\\..\\data\\befkbhalderstatkode.csv'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

year_mask = (bef_stats_df[:,0] == 2015)
all_people_dict = {}
#all_people_list = []
for area in neighb:
    all_people_in_area = bef_stats_df[year_mask & (bef_stats_df[:,1] == area)]
    sum_of_people = all_people_in_area[:,4].sum()
    #all_people_list.append(sum_of_people)
    
    all_people_dict[neighb[area]] = sum_of_people
    print(neighb[area] + ': ' + str(sum_of_people))
    
print(all_people_dict)
#all_people_array = np.array(all_people_list)

neighb[1]