
###############################################
# ÖDEV /HOMEWORK 3: List Comprehension Applications
###############################################

###############################################
# Görev 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
#Convert the names of the numeric variables in the 'car_crashes 'data to uppercase  and add NUM at the beginning of the names
###############################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Veri setini baştan okutarak aşağıdaki çıktıyı elde etmeye çalışınız.
# Try to get the following output by reading the data set from the beginning.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar/Notes:
# Numerik olmayanların da isimleri büyümeli./Categoric varaibels also should be in uppercase
# Tek bir list comp yapısı ile yapılmalı. /Code should be in comprehension list and single line


###############################################
# Görev 1 Çözüm
# Task 1 Solution
###############################################

["NUM_" + col.upper() if df[col].dtype!='O' else col.upper() for col in df.columns]

###############################################
# Görev 2: İsminde "no" BARINDIRMAYAN değişkenlerin isimlerininin SONUNA "FLAG" yazınız.
# Task 2: Add "FLAG" at the end of the names of the variables that do not contain "no" in their name.
###############################################

# Notlar/Notes::
# Tüm değişken isimleri büyük olmalı./All variable names must be large.
# Tek bir list comp ile yapılmalı/Code should be in comprehension list and single line

# Beklenen çıktı/Expected output:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']
###############################################
# Görev 2 Çözüm/Task 2 Solution:
###############################################

[col.upper() if "NO" in col else col.upper()+"_FLAG" for col in df.columns ]

###############################################
# Görev 3: Aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçerek yeni bir df oluşturunuz.
# Task 3: Create a new df by selecting the names of the variables that are DIFFERENT from the variable names given below.
###############################################

# df.columns
# og_list = ["abbrev", "no_previous"]

# Notlar/Notes:
# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz./First create a new list named new_cols using list comprehension according to the list above.
# Sonra df["new_cols"] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz./Then create a new df by selecting these variables with df ["new_cols"] and name it as new_df.


# Beklenen çıktı/Expected output:

# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630
###############################################
# Görev 3 Çözüm/Task 3 Solution
###############################################

new_cols=[col for col in df.columns if col!="abbrev" and col!="no_previous"]
new_df=df[new_cols]
