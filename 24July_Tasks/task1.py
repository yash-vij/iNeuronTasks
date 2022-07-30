import mysql.connector as conn
mydb = conn.connect(host = "localhost", user ="root", passwd = "0000")

myCursor = mydb.cursor()
myCursor.execute("create database if not exists iNeuronTasks")
myCursor.execute("use iNeuronTasks")
myCursor.execute("create table if not exists attribute(Dress_ID int(50), Style varchar(30),	Price int(20), Rating int(20), Size varchar(10), Season varchar(30), NeckLine varchar(30), SleeveLength varchar(30), waiseline varchar(30), Material varchar(30),FabricType	varchar(30), Decoration varchar(30),Pattern_Type varchar(30), Recommendation int(2)) ")
myCursor.execute("create table if not exists dress(Dress_ID	int(50), `29/8/2013` int(10),	`31/8/2013` int(10),	`2/9/2013` int(10),	`4/9/2013` int(10),	`6/9/2013` int(10),	`8/9/2013` int(10),	`10/9/2013` int(10),	`12/9/2013` int(10),	`14/9/2013` int(10),	`16/9/2013` int(10),	`18/9/2013` int(10),	`20/9/2013` int(10),	`22/9/2013` int(10),	`24/9/2013` int(10),	`26/9/2013` int(10),	`28/9/2013` int(10),	`30/9/2013` int(10),	`2/10/2013` int(10),	`4/10/2013` int(10),	`6/10/2013` int(10),	`8/10/2010` int(10),	`10/10/2013` int(10),	`12/10/2013` int(10))")
myCursor.execute("show tables")
print(myCursor.fetchall())