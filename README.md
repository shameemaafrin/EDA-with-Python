## Data Exploration in Python

### Dataset Overview
We begin by loading the dataset into a DataFrame named `tordata`. Displaying the initial data provides a snapshot of the contents.
![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/ef1c7207-c0ab-4a8b-b310-485cebaad230)


- `tordata.dtypes` lists all data types within the DataFrame.
  ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/218abc09-4a2c-4518-9214-e2ff9d0e6324)

- `tordata.mo` displays data pertaining to different months.
  ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/d8f92635-fc7c-4638-b1f9-63f53ecbe77f)


### Visual Analysis
1. **Monthly Data Distribution**
   - A histogram showing data distribution by month.
   - Data values sorted in ascending order indicate the arrangement of months.
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/01f59841-4e45-4be0-ab99-133fc3dcd076)
     

2. **Relationship Between Month and Magnitude**
   - The relationship is depicted through a detailed graph showing trends and outliers.
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/a01160e0-6225-43a6-9a93-7635261d883e)


3. **State-wise Analysis**
   - Ohio (OH) shows the highest average injuries, while Massachusetts (MA) shows the highest average fatalities.
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/f84899e2-bfa2-435f-96c9-2a278e12f19d)
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/4606e080-dcc1-4671-81c3-dd7715dc6dc7)


   - Texas (TX) experiences a higher percentage (13%) of tornado occurrences compared to other states such as Kansas (KS), Oklahoma (OK), and Florida (FL).
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/1b4153c2-6715-47cf-b70d-15f86320656b)

     
4. **Temporal Trends**
   - December records the highest number of tornadoes, suggesting an increase towards the year's end.
   - Over the years, there is a visible increase in tornado occurrences.
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/e0bbf53b-aee7-4cee-aafb-e6cba54b1a9b)
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/4d93931a-ef87-4bf0-95b0-8b9bbf081da8)



5. **Boxplot Analysis**
   - A boxplot provides a statistical summary for different years, emphasizing Texas as the state with the most tornadoes and December as the most prone month.
     ![image](https://github.com/shameemaafrin/EDA-with-Python/assets/77144007/effd3b75-c8c8-4049-8d4b-a87315255632)

### Conclusion
The analysis underscores the importance of data analytics in understanding and preparing for tornado occurrences. Without this collected data, identifying tornado-prone months and states would be challenging. This information allows for better preparedness and precautionary measures.
