Welcome to DS_Project Fraud's documentation!
============================================

This is the documentation of our mockup project for the datascientest
certification in data engineering. For now, you'll find a summary of
included modules and a diagram showing the process.

.. figure:: /ds_project_fraud.drawio.png

   *processflow of a transaction that is asking for a classification*

.. toctree::
   :maxdepth: 2

    Html <ds_project.html.rst>
    Model <ds_project.model.rst>
    Data <ds_project.data.rst>

Main
====
	Starting point for complete Fraud API is main.py (root folder).
		**Include:**

		- Fastapi modules: FastApi,Request,Depends,HTMLResponse,Jinja2Templates,StaticFiles.
		- Python modules: datetime,
		- Fraud modules (see in DATA and MODEL)