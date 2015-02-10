#Best works with windows
#pls install sudo apt-get install python-openpyxl
#in Windows download and copy openpyxl folder to C:/python/lib
#using module openpyxl for reading xls file
import re
import openpyxl as px
#open XLS file
W = px.load_workbook('dictionary_wdout_comprtmnts.xlsx', use_iterators = True)
#open sheet
p = W.get_sheet_by_name(name = 'dictionary_wdout_comprtmnts')
#read each columns
fullname=[]
metrecid=[]
pubchemid=[]
pubchemsid=[]
chebiid=[]
for row in p.iter_rows():
    fullname.append(row[0].internal_value.replace(u'\xa0', u' '))
    metrecid.append(row[1].internal_value)
    pubchemid.append(row[2].internal_value)
    pubchemsid.append(row[3].internal_value)
    chebiid.append(row[4].internal_value)
#replace none type with zeros and change ids to int
chebiids=[]
for i in range(0,len(chebiid)):
    if chebiid[i]==None:
        chebiids.append("0")
    else:
        chebiids.append(int(chebiid[i]))
#replace none type with zeros and change ids to int
pubchemids=[]
for i in range(0,len(pubchemid)):
    if pubchemid[i]==None:
        pubchemids.append("0")
    else:
        pubchemids.append(int(pubchemid[i]))
#replace none type with zeros and change ids to int
pubchemsids=[]
for i in range(0,len(pubchemsid)):
    if pubchemsid[i]==None:
        pubchemsids.append("0")
    else:
        pubchemsids.append(int(pubchemsid[i]))
#matching pattern for KEGG IDs
keggid=re.compile("^(C+[0-9]+)*$")
#HTML file generator
for i in range(0,len(fullname)):
    html_file=open('%s.html' % (metrecid[i]),'w')
    print >>html_file, """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title src="">MetRec</title>
  <link rel="shortcut icon" href="images/download.jpg" type="image/png"/>
  <link rel="stylesheet" type="text/css" href="css/style.css" />
    <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
 
 </head>
<body>
	<header id="header" class="site-header" role="banner">
    <div id="header-inner" class="container sixteen columns over">
    <hgroup class="one-third column alpha">
    <h1 id="site-title" class="site-title">
    <a id="logo"><img src="images/metrec.jpg" alt="Phylopro logo" height="63" width="157" /></a>
    </h1>
    </hgroup>
    <nav id="main-nav" class="two thirds column omega">
    <ul id="main-nav-menu" class="nav-menu">
    <li id="menu-item-1" class="current">
    <a href="index.html">Home</a>
    </li>
    <li id="menu-item-2">
    <a href="organisms.jsp">Organisms</a>
    </li>
    <li id="menu-item-3">
    <a href="faqs.html">FAQs</a>
    </li>
    <li id="menu-item-4">
    <a href="help.html">Help</a>
    </li>
    </ul>
    </nav>
    </div>
    </header><div id="site_content"><div id="content"><div class="content_item">
"""
    print chebiids[i]
    print pubchemids[i]
    html_file.write("<table>")
    #KEGG ID
    if keggid.match(metrecid[i]):
        html_file.write("""<tr><td>KEGG ID:<a href="http://www.genome.jp/dbget-bin/www_bget?%s"  target="_blank">%s</a></td></tr>"""  % (metrecid[i],metrecid[i]))
    else:
        html_file.write("<tr><td>Metrec ID:%s</td></tr>"  % (metrecid[i]))
    #Full Name
    html_file.write("<tr><td>Full Name:%s</td></tr>"  % (fullname[i]))
 
    #Chebi ID
    if chebiids[i]=="0":
        html_file.write("<tr><td>Chebi ID: </td></tr>")
    else:
        html_file.write("""<tr><td>Chebi ID:<a href="http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:%d"  target="_blank">%s</a></td></tr>""" % (chebiids[i],chebiids[i]))
    #Pubchem CID
    if pubchemids[i]=="0":
        html_file.write("<tr><td>Pubchem CID: </td></tr>")
    else:
        html_file.write("""<tr><td>PubChem CID:<a href="http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=%d"  target="_blank">%s</a></td></tr>"""  % (pubchemids[i],pubchemids[i])) 
    #Pubchem SID
    if pubchemsids[i]=="0":
        html_file.write("<tr><td>Pubchem SID: </td></tr>")
    else:
        html_file.write("""<tr><td>PubChem SID:<a href="http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?sid=%d"  target="_blank">%s</a></td></tr>"""  % (pubchemsids[i],pubchemsids[i]))     

    html_file.write("</table></div><!--close content_item--></div><!--close content--></div><!--close site_content--> </body></html>")
    html_file.close()
    

    



