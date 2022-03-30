# Python_XLS_File_Processing
 Process Excel Files with blank. If a cell and next cell is empty, it will take the value of the previous cell and fill in the rest. 
![image](https://user-images.githubusercontent.com/83979205/140432178-8cd7b225-7003-432a-a81a-805c2ad30d12.png)

FROM:
#    Order_ID Customer_name            Album_Name           Artist  Quantity
# 0       NaN           NaN            RadioShake              NaN       NaN
# 1       1.0       Bob Dole         The Bodyguard  Whitney Houston       2.0
# 2       1.0                             Lemonade          Beyonce       1.0
# 3       1.0                 The Thrill Of It All        Sam Smith       2.0
# 4       1.0                              Thriller  Michael Jackson      11.0
# 5       1.0                               Divide       Ed Sheeran       4.0
# 6       1.0                           Reputation     Taylor Swift       3.0
# 7       1.0                       Red Pill Blues         Maroon 5       5.0




TO this:

#    Order_ID Customer_name            Album_Name           Artist  Quantity
# 0       NaN           NaN            RadioShake              NaN       NaN
# 1       1.0       Bob Dole         The Bodyguard  Whitney Houston       2.0
# 2       1.0       Bob Dole              Lemonade          Beyonce       1.0
# 3       1.0       Bob Dole  The Thrill Of It All        Sam Smith       2.0
# 4       1.0       Bob Dole              Thriller  Michael Jackson      11.0
# 5       1.0       Bob Dole                Divide       Ed Sheeran       4.0
# 6       1.0       Bob Dole            Reputation     Taylor Swift       3.0
# 7       1.0       Bob Dole        Red Pill Blues         Maroon 5       5.0
