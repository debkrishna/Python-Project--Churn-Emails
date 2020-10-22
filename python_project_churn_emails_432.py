#!/usr/bin/env python
# coding: utf-8

# # Python Project - Churn Emails - Dataset

# ## We have a text file which records mail activity from various individuals in an open source project development team. Below is the file location

# In[ ]:


filehandle = open("/cxldata/datasets/project/mbox-short.txt")
filehandle.read()


# # Python Project - Churn Emails - Count the Number of Lines

# In[16]:


def number_of_lines():
    path = "/cxldata/datasets/project/mbox-short.txt"
    f = open(path)
    cnt = 0
    for x in f:
        cnt = cnt +1
    return(cnt)


# In[17]:


number_of_lines()


# # Python Project - Churn Emails - Count the Number of Lines

# In[26]:


def count_number_of_lines():
    path = "/cxldata/datasets/project/mbox-short.txt"
    f = open(path)
    cnt = 0
    for x in f:
        x = x.rstrip()
        if x.startswith("Subject:"):
            cnt  = cnt +1
    return (cnt)


# In[27]:


count_number_of_lines()


# # Python Project - Churn Emails - Find Average Spam Confidence

# In[10]:


def average_spam_confidence():
    import re
    path = "/cxldata/datasets/project/mbox-short.txt"
    f = open(path)
    cnt = 0
    sm = 0
    for line in f:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            value = float((re.findall("[0-9]+\\.[0-9]+",line))[0])
            sm =sm + value
            cnt = cnt+1
    return(sm/cnt)
    


# In[11]:


average_spam_confidence()


# # Python Project - Churn Emails - Find Average Spam Confidence

# In[24]:


def find_email_sent_days():
    f = open("/cxldata/datasets/project/mbox-short.txt")
    lst =[]
    for line in f:
        line =line.rstrip()
        if line.startswith("From "):
            day  = (line.split())[2]
            lst.append(day)
    dct =dict()
    for day in lst:
        dct[day] = dct.get(day,0)+1
    return(dct)


# In[25]:


find_email_sent_days()


# # Python Project - Churn Emails - Count Number of Messages From Each Email Address

# In[81]:


def count_message_from_email():
    import re
    f = open("/cxldata/datasets/project/mbox-short.txt")
    lst =[]
    for line in f:
        if line.startswith("From "):
            email = re.findall("\S+@\S+",line)
            lst.append((email[0]))
    dct = dict()
    for keys in lst:
        dct[keys]  =dct.get(keys,0)+1
    return(dct)


# # Python Project - Churn Emails - Count Number of Messages From Each Domain

# In[47]:


def count_message_from_domain():
    f = open("/cxldata/datasets/project/mbox-short.txt")
    import re
    lst = []
    for line in f:
        if line.startswith("From:"):
            domain =  re.findall("@(\S+)",line)
            lst.append(domain[0])
    dct = dict()
    for keys in lst:
        dct[keys]  =dct.get(keys,0)+1
    return(dct)      


# In[48]:


count_message_from_domain()

