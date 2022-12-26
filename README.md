<body lang=EN-GB style='tab-interval:36.0pt;word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:20.0pt;line-height:107%'>Web scraping with Google Shopping
search<o:p></o:p></span></b></p>

<p class=MsoNormal><o:p>&nbsp;</o:p></p>

<p class=MsoNormal><b>Business need:</b> Get ecommerce competitors’ data on Google
Shopping searches.</p>

<p class=MsoNormal><b>Proposed solution</b>: A Python script that can retrieve
and save in a CSV the data coming from the Google Shopping search queries. </p>

<p class=MsoNormal><b>Possible next implementations</b>: Run with a VM these
functions in a loop for different products and save the extracted data into an
SQL server.</p>

<p class=MsoNormal><b>Code prerequisites</b>: Python (I used the version 3.10) ,
Selenium, Pandas, <span class=SpellE>Webbrowser</span> packages installed,
Chromium extension and Chrome installed.</p>

<p class=MsoNormal><b>Code limitation: </b>Most of the elements are searched on
the HTML by Class. This may be risky in case of Class changes from Google body.
</p>

<p class=MsoNormal><b><o:p>&nbsp;</o:p></b></p>

</div>

</body>
