# Shortcut for odoo-bin
***
## Description

This program is good enough to run the odoo server for all structures right now. The program's goal is to allow projects to have many versions; for instance, a project may have a version shift from 13 to 17, etc. Thus, the developer **finds** the project directory, **needs to activate** the python environment that is reliable for Odoo version, then **_resets and restarts_** the server. The program can reduce your time; just configure your customized settings in [```settings.py```](https://github.com/XharonX/odoo-dev/blob/main/settings.py)


### Default Project Structure
```
ODOO DEFAUT ROOT            :   /home/username/.odoo/
Projects DIR                :   /home/username/Projects/Odoo/{project_name}
Python Environment Path     :   /home/username/pyenv/env{version}
Odoo Configuration file     :   /home/username/Projects/Odoo/{project_name}/config/odoo{version}.conf


```

### Man Page for dev_odoo.py
```bash
options:
  -h, --help            show this help message and exit
  -v {13,16,17}, --version {13,16,17}
                        odoo version (default == 17)
  -p {will,show,the,list,of,projects}, --project {will,show,the,list,of,projects}
                        ODOO Project Directory Name
  -u UPGRADE, --upgrade UPGRADE
                        To upgrade modules
  -d DATABASE, --database DATABASE
                        Select the database
  -s, --shell           Odoo Shell

```
***

### Bash Shell (Linux)
```bash
    $ chmod +x odoo_dev/run
    $ odoo_dev/run -p project_name -u upgrade_module # to run default odoo version
    $ odoo_dev/run -v version -p project_name -d database -u upgrade_module -s # odoo shell
```
***
### Python and Windows users
```bash
    $ python3 odoo_dev/run -v version -p project_name -d database -u upgrade_module -s 
    $ python3 odoo_dev/run -v version -p project_name -d database -u upgrade_module
```

