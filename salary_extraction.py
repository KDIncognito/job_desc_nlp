# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:33:41 2019

@author: 703162279
"""
import pandas as pd

file= pd.read_csv("/.../Project/jobs_all.csv",encoding = "ISO-8859-1")

import numpy as np

import spacy
import re
import math

nlp = spacy.load('en')
nlp = spacy.load('en_core_web_sm')

out_p = pd.DataFrame()
out_p = pd.DataFrame(columns=['iter','s_type','s_amt','y_type','y_amt','w_type','w_amt','h_type','h_amt','r_type','r_amt','d_type','d_sal','m_type','m_sal'])

for i in range(len(file)):
    c=''
    a=''
    b=''
    e=''
    ob=''
    text_c=''
    s_type=''
    s_amt=''
    y_type=''
    y_amt=''
    w_type=''
    w_amt=''
    h_type=''
    h_amt=''
    r_type=''
    r_amt=''
    m_type=''
    m_amt=''
    d_type=''
    d_amt=''
    
    
    a= file.loc[i,"description"] #acts on description field
    a= a.lower()
    a=re.sub('[\d+]+\-[\d+]+\-[\d+]+',"",a) # phone numbers are removed
    a=re.sub('(\$)([\d+]+)(?:k)','\\1\\2,000 ',a) #convert k to '000
    a=re.sub('\,','',a)
    a=re.sub('\;','.',a)
    a= re.sub('\.00','',a) #remove decimals
    a= re.sub(r'\+','',a)
    a= re.sub(r' to ',' - ',a)
    range_pat_1=(r"(\$\d+[.]?[\d+]{2}?[\s]?)\-([\s]?\$\d+[.]?[\d+]{2}?)")
    range_pat_2=(r"(\$\d+[\s]?)\-([\s]?\$\d+)")
    
    if bool(re.search(r"([$]\d{1,}[.]?\d+)([\s]?[\-]?[\s]?)([$]\d{1,}[.]?\d+)",a)):
        ax= re.sub(r"([$]\d{1,}[.]?\d+)([\s]?[\-]?[\s]?)([$]\d{1,}[.]?\d+)","\\1-\\3",a)
        for nums in re.findall("([$]\d{1,}[.]?\d+)([\s]?[\-]?[\s]?)([$]\d{1,}[.]?\d+)",ax):
            nums=str(nums)
            nums= re.sub("[$,()']", "", nums)
            nums= re.sub('-','',nums)
            nums= re.sub(' +',' ',nums)
            p,q=map(float,nums.split())
            numbro=math.ceil((p+q)/2)
            numbro='$'+str(numbro)
            ax= re.sub("([$]\d{1,}[.]?\d+)([\s]?[\-]?[\s]?)([$]\d{1,}[.]?\d+)",numbro,ax) # ranged numbers are modified to single number
            a=ax
            
    a= re.sub('{|}','',a)
    a= re.sub("week[ly] home|weekend|hours|months|gross","",a) #removing false positive words for continuity
    a=re.sub(r'(annum|annual|mnth|yr|wk|day|cpm|cost per mile|refer|hour|hr|sign|year|week|month|revenue)',r'{\1} ',a.lower())
    #a=re.sub(r"([\$]\d+\D+)per (?!{)","",a) #deletes a pattern with 'per'
    a= re.sub(r'(?<!\s)\{',' {',a)
    a= re.sub(r'(?<!\s)\$',' $',a)
    a= re.sub(r'([0-9]+)([a-z]+)','\\1 \\2',a)
    a=nlp(a)
    for ent in a.ents:
        text_c += ent.label_ +': ' + ent.text +', '
    
    b= re.findall('MONEY\:\s((\D+)?[\d]+)',text_c)
    l_ob= list(set(b))
    ob=[i[0] for i in l_ob]
    #db= list(map(lambda x: x.replace('MONEY:','').replace('  ',''),ob))

    for sal in ob:
        sal= re.sub("\D","",sal)
        if bool(re.search(re.escape(sal)+"(?:\W+\w+){0,5}(?:\W+)+\{\w+|\{\w+(?:\W+\w+){0,5}(?:\W+)"+re.escape(sal), str(a))):
            e=re.search(re.escape(sal)+"(?:\W+\w+){0,5}(?:\W+)+\{\w+|\{\w+(?:\W+\w+){0,5}(?:\W+)"+re.escape(sal), str(a))
            tex=e.group()
            if '{y|{a' in  tex:
                y_type= 'year'
                y_amt= sal
            if '{w' in tex:
                w_type='week'
                w_amt=sal
            if '{h' in tex:
                h_type='hour'
                h_amt=sal
            if '{s' in tex:
                s_type='sign up'
                s_amt=sal
            if '{r' in tex:
                r_type= 'referral'
                r_amt= sal
            if '{m' in tex:
                m_type= 'month'
                m_amt= sal
            if '{d' in tex:
                d_type= 'day'
                d_amt= sal    
            out_p=out_p.append({'iter':i,'s_type':s_type,'s_amt':s_amt,'y_type':y_type,'y_amt':y_amt,'w_type':w_type,'w_amt':w_amt,'h_type':h_type,'h_amt':h_amt,'r_type':r_type,'r_amt':r_amt,'m_type':m_type,'m_sal':m_amt,'d_type':d_type,'d_sal':d_amt}, ignore_index=True)

    print(i)
