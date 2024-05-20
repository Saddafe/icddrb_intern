#!/usr/bin/env python
# coding: utf-8

# # Prevalence Estimate

# In[4]:


# Import packages
import pandas as pd
import numpy as np
import scipy.stats as stat
import os


# In[13]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("fhs.csv", index_col="randid")
# Drop NaN
df.dropna(subset=["hyperten"], inplace=True)
df['hyperten'].head()


# In[12]:


# Calculate proportion
var=df["hyperten"]
prop=round(var.mean(),3)

# Calculate standard error
se=round(var.sem(),3)

# Calculate 95% confidence interval
ci_95=stat.norm.interval(confidence=0.95, loc=var.mean(), scale=var.sem())
# Rounding results
ci_lu=round(ci_95[0],3)
ci_up=round(ci_95[1],3)
ci_95=((ci_lu,ci_up))

# Format results
txt=(" Prevalence ={}\n Standard Error= {}\n 95% confidence interval= {}")
# Print results
print(txt.format(Prop,se,ci_95))


# # Chi Square Test

# In[18]:


# Import packages
import pandas as pd
from scipy.stats import chi2_contingency
import os


# In[19]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("fhs.csv", index_col="randid")
# Drop NaN
#df.dropna(subset=["sex1", "death"], inplace=True)
df.head()


# In[21]:


# Calculate cross tabulation
my_tab=pd.crosstab(index=df['death'], columns=df['sex1'])
# Calculate chi square test statistics
c, p, dof, expected = chi2_contingency(my_tab)
# Print results
print(f"Chi2 value={c}\n p-value= {p} \n Degrees of freedom= {dof} \n Crosstable={expected}")


# The value of expected cell is not less than 5. Fisher exact test is correct test to use here.

# In[26]:


from scipy.stats import fisher_exact

# Calculate fisher exact test statistics
fisher=fisher_exact(my_tab, alternative='two-sided')
# Print results
print("Fishe Exact Test = ", fisher)


# # Risk Difference

# In[33]:


# Import packages
import pandas as pd
from zepid import RiskDifference
import os


# In[34]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("fhs.csv", index_col="randid")
# Drop NaN
df.dropna(subset=["hyperten", "death"], inplace=True)
df.head()


# In[35]:


# Calculate risk difference
rd=RiskDifference()
rd.fit(df, exposure="hyperten", outcome="death")
# Print summary results
print(rd.summary())


# # Risk Ratio (RR)

# In[1]:


# Import packages
import pandas as pd
from zepid import RiskRatio
import os


# In[2]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("fhs.csv", index_col="randid")
# Drop NaN
df.dropna(subset=["hyperten", "death"], inplace=True)
df.head()


# In[3]:


# Calculate Risk Ratio
rr=RiskRatio()
rr.fit(df,exposure="hyperten",outcome="death")
# Print results
print(rr.summary())


# # Odds Ratio (OR)

# In[4]:


# Import packages
import pandas as pd
from zepid import OddsRatio
import os


# In[5]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("fhs.csv", index_col="randid")
# Drop NaN
df.dropna(subset=["hyperten", "death"], inplace=True)
df.head()


# In[6]:


# Calculation of Odds Ratio
OR=OddsRatio()
OR.fit(df,exposure="hyperten",outcome="death")
# Print result summary
print(OR.summary())


# # Incidence Rate Ratio

# In[8]:


# Import packages
import pandas as pd
from zepid import IncidenceRateRatio
import os


# In[9]:


# change directory
os.chdir("D:/All is Well/icddrb/Data")

# load data
df=pd.read_csv("incidencerate.csv", index_col="id")
df.head()


# In[11]:


# Calculate incidence rate ratio
IRR=IncidenceRateRatio()
IRR.fit(df, exposure="sex", outcome="total_case", time="time")
# Print result summary
print(IRR.summary())


# In[ ]:




