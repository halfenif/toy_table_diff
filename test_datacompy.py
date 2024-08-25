from io import StringIO 
import pandas as pd 
import datacompy 
   
      
data1 = """employee_id, name, year_in, year_retire, rank_dept, rank_hr
1, rajiv kapoor , 1972, , SSS, ZZZ
2, rahul agarwal , 1972, , SSS, ZZZ
3, alice johnson , 1972, , SSS, ZZZ
"""
   
data2 = """employee_id, name, year_in, year_retire, rank_dept, rank_hr 
1, rajiv khanna , 1972, , SSS, ZZZ
2, rahul aggarwal , 1982, 2000, SSS, ZZZ
3, alice tyson , 1972, , SSS, ZZZ
"""
   
df1 = pd.read_csv(StringIO(data1)) 
df2 = pd.read_csv(StringIO(data2)) 
   
compare = datacompy.Compare( 
    df1, 
    df2, 
      
    # You can also specify a list 
    # of columns 
    join_columns = 'employee_id',  
      
    # Optional, defaults to 0 
    abs_tol = 0, 
      
    # Optional, defaults to 0 
    rel_tol = 0,  
      
    # Optional, defaults to 'df1' 
    df1_name = 'Original', 
      
    # Optional, defaults to 'df2' 
    df2_name = 'New' 
    ) 
  
# if ignore_exra_columns=True,  
# the function won't return False 
# in case of non-overlapping  
# column names 
compare.matches(ignore_extra_columns = False)    
   
# This method prints out a human-readable  
# report summarizing and sampling  
# differences 
print(compare.report()) 