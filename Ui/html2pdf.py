import pdfkit
pdfkit.from_string('Hello!','out.pdf')



def html2pdf():
    options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [('Accept-Encoding', 'gzip')],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None,
    'quiet': ''
}
    body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      <body>
<table width="800" border="1">
  <tbody>
    <tr>
      <th scope="col" width="150">Items</th>
      <th scope="col">Sample1</th>
      <th scope="col">Sample2</th>
      <th scope="col">Sample3</th>
    </tr>
    <tr>
      <th scope="row">Sample Name</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th scope="row">Material Type</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th scope="row">Chemistry Type</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

      </body>
      </html>
    """

    pdfkit.from_string(body, 'out.pdf',options=options) #with --page-size=Legal and --orientation=Landscape
    #pdfkit.from_url('http://google.com', 'out.pdf', options=options)
if __name__=="__main__":
    html2pdf()
