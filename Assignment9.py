# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:50:00 2018

@author: Patrick
"""

#Assignment 9

###NUMBER 1###
from plotnine import *
import numpy as np
import pandas as pd

pitching=pd.read_csv('PitcherData.txt',sep='\t',header=0)

scatter=ggplot(pitching,aes(x="Command",y="ERA"))+theme_classic()+xlab('Pitchers Command')+ylab('ERA')
scatter+geom_point()+stat_smooth(method="lm")

###NUMER 2###
data=pd.read_csv('data.txt',sep=',',header=0)
#Barplot of the means of the observations
b=ggplot(data,aes(x='factor(region)',y='observations'))+theme_classic()+ylab('Observations')+xlab('Region')
b+geom_bar(stat='summary', fun_y=np.mean)
#Scatterplot of all of the observations
c=ggplot(data,aes(x='factor(region)',y='observations'))+theme_classic()+ylab('Observations')+xlab('Region')
c+geom_jitter()

#Do the barplot and the scatterplot tell different stories?

#Yes. The barplot indicates that the average number of observation for each of the regions is 
#about equivilant (all regions have an average of about 15 observations). However, when the 
#scatterplot is used to show the distributions of the four regions, it becomes clear that 
#the four directions have very different distributions in number of observations. East and 
#West have wide distributions from about 0 to about 30 observations. All of the North data 
#points had about 15 observatoins, so there was a very small distribution for it. Finally, 
#South had a bimodal distribution, with two seperate averages of about 5 and 25, so that the
#overall average number of observations is about 15. In this case, the scatterplot tells a 
#more complete story about the data.