# Do a bulk load for these two table for respective dataset
import pandas as pd
import mysql.connector as conn
mydb = conn.connect(host = "localhost", user ="root", passwd = "0000")
myCursor = mydb.cursor()

myCursor.execute("use iNeuronTasksClass")

#myCursor.execute("insert into attribute values (966005983,'Brief','Average',4.6,'L','Spring','o-neck','full','natural','silk','chiffon','embroidary','print',1),(876339541,'cute','Low',4.5,'M','Summer','o-neck','butterfly','natural','chiffonfabric','chiffon','bow','dot',0),(1068332458,'bohemian','Low',0.0,'M','Summer','v-neck','sleevless','empire',NULL,NULL,NULL,'print',0)")

myCursor.execute("insert into dress values (1006032852,2114,2274,2491,2660,2727,2887,2930,3119,3204,3277,3321,3386,3479,3554,3624.0,3706,3746.0,3795.0,3832.0,3897,3923.0,3985.0,4048),(1212192089,151,275,570,750,813,1066,1164,1558,1756,1878,1985,2106,2454,2710,2942.0,3258,3354.0,3475.0,3654.0,3911,4024.0,4125.0,4277),(1190380701,6,7,7,7,8,8,9,10,10,10,10,10,11,11,11.0,11,11.0,11.0,11.0,11,11.0,11.0,11),(966005983,1005,1128,1326,1455,1507,1621,1637,1723,1746,1783,1796,1812,1845,1878,1892.0,1914,1924.0,1929.0,1941.0,1952,1955.0,1959.0,1963),(876339541,996,1175,1304,1396,1432,1559,1570,1638,1655,1681,1743,1824,1919,2032,2156.0,2252,2312.0,2387.0,2459.0,2544,2614.0,2693.0,2736)")
mydb.commit()





