#!/usr/bin/env python
# coding: utf-8

# In[2]:


def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    import pandas as pd
    
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    
    EDUC1 = df['EDUC1'].value_counts(normalize=True)
    EDUC1_dict = {"less than high school": EDUC1.iloc[3],
                   "high school": EDUC1.iloc[2],
                   "more than high school but not college": EDUC1.iloc[1],
                   "college": EDUC1.iloc[0]}
    return EDUC1_dict
#     raise NotImplementedError()


# In[3]:


assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."


# In[7]:


def average_influenza_doses():
    # YOUR CODE HERE
    import pandas as pd
    
    df = pd.read_csv('NISPUF17.csv')
    
    df1 = df[df["CBF_01"] == 1]
    df2 = df[df["CBF_01"] == 2]
    
    return (df1["P_NUMFLU"].mean(), df2["P_NUMFLU"].mean())
#     raise NotImplementedError()


# In[8]:


assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."


# In[11]:


def chickenpox_by_sex():
    # YOUR CODE HERE
    import pandas as pd
    
    df = pd.read_csv('NISPUF17.csv')
    
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    df = df[["SEX", "HAD_CPOX", "P_NUMVRC"]].dropna()
    df = df[df["P_NUMVRC"] > 0]
    
    male_df = df[df["SEX"] == 1]
    female_df = df[df["SEX"] == 2]
    
    female_chickenpox = female_df[(female_df["HAD_CPOX"] == 1) & (female_df["P_NUMVRC"] >= 1)]
    female_non_chickenpox = female_df[(female_df["HAD_CPOX"] == 2) & (female_df["P_NUMVRC"] >= 1)]
    
    male_ratio = len(male_df[male_df["HAD_CPOX"] == 1])/len(male_df[male_df["HAD_CPOX"] == 2])
    female_ratio = len(female_df[female_df["HAD_CPOX"] == 1])/len(female_df[female_df["HAD_CPOX"] == 2])
    
    return {"male": male_ratio, "female": female_ratio}
#     raise NotImplementedError()


# In[12]:


assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."


# In[13]:


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv('NISPUF17.csv', index_col=0)
    df = df[df["HAD_CPOX"] <= 2]
    df = df[~df["P_NUMVRC"].isna() & ~df["HAD_CPOX"].isna()]

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])
    
    # just return the correlation
    return corr

    # YOUR CODE HERE
#     raise NotImplementedError()


# In[14]:


assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."


# In[ ]:





# In[ ]:




