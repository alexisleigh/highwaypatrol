Last login: Sat Nov  3 17:25:18 on ttys001
MacBook-Pro-9:~ energetti1611$ workon dataj
(dataj) MacBook-Pro-9:~ energetti1611$ python
Python 2.7.10 (default, Aug 17 2018, 17:41:52) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests, mechanize
>>> from bs4 import BeautifulSoup
>>> 
>>> url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=10/31/2017'
>>> 
>>> br = mechanize.Browser()
>>> br.open(url)
<response_seek_wrapper at 0x10b999758 whose wrapped object = <closeable_response at 0x10b9995f0 whose fp = <socket._fileobject object at 0x10b790ad0>>>
>>> html = br.response().read()
>>> soup=BeautifulSoup(html, "html.parser")
>>> 
>>> main_table = soup.find('table', {'class':'accidentOutput'})
>>> row_list = main_table.find_all('tr')
>>> for r in row_list:
...     cell_list = r.find_all('td')
...     if len(cell_list) > 0:
...         for c in cell_list:
...             print c.text.strip()
...         print '---------'
... 
View
FANN, DALTON C
20
BOURBON, MO
10/31/2017
11:13PM
CRAWFORD
I
---------
View
DABNEY, SESSILEAH N
28
INDEPENDENCE, MO
10/31/2017
10:55PM
CASS
A
---------
View
BRADLEY, JOHNSON L
57
KANSAS CITY, MO
10/31/2017
10:40PM
HOLT
H
---------
View
SHINN, DALE E
62
JOPLIN, MO
10/31/2017
9:50PM
BATES
A
---------
View
JEFFRIES, PAMELA R
38
WARRENTON, MO
10/31/2017
9:40PM
LINCOLN
C
---------
View
STEWARD, PATRICK J
50
COLUMBIA, MO
10/31/2017
9:40PM
LINCOLN
C
---------
View
TURIELLO, ALEXA S
19
LAWRENCE, KS
10/31/2017
9:40PM
BOONE
F
---------
View
WILLIAMS, MARSHAWN P
38
MEMPHIS,TN
10/31/2017
9:24PM
SCOTT
E
---------
View
MCALPINE, NELSON
26
ST LOUIS, MO
10/31/2017
9:15PM
ST. LOUIS CITY
C
---------
View
PALMER, STACEY R
41
RICHMOND, MO
10/31/2017
8:24PM
RAY
A
---------
View
PHILLIPS, BRADLEY W
47
STANBERRY, MO
10/31/2017
7:10PM
NODAWAY
H
---------
View
WILLIAMS, BRANDI D
42
RICH HILL, MO
10/31/2017
6:57PM
BATES
A
---------
View
BREWSTER, QUADRICQUS C
34
POPLAR BLUFF, MO
10/31/2017
6:51PM
BUTLER
E
---------
View
BISHOP, SCOTT M
38
MOBERLY, MO
10/31/2017
6:17PM
RANDOLPH
B
---------
View
OBERKRAMER, ROGER W
52
HOUSE SPRINGS, MO
10/31/2017
6:06PM
FRANKLIN
C
---------
View
KAMINSKI, JOSEPH W
62
ST LOUIS, MO
10/31/2017
5:54PM
ST. LOUIS
C
---------
View
BECKER, SHAWN P
36
SEDALIA, MO
10/31/2017
5:45PM
MORGAN
F
---------
View
FREEMAN, SETH D
23
ANDERSON, MO
10/31/2017
5:35PM
NEWTON
D
---------
View
WIEDMAIER, AMANDA J
23
CAMERON, MISSOURI
10/31/2017
5:31PM
DEKALB
H
---------
View
MARTIN, VIRGINIA L
45
ULMAN, MO
10/31/2017
4:50PM
MILLER
F
---------
View
STROBL, JOSEPH A
33
HILLSBORO, MO
10/31/2017
3:37PM
JEFFERSON
C
---------
View
WALLACE, JENNIFER N
31
ST LOUIS, MO
10/31/2017
2:16PM
ST. LOUIS CITY
C
---------
View
BARNES, JAMES A
26
FLORISSANT, MO
10/31/2017
1:58PM
ST. LOUIS CITY
C
---------
View
HAYES, ALEX M
22
ST LOUIS, MO
10/31/2017
1:52PM
ST. LOUIS
C
---------
View
BIRCH, FRED T
56
INDEPENDENCE, MISSOURI
10/31/2017
1:47PM
PLATTE
A
---------
View
PONDER, JESSE D
24
ELDON, MO
10/31/2017
1:15PM
MILLER
F
---------
View
COYLE, BRANDON L
20
WASHINGTON, MO
10/31/2017
1:12PM
FRANKLIN
C
---------
View
WARREN, JELANI K
24
ST LOUIS, MISSOURI
10/31/2017
1:08PM
JOHNSON
A
---------
View
STEPHENS, JENNIFER N
42
EAST ST LOUIS, IL
10/31/2017
12:53PM
ST. LOUIS CITY
C
---------
View
PEDROLEY, MATTHEW S
27
ST LOUIS, MO
10/31/2017
11:33AM
ST. LOUIS CITY
C
---------
View
PETREE, BRITTANI L
30
LAKE OZARK, MO
10/31/2017
10:15AM
CAMDEN
F
---------
View
MOSS, KYLE M
17
ST LOUIS, MISSOURI
10/31/2017
8:34AM
JOHNSON
A
---------
View
MAZE, KASSIDY M
17
LAMAR, MO
10/31/2017
7:35AM
BARTON
D
---------
View
WHITTLE, JACOB R
27
SPRINGFIELD, MO
10/31/2017
2:00AM
GREENE
D
---------
View
PESKISHEV, VANESSA J
26
ROLLA, MO
10/31/2017
1:35AM
BOONE
F
---------
View
WATSON, JACOB E
24
SPRINGFIELD, MO
10/31/2017
1:01AM
GREENE
D
---------
View
BENNETT, ERIN M
33
SPRINGFIELD, MO
10/31/2017
12:42AM
GREENE
D

