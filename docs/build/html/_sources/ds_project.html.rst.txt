ds\_project.html package
========================

Display part via http.

.. toctree::
  :titlesonly:


Tree
-------
	+ html
		+ static
			- check.png
			- info.png
			- jquery-3.5.0.min.js
			- style.css
			- support.png
			- uncheck.png

		+ templates
			- form.html
			- response.html

	- schemas.py
	- attack.py


:Reminder: Entry point for Fraud Dectection is main.py (root folder). It will display form.html, manage submit, modules and response.

Python
------
	- schemas.py
		**Include Class WebForm**
			- signup_time: str
			- purchase_value: int
			- purchase_time: str
			- device_id: str
			- source: str
			- browser: str
			- sex: str
			- age: int
			- ip_address: str "


	- attack.py
		**Injection loop (4X) on FastApi url.**
			- urldata: Server + port /form
			- data: *(Data manually choice)*
				- 'signup_time':'',
				- 'purchase_value':'',
				- 'purchase_time':'',
				- 'device_id':'',
				- 'source':'',
				- 'browser':'',
				- 'sex':'',
				- 'age':'5',
				- 'ip_address':''


Templates
---------

	**form.html**
			Template base on Jinja2Templates. Use for Get action.

	**response.html**
			Template base on Jinja2Templates. Use for Post action.


App
---
	- @app.get("/form", response_class=HTMLResponse)
		- Initialisation variables for form.html
		- Render template form.


	- @app.post('/form', response_class=HTMLResponse)
		- Reception of submit data from form.html
		- Call all process modules in MODEL folder
		- Render template response. (Fraud or not)

Variables
---------

	- trns_dict =
		  -'raw':
			 - 'signup_time':datetime.strptime(form_data.signup_time,'%d/%m/%Y %H:%M:%S'),
			 - 'purchase_time':datetime.strptime(form_data.purchase_time,'%d/%m/%Y %H:%M:%S'),
			 -  'purchase_value':form_data.purchase_value,
			 - 'device_id':form_data.device_id,
			 - 'source':form_data.source,
			 - 'browser':form_data.browser,
			 - 'sex':form_data.sex,
			 - 'age':form_data.age,
			 - 'ip_address':form_data.ip_address


	- purchase_date = Date Now.
	- data = Request submit datas.













