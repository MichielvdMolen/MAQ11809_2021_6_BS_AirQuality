from IPython.display import Image

import os
teacher_dir  = os.getenv('TEACHER_DIR')
imgpath = teacher_dir + '/JHL_data/pictures/'

def check_my_answer_AQ1_1(x, y):
    dy = 1
    if x == 'Vredepeel' and 21.02 - dy <= y <= 21.02 + dy:
        print('Hoera! Your answer is correct! Today, we will go to an adventure!')
        print('\033[1m' + 'Feedback:' + '\033[0m','According to the table above, station Vredepeel has the highest mean NH\u2083 concentration. This happens because Vredepeel is situated in area where many livestock farms emit a lot of nitrogen. Around the Veluwe national park where station Wekerom is situated, are also animal farms like chickens. But the amount of nitrogen they emit is lower compared to Vredepeel. Zegveld is closer to the coast. Area is highly ventialated due to persistant winds, thus, lower concentrations are present.')
        display(Image(filename= imgpath + "ship1.png", width=200, height=200))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x != 'Vredepeel'              : print('x  is incorrect')
        if y < 21.02-dy or y > 21.02 + dy: print('y  is incorrect')
        return False
    
    
def check_my_answer_AQ1_2(x):
    if x == ('a','b','c'):
        print('Hoera! Your answer is correct! Where do you think we will go from here?')
        print('\033[1m' + 'Feedback:' + '\033[0m','Some of the reasons for the differences seen in table under Question 1.1 are the wind speed, wind direction and changes in emission. Changing wind speed and direction can severely decrease amount of nitrogen present at an area. Zegveld, that is situated close to the coast for that reason has the lowest mean ammonia concetration. Additionally, animal farms are a major source of nitrogen. Pig farms are higher source of ammonia compared to chicken farms.')
        display(Image(filename= imgpath + "stars.png", width=500, height=500))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if 'a' in x               : print('a is correct')
        if 'b' in x               : print('b is correct')
        if 'c' in x               : print('c is correct')
        return False
    
def check_my_answer_AQ2a_1(x, y, z):
    dy = 10
    if x == 'Vredepeel' and 70-dy <= y <= 70+dy and z == ('b','c'):
        print('Hoera! Your answer is correct! Any ideas?')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'Vredepeel station has the highest inter-annual variability. This can be seen on the time series where a mean concentration of almost every year exceeds mean concentrations of other two stations. The interannual variability at that station is about 67%. This is about 23% higher than the variability at station Wekerom and Zegveld. The variability is very high at station Wekerom because of its geographical position in Brabant area where a lot of animal, i.e., pig farms emit large amounts of nitrogen. Additionally, station Zegveld, situated near the coast, is affected by the westerly winds that bring clean air and ventilate the area thus lowering the nitrogen concentration.')
        display(Image(filename= imgpath + "milkyway.jpeg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        print('x is incorrect') if x != 'Vredepeel'                else print('x is correct')
        print('y is incorrect') if y<70-dy or y>70+dy              else print('y is correct')
        if 'a' in z                 :      print('a is incorrect')
        if 'b' in z                 :      print('b is correct')
        if 'c' in z                 :      print('c is correct')
        return False
    
def check_my_answer_AQ2b_1(x, y, z1, z2, z3):
    if x == 'Vredepeel' and y == 3 and  12<=z1<=16 and 30<=z2<=40 and 45<=z3<=50:
        print('Hoera! Your answer is correct! Still not?')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'Vredepeel station has the highest seasonal variability. This can be seen on the time series where a mean concentration in every week exceeds mean concentrations of other two stations. There are three dominant peaks observed in the stations\' time series. The first one starts at approximately week 12 (late march) and lasts till week 16. The second one differs per measurement location. In Wekerom and Vredepeel the week is seen in week 30, while in Zegveld in week 36. Farmers are allowed to use manure on the land from about half february, which is why we see the increase in ammonia concentration from week 6-8. Depending on the crop farmers are growing, they are able to use manure on their land a second time sometime in summer. A third peak appears in November (weeks 45-50), just before the end of the legal manure application period, when some farmers apply manure on winter crops.')
        display(Image(filename= imgpath + "earth.jpeg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        print('x  is incorrect') if x != 'Vredepeel'   else print('x  is correct')
        print('y  is incorrect') if y != 3             else print('y  is correct')
        print('z1 is incorrect') if z1 < 12 or z1 > 16 else print('z1 is correct')
        print('z2 is incorrect') if z2 < 30 or z2 > 40 else print('z2 is correct')
        print('z3 is incorrect') if z3 < 45 or z3 > 50 else print('z3 is correct')
        return False   
    
    
def check_my_answer_AQ3_1(x, y, z):
    if x == 'decreases' and y == 'night' and z == 'weaker':
        print('Hoera! Your answer is correct! Look better!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'If we zoom into the figure, we can see that at times when the wind speed increases, the aerodynamical resistence will decrease. Accordingly, at times when the wind speed decreases, the aerodynamical resistance will increase. This can also be inferred from the equation for aerodynamical resistance (see Section 3). Vertical mixing is weaker during the night. It depends on two processes: convection, i.e., an upward (or downward) movement of warm air that occurs as a result of vertical temperature gradients, and turbulent diffusion, a chaotic transport of mass, heat and momentum due to turbulent and random motions. Both processes lead to stronger vertical mixing during the day. Consequently, we can see that the resistance is slightly higher during the night compared to day. This is because there is less vertical mixing as convection and turbulent diffusion are lower in the night. The first because we have a stable atmosphere during the night, and  the latter because there is less friction during the night.')
        display(Image(filename= imgpath + "netherlands.jpeg", width=300, height=300))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        print('x is incorrect') if x != 'decreases' else print('x  is correct')
        print('y is incorrect') if y != 'night'     else print('y  is correct')     
        print('z is incorrect') if z != 'weaker'    else print('z  is correct')
        return False 

def check_my_answer_AQ4_1(x, y, z, u1, u2):
    if x == 'is not' and y == 'lower' and z == 'inversely proportional' and u1 == 'open up' and u2 == 'lower':
        print('Hoera! Your answer is correct! Yes? No?')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'Looking at the figure, we can see that the canopy resistance does not fall in between the minimum and the maximum canopy resistance. The maxumum canopy resistance is not exceded while the minimum is. The canopy resistance is lower during summer compared to winter since the resistance is inversely proportional to global radiation Rg. This can be explained by the fact that photosynthesis is higher when the radiation is higher. For photosysnthesis to work, more CO2 is needed. The stomata will therefore open up more with high radiation, leading to a lower resistance. This effect of radiation can be seen in daily variation (zoom into figure for beter overview). Peaks with higher resistance will likely mean that there was a cloudy day.')
        display(Image(filename= imgpath + "amsterdam.jpeg", width=300, height=300))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        print('x  is incorrect') if x  != 'is not'                  else print('x  is correct')
        print('y  is incorrect') if y  != 'lower'                   else print('y  is correct')
        print('z  is incorrect') if z  != 'inversely proportional'  else print('z  is correct')    
        print('u1 is incorrect') if u1 != 'open up'                 else print('u1 is correct')    
        print('u2 is incorrect') if u2 != 'lower'                   else print('u2 is correct')    
        return False
    
def check_my_answer_AQ5_1(aerodynamic_res, canopy_res, x, y1, y2, z1, z2):
    if aerodynamic_res == 20 and canopy_res == 30 and x == 'negligible' and y1 == 'canopy' and y2 == 'radiation' and z1 == 'night' and z2 == 'high':
        print('Hoera! Your answer is correct! It gets clearer with every correct answer!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'Typical values for the aerodynamical resistance in winter months are between 12 and 120 s/m, while the canopy resistance is about 35 s/m. Boundary layer resistance is about 5 s/m which means that it is negligible compared to the other two resistances. From the figures above, we can see that the canopy resistance has the pronounced diurnal and seasonal variability (see figure under Question 4.1). This happens because the canopy resistance depends on radiation (for additional info see feedback under Question 4.1). Aerodynamical resistance does not have pronounced diurnal cycle. However, it is still "somewhat" present due to changes in vertical mixing between night and day.')
        display(Image(filename= imgpath + "museumplein.jpeg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if aerodynamic_res != 20    :    print('aerodynamic_res is incorrect') 
        if canopy_res      != 30    :    print('canopy_res      is incorrect')
        if x  != 'negligible'       :    print('x  is incorrect')
        if y1 != 'canopy'           :    print('y1 is incorrect')
        if y2 != 'radiation'        :    print('y2 is incorrect')
        if z1 != 'night'            :    print('z1 is incorrect')
        if z2 != 'high'             :    print('z2 is incorrect')
        return False
    
def check_my_answer_AQ6_1(x, y, z1, z2):
    if x == 'Vredepeel' and y == 'F_NH3_Vredepeel.mean()' and z1 == 'higher' and z2 == 'lower': 
        print('Hoera! Your answer is correct! A bit longer!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'The same as the ammonia concentration, we can see that station Vredepeel has the highest nitrogen deposition. If we calculate the mean value using F_NH3_Vredepeel.mean() python code, we obtain the mean deposition flux at Vredepeel station almost 30% higher compared to the deposition at Wekerom station, and about 50% higher compared to deposition at Zegveld station. Looking at the figure for deposition flux, it is obvious that the flux is higher during summer compared to winter. For better view, zoom into the figure.')
        display(Image(filename= imgpath + "rijksmuseum.jpeg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'Vredepeel'        :    print('x  is incorrect')
        if y  != 'F_NH3_Vredepeel.mean()' : print('y  is incorrect')    
        if z1 != 'higher'           :    print('z1 is incorrect')
        if z2 != 'lower'            :    print('z2 is incorrect')
        return False
    
def check_my_answer_AQ7a_1(x, y1, y2):
    if x == 'summer' and y1 == 'high' and y2 == 'open':
        print('Hoera! Your answer is correct! Two more to go!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'We can see that the highest deposition flux is in summer. During this time concentrations are high (see figure under Question 2b.1) and the stomata are open (recting to the global raditaion flux), so these two processes strengthen eachother.')
        display(Image(filename= imgpath + "rijksmuseum1.jpeg", width=350, height=350))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'summer'           :    print('x  is incorrect')
        if y1 != 'high'             :    print('y1 is incorrect')
        if y2 != 'open'             :    print('y2 is incorrect')
        return False  
    
def check_my_answer_AQ7b_1(x, y, z1, z2):
    if x == 'higher' and y == 'night' and z1 == 'night' and z2 == 'canopy resistance':
        print('Hoera! Your answer is correct! And you are almost there to recognise your lecturer!')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'There is something controversial in the hourly variation. We know that ammonia concentrations are higher during the night, which would logically lead to a higher flux (F = deltaC/r). The deposistion flux, however, is close to zero during the night. Apparently, the resistance becomes so big in the night that the effect of high concentration is not important.')
        display(Image(filename= imgpath + "rembrandt.jpeg", width=450, height=450))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if x  != 'higher'           :    print('x  is incorrect')
        if y  != 'night'            :    print('y  is incorrect')
        if z1 != 'night'            :    print('z1 is incorrect')
        if z2 != 'canopy resistance':    print('z2 is incorrect')
        return False 
    
def check_my_answer_AQ7b_2(Wekerom, Vredepeel, Zegveld, x):
    margin = 1000
    if  (2111-margin <=Wekerom<= 2111+margin) and (3136-margin <=Vredepeel<= 3136+margin) and (1311-margin <=Zegveld<= 1311+margin) and x == 'comparable':
        print('Hoera! Your answer is correct! ok, lets take a responsible break :)')
        print('\033[1m' + 'Feedback:' + '\033[0m', 'If you have calculated correctly, you should get that modeled mean concentrations are comparable to the ones seen in Figure 1.')
        display(Image(filename= imgpath + "heineken.jpeg", width=400, height=400))
        return True
    else:
        print('Your answer is not correct. Please, try again!')
        if (Wekerom   < 2111-margin or Wekerom   > 2111+margin): print('F_NH3_2018_Wekerom   is incorrect')
        if (Vredepeel < 3136-margin or Vredepeel > 3136+margin): print('F_NH3_2018_Vredepeel is incorrect')
        if (Zegveld   < 1311-margin or Zegveld   > 1311+margin): print('F_NH3_2018_Zegveld   is incorrect')
        if x != 'comparable': print('x is incorrect')
        return False    