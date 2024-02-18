# File: KerasData.py
# Author: Ha SeungJae 
# Date: February 18, 2024
# Description: Collecting and preprocessing data

import pandas as pd
import os
import urllib.request

class KerasData():

    def __init__(self):
        '''
        Names   :   Pills name
        Url     :   Pills url
        Path    :   Where save  pills image
        File    :   Pills name and url saved csv file
        
        Total_Percent : Check progress
        Error_Cnt     : Lost image
        '''
        self.Names = []
        self.Url   = []
        self.Path  = "D:/image_set/"
        self.File  = pd.read_csv('file.csv',
                                  sep = ',',
                                  encoding = 'cp949')
        self.Total_Percent = 0
        self.Error_Cnt     = 0

        # Check folder exist
        if not os.path.isdir(self.Path) :
            os.makedirs(self.Path)
        else :
            pass

    def Collect_Image(self):
        '''
        Collect image from file.csv
        '''     
        for Name in range(len(self.File)):
            for Url in range(len(self.File.columns)):
                if Url == 0:
                    self.Names.append(self.File.iloc[Name][Url])
                else:
                    self.Url.append(self.File.iloc[Name][Url])

        for Image_Num in range(len(self.Names)):
            try :
                Image_Path = self.Path + str(self.Names[Image_Num] + '.png')
                Url_Link   = ''.join(self.Url[Image_Num])
                urllib.request.urlretrieve(Url_Link, Image_Path)
                os.system('cls')
                self.Total_Percent += 0.004
                print(" Percent : {0:.2f} % ".format(self.Total_Percent))

            except:
                self.Error_Cnt += 1
                os.system('cls')
                print(" Losted Image : {} ".format(self.Error_Cnt))