import mechanize

br = mechanize.Browser()

#email form data
to = raw_input("Enter the recipient address: ")
subject = raw_input ("Enter Subject Line: ")
print("Body")
message = raw_input(">")

#proxy = "http://127.0.0.1:8080"

url = "http://anonymouse.org/anonemail.html"
headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
br.addheaders = [('User-agent', headers)]
br.open(url)
br.set_handle_equiv(True)
br.set_handle_qzip(True)
br.set_handlle_redirect(True)
br.set_handle_robots(False)
br.set_handle_robots(False)
br.set_degbug_http(False)
#br.set_proxies({"http": proxy})

br.select_form(nr=0)

br.form['to'] = to
br.form['subject'] = subject
br.form['text'] = message

result = br.submit()

response = br.response().read()