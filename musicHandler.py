# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:18:49 2018

@author: edwin
"""

from musicFactory import *

#This is the folder where music files are located
defaultDir1='C:/Users/edwin/Documents/music/musicSimulator/musicFile/Test3'
genre='Test'
window=0.04;step=0.04

class MusicHandler(object):
    defaultDir=defaultDir1;
    newFactory=MusicFactory()  
    newFactory.loadMusic(genre,defaultDir,window,step);newFactory.saveMusicInfo()
    #Saving index of the musicfile that received either positive or negative result
    # Static variables to be shared by all objects 
    posMusic=[];negMusic=[];absMusic=[];
    results=[]
    predictRate=0
    
    #Past choices will be saved in history
    history={}
    musicCount=20
    # will be overwritten 

    ###player----
    def musicPlay(self):
        pass
    
    def displayHistory(self):
        pass
    
 
    
    ## selector-----
    def randomSelect(self):
        pass
     
    ## Classifier-----
    def binaryClassifier(self):
        pass
    
    def testClassifier(self):
        pass
        
    def mostFavSelect(self):
        pass
    
    
