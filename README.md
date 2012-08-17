python-scim
===========
_A python interface to produce and consume System for Cross-domain Identity Management (SCIM) messages_.

Features
--------
 - __SCIM conformance__ <br />
   python-scim conforms to the latest SCIM standards.

 - __Environment agnostic__ <br />
   python-scim may be used to produce and consume SCIM messages regardless
   of the environment (terminal, WSGI, django) used to call it.

Dependencies
------------
### Build

### Runtime
 - __[lxml][]__ <br />
   The lxml library is used for consuming and producing SCIM messages
   as XML.

 - __[requests][]__ <br />
   The requests library is used to make outgoing requests to a SCIM endpoint

[lxml]: http://pypi.python.org/pypi/lxml/
[requests]: http://pypi.python.org/pypi/requests/

License
-------
Unless otherwise noted, all files contained within this project are liensed
under the MIT opensource license. See the included file LICENSE or visit
[opensource.org][] for more information.

[opensource.org]: http://opensource.org/licenses/MIT
