# API with two endpoints 
## Test case

API (aiohttp, async peewee, marshmallow)

### API Endpoints

#### List of endpoints

* **/api/v1/list_pages** (Endpoint for list of pages with only name and url)
* **/api/v1/page/{page_id}** (Endpoint for list of all information of blocks py page id)

Notice that you need python 3.8 or higher
Clone repo at first.

### Install (for UNIX/MAC OS)
    pip3 install virtualenv
    mkdir path/to/project
    cd path/to/project
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
### Usage
  python -m aiohttp.web -H localhost -P 8080 app.server:make_app

