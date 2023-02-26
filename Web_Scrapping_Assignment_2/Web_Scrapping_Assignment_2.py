#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install selenium')


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data

# In[4]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[14]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[15]:


driver.get("https://www.naukri.com/")


# In[16]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation.send_keys('Data Analyst')


# In[17]:


location=driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[18]:


search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[30]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[32]:


title_tags=driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[33]:


print(len(job_title), len(job_location), len(company_name), len(experience_required) )


# In[34]:


import pandas as pd
df=pd.DataFrame({'Title' : job_title, 'Location': job_location, 'Company':company_name, 'Experience': experience_required})


# In[35]:


df


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[48]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.naukri.com/")


# In[49]:


designation1=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation1.send_keys('Data Scientist')
locatio1n=driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location1.send_keys('Bangalore')
search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[50]:


job_title1=[]
job_location1=[]
company_name1=[]


# In[51]:


title_tags1=driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tags1[0:10]:
    title1=i.text
    job_title1.append(title1)
    
location_tags1=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tags1[0:10]:
    location1=i.text
    job_location1.append(location1)

company_tags1=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags1[0:10]:
    company1=i.text
    company_name1.append(company1)


# In[52]:


print(len(job_title1), len(job_location1), len(company_name1) )


# In[53]:


import pandas as pd
df=pd.DataFrame({'Title' : job_title1, 'Location': job_location1, 'Company':company_name1})


# In[54]:


df


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below.You have to use the location and salary filter.You have to scrape data for “Data Scientist” designation for first 10 job results. You have to scrape the job-title, job-location, company name, experience required.The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.naukri.com/")


# In[2]:


designation2=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation2.send_keys('Data Scientist')
search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[3]:


loc=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]").click()


# In[4]:


sal=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]").click()


# In[5]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[6]:


title_tags=driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[8]:


import pandas as pd
df=pd.DataFrame({'Title' : job_title, 'Location': job_location, 'Company':company_name, 'Experience': experience_required})
df


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:1. Brand 2. Product Description 3. Price

# In[82]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.flipkart.com/")


# In[83]:


item=driver.find_element(By.CLASS_NAME, "_3704LK")
item.send_keys('Sunglasses')


# In[84]:


search=driver.find_element(By.CLASS_NAME, "L0Z3Pu")
search.click()


# In[85]:


brand=[]
description=[]
price=[]
discount=[]


# In[86]:


start=0
end=3

for page in range(start,end):

    brands=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')

    for i in brands:

        brand.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")   


# In[87]:


start=0
end=3

for page in range(start,end):

    desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')

    for i in desc:

        description.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")   


# In[88]:


start=0
end=3

for page in range(start,end):

    p=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')

    for i in p:

        price.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")   


# In[89]:


start=0
end=3

for page in range(start,end):

    disc=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')

    for i in disc:

        discount.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")   


# In[90]:


print(len(brand))


# In[91]:


print(len(description))


# In[92]:


print(len(price))


# In[93]:


print(len(discount))


# In[94]:


import pandas as pd
df1=pd.DataFrame({'Brand' : brand, 'Description': description, 'Price': price, 'Discount':discount})


# In[95]:


df1


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART

# In[177]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd")


# In[178]:


rating=[]
review_summary=[]
full_review=[]


# In[179]:


load=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[7]/div/a").click()


# In[180]:


start=0
end=10

for page in range(start,end):

    r=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')

    for i in r:

        rating.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]")   


# In[181]:


start=0
end=10

for page in range(start,end):

    rs=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')

    for i in rs:

        review_summary.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]")   


# In[182]:


start=0
end=10

for page in range(start,end):

    fl=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')

    for i in fl:

        full_review.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]") 


# In[183]:


import pandas as pd
df=pd.DataFrame({'Rating' : rating, 'Review': review_summary, 'Full Review': full_review})


# In[184]:


df


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.You have to scrape 3 attributes of each sneaker:1. Brand 2. ProductDescription 3. Price

# In[123]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.flipkart.com/")


# In[124]:


item=driver.find_element(By.CLASS_NAME, "_3704LK")
item.send_keys('Sneakers')


# In[125]:


search=driver.find_element(By.CLASS_NAME, "L0Z3Pu")
search.click()


# In[126]:


brand=[]
description=[]
price=[]


# In[127]:


start=0
end=3

for page in range(start,end):

    brands=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')

    for i in brands:

        brand.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]") 


# In[128]:


start=0
end=3

for page in range(start,end):

    desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')

    for i in desc:

        description.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")


# In[129]:


start=0
end=3

for page in range(start,end):

    pr=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')

    for i in pr:

        price.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]") 


# In[130]:


print(len(brand))


# In[131]:


print(len(description))


# In[132]:


print(len(price))


# In[133]:


import pandas as pd
df4=pd.DataFrame({'Brand' : brand, 'Description': description, 'Price': price})


# In[134]:


df4


# # Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# 

# In[36]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("chromedriver.exe")


# In[37]:


driver.get("https://www.amazon.in/")


# In[38]:


pdt=driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
pdt.send_keys('Laptop')


# In[39]:


search=driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[40]:


pro=driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[6]/li[13]/span/a/span").click()


# In[41]:


title=[]
rating=[]
price=[]


# In[42]:


title_tags=driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
for i in title_tags[0:10]:
    t=i.text
    title.append(t)
    
r_tags=driver.find_elements(By.XPATH, '//span[@class="a-size-base"]')
for i in r_tags[0:10]:
    r=i.text
    rating.append(r)
p_tags=driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
for i in p_tags[0:10]:
    p=i.text
    price.append(p)


# In[43]:


import pandas as pd


# In[44]:


df=pd.DataFrame({'Title' : title, 'Rating': rating, 'Price':price})
df


# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# 

# In[263]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("chromedriver.exe")


# In[264]:


driver.get("https://www.azquotes.com/")


# In[265]:


loc=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a").click()


# In[266]:


quote=[]
author=[]
qtype=[]


# In[267]:


start=0
end=10

for page in range(start,end):
    qu=driver.find_elements(By.XPATH,'//a[@class="title"]')

    for i in qu:
        quote.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a")


# In[268]:


start=0
end=10

for page in range(start,end):
    aut=driver.find_elements(By.XPATH,'//div[@class="author"]')

    for i in aut:
        author.append(i.text)

    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a")


# In[269]:


start=0
end=10

for page in range(start,end):
    qt=driver.find_elements(By.XPATH,'//div[@class="tags"]')

    for i in qt:
        qtype.append(i.text)
    
    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[4]/li[12]/a")


# In[270]:


print(len(quote))


# In[271]:


print(len(author))


# In[272]:


print(len(qtype))


# In[273]:


import pandas as pd
df=pd.DataFrame({'Quote' : quote, 'Author': author, 'Type': qtype})
df


# # Q9 : Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/

# In[274]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("chromedriver.exe")


# In[275]:


driver.get("https://www.jagranjosh.com/")


# In[276]:


gk=driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[9]/a").click()


# In[278]:


pm=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a").click()


# In[279]:


name=[]
span=[]
term=[]
remarks=[]


# In[283]:


name_tags=driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[3]/td[2]/p')
for i in name_tags[0:18]:
    title=i.text
    name.append(title)
    
span_tags=driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[3]/td[2]/p')
for i in span_tags[0:18]:
    sp=i.text
    span.append(sp)

term_tags=driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[3]/td[2]/p')
for i in term_tags[0:18]:
    tm=i.text
    term.append(tm)
    
r_tags=driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[3]/td[2]/p')
for i in r_tags[0:18]:
    rm=i.text
    remarks.append(rm)


# In[284]:


import pandas as pd
df=pd.DataFrame({'Name' : name, 'Period': span, 'Term': term, 'Remarks':remarks})
df


# # Q10) Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com

# In[330]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("chromedriver.exe")


# In[331]:


driver.get("https://www.motor1.com/")


# In[333]:


ls=driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div").click()


# In[334]:


fs=driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/ul/li[5]/button").click()


# In[335]:


lt=driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a").click()


# In[336]:


exp=driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[1]/div[1]/div/div/div[4]/div/div[1]/h3/a").click()


# In[337]:


car=[]
price=[]


# In[338]:


car_tags=driver.find_elements(By.XPATH, '//h3[@class="subheader"]')
for i in car_tags[0:50]:
    c=i.text
    car.append(c)
    


# In[339]:


print(len(car))


# In[325]:


import pandas as pd
df=pd.DataFrame({'Car':car})


# In[326]:


df


# In[ ]:




