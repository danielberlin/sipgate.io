sipgate.io
==========

This README documents the sipgate.io functionality. A demo page can be found [here](https://demo.sipgate.io).

Requirements
------------

* [x] [Order a simquadrat SIM](https://www.simquadrat.de)
* [x] [Book the sipgate.io feature](https://www.simquadrat.de/feature-store/sipgate.io)
* [x] [Enter your URL in the simquadrat dashboard](https://www.simquadrat.de/dashboard)



The POST request
================

sipgate.io sends a simple POST request with an `application/x-www-form-urlencoded` payload. The request contains the following parameters:

Parameter | Description
--------- | -----------
from      | The calling number (e.g. `"492111234567"` or `"anonymous"`)
to        | The called number (e.g. `"4915791234567"`)

That's all!

You can simulate this POST request and test your server with a simple cURL command:

```sh
curl -X POST --data "from=492111234567&to=4915791234567" http://localhost:3000
```

The XML response
============
After sending the POST request sipgate.io will accept an XML response to determine what to do. Make sure to set ```application/xml``` in the ```Content-Type``` header of your response and you are ready to go!

sipgate.io currently supports the following responses:

Action            | Description
----------------- | -----------
[Reject](#reject) | Reject call or pretend to be busy

Reject
------

Pretend to be busy or block unwanted calls. 

Possible attributes | Possible values | Default value
------------------- | --------------- | -------------
reason              | rejected, busy  | rejected


**Example 1: Reject call**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
        <Reject />
</Response>
```

**Example 2: Reject call signaling busy**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
        <Reject reason="busy" />
</Response>
```

More to come
------------
Stay tuned...



Server Examples
===============

We compiled a collection of server examples to get you started:

* [C++](https://github.com/sipgate/sipgate.io/tree/master/examples/c++)
* [Clojure](https://github.com/sipgate/sipgate.io/tree/master/examples/clojure)
* [Common Lisp](https://github.com/sipgate/sipgate.io/tree/master/examples/commonlisp)
* [Go](https://github.com/sipgate/sipgate.io/tree/master/examples/go)
* [Java](https://github.com/sipgate/sipgate.io/tree/master/examples/java)
* [Node.js](https://github.com/sipgate/sipgate.io/tree/master/examples/nodejs)
* [PHP](https://github.com/sipgate/sipgate.io/tree/master/examples/php)
* [Perl](https://github.com/sipgate/sipgate.io/tree/master/examples/perl)
* [Prolog](https://github.com/sipgate/sipgate.io/tree/master/examples/prolog)
* [Python](https://github.com/sipgate/sipgate.io/tree/master/examples/python)
* [Ruby](https://github.com/sipgate/sipgate.io/tree/master/examples/ruby)
* [Scala](https://github.com/sipgate/sipgate.io/tree/master/examples/scala)



Troubleshooting
===============

sipgate.io Log
--------------

You can enable logging for debugging purposes from your simquadrat dashboard. You will find each request and the corresponding response in the logging table.

How do I inspect network traffic?
---------------------------------

You can use ```ngrep``` to inspect the incoming requests on your side:
```sh
sudo ngrep -dany -Wbyline port 3000
```



A word about security
=====================

HTTP vs. HTTPS
--------------

We strongly encourage you to use a HTTPS server. Although we support plain HTTP connections we do not recommend pushing sensitive call details over unencrypted connections. By default sipgate.io does not accept [self-signed certificates](http://stackoverflow.com/a/10176685), but you can allow them in the simquadrat dashboard.

Authentication
--------------

sipgate.io supports HTTP Basic Authentication. You can include your username and password within the URL (e.g. `https://username:password@example.com:8080`).



Help us make it better
======================

Please tell us how we can improve sipgate.io. If you have a specific feature request, found a bug or would like to add an example, please use [GitHub Issues](https://github.com/sipgate/sipgate.io/issues) or fork these docs and send a [pull request](https://github.com/sipgate/sipgate.io/pulls) with your improvements.
