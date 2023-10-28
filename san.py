from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<title> jungook </title>
<body>
<table border="2">
	<caption> Top five revenue generating software companinies </caption>

	<tr>
		<th> S.no </th>
		<td> 1 </td>
		<td> 2 </td>
		<td> 3 </td>
		<td> 4 </td>
		<td> 5 </td>
	</tr>

	<tc>
		<th> Company </th>
		<td> Mircrosoft </td>
		<td> Oracle </td>
		<td> IBM </td>
		<td> SAP </td>
		<td> Symantec </td>
	</tr>


	<tr>
		<th> Revenue </th>
		<td> 65 Billion </td>
		<td> 29.6 Billion </td>
		<td> 29.1 Billion </td>
		<td> 6.4 Billion </td>
		<td> 5.6 Billion </td>
	</tr>
</body>
</table>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()