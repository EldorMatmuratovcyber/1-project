import numpy as np
#1. massiv yaratish
raqam=np.array([1,2,3,4,5])
raqam_guruh=np.array([[1,2,3], [4,5,6]])

#2. matematik operatsiyalar
sum_raqam=np.sum(raqam)
mean_raqam=np.mean(raqam)
product_raqam=np.prod(raqam)

sum_raqam_guruh=np.sum(raqam_guruh)
mean_raqam_guruh=np.mean(raqam_guruh)
product_raqam_guruh=np.prod(raqam_guruh)

print("Raqam Massiv: ", raqam)
print("Raqamlar Massiv:\n", raqam)
print("Massivlar yigindisi: ", sum_raqam)
print("O`rtacha: ", mean_raqam)
print("Ko`paytma: ", product_raqam)

print("Raqam Massiv: ", raqam_guruh)
print("Raqamlar Massiv:\n", raqam_guruh)
print("Massivlar yigindisi: ", sum_raqam_guruh)
print("O`rtacha: ", mean_raqam_guruh)
print("Ko`paytma: ", product_raqam_guruh)





import pandas as pd
#1. DataFrame yaratish
data={
    'ism':['Eldor', 'Anvarjon', 'Mahmudbek'],
    'Yoshi':[20,19,20],
    'Shahar':['Xorazm', 'Fargona', 'Fargona']
}
df=pd.DataFrame(data)

#2. Ma`lumotlarni ko`rish
print(df)

#3. Filtrlash
young_people=df[df['Yoshi']<20]
print("20 yoshdan kichiklar:\n", young_people)

#4. O`zgartirish
df['Yoshi']+=1 #har bir shaxsning yoshini 1 ga oshirish
print("Yangilangan DataFrame:\n", df)
#5.CSV formatdda saqlash
df.to_csv('data.csv', index=False)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                .................................................................................................................... ism  Yoshi   Shahar
# 0      Eldor     20   Xorazm
# 1   Anvarjon     19  Fargona
# 2  Mahmudbek     20  Fargona
#20 yoshdan kichiklar:
#         ism  Yoshi   Shahar
# 1  Anvarjon     19  Fargona
#Yangilangan DataFrame:
#          ism  Yoshi   Shahar
#0      Eldor     21   Xorazm
#1   Anvarjon     20  Fargona
#2  Mahmudbek     21  Fargona