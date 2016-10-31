weights = [] #list of points by weight

for i in range(len(fracs_df)): #for each row in the fractional dataframe
    for j in range(int(fracs_df['n'][i])): #reproduce the points n times in a new dataframe
        weights.append([fracs_df['zhvi'][i],fracs_df[1][i],fracs_df[2][i],fracs_df[3][i],fracs_df[4][i],fracs_df[5][i]])
        
w_df = pd.DataFrame(weights) #convert back into a dataframe
w_df.rename(columns = {0: 'zhvi'}, inplace = True) #rename column 0 to zhvi

plt.scatter(w_df['zhvi'], w_df[1])

zhvi_bin_centers = np.linspace(0,1000000,101)
bin_eps = 30000

star = 5
rolling = []

for bc in zhvi_bin_centers:
    inbin = w_df[(w_df['zhvi'] < (bc + bin_eps)) & (w_df['zhvi'] > (bc - bin_eps))]
    
    if len(inbin) > 0:
        rolling.append((int(bc), np.mean(inbin[star])))
        
r_df = pd.DataFrame(rolling) #rolling average dataframe
ts = np.mean(abs(r_df[1] - np.mean(r_df[1]))) #area test statistic 

plt.scatter(r_df[0],r_df[1])
#plt.xlim(0,600000)
plt.axhline(np.mean(r_df[1]), lw = 1, c = 'grey')
sns.despine()