import webbrowser
files = open('index.html', 'w')
code = """<html lang='en'>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width'>
<meta http-equiv='X-UA compatible' content='IE-edge'>
<title>Writing html using python</title>
</head>
<body>
<p>this is a simple test of how to write html using python and loading it on the browser</p>
</body>
</html>"""
files.write(code)
files.close()
webbrowser.open('index.html')
