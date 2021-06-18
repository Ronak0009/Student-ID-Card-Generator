Steps to run file:
1. First install all the required libraries which are in the requirements.txt.
2. To run this you must install MySql in the system.
3. Install MySql in your system and create user in it.
4. Now after configuring MySql, change host name, user name,database,password in line number #27.
 Eg:con=pymysql.connect(host='localhost',user='root',database='Project',password='your-password')
5. Now uncomment line number #31 #32 #33
   This lines will create database and table in mysql.
	or
   If there is any kind of error or If you dont want to run the 5th step than create database manually in MySql workspace.
6.Change path to save the generated QRcode image in line number #123.
  Eg: img=(r'your-path''+h)
7.Give the same path where qrcode image is save in line number #153 and #217.
8.Run the code file (idcard.py).
