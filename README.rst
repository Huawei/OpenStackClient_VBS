python-antiddosclient
=====================

This is a `OpenStack Client`_ plugin for HuaWei Cloud-Eye Management API which
provides **command-line scripts** (integrated with openstack) and Python library for
accessing the Cloud-Eye management API.


Installation
------------
Currently, We can install the plugin from source code

.. code:: console

  git clone https://github.com/Huawei/OpenStackClient_CES python-cloudeyeclient
  cd python-cloudeyeclient
  python setup.py install


Command Line Client Usage
-----------------------------------------

.. note::

    The command line client is self-documenting. Use the --help or -h flag to access the usage options.
    You can find more command line client examples `here <./commands.rst>`_


This plugin is integrated with `OpenStack Client`_ , so the command line client
follow all the usage **openstack** provided.

.. code:: console

    $ openstack --help
    usage: openstack [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                 [--os-cloud <cloud-config-name>]
                 [--os-region-name <auth-region-name>]
                 [--os-cacert <ca-bundle-file>] [--os-cert <certificate-file>]
                 [--os-key <key-file>] [--verify | --insecure]
                 [--os-default-domain <auth-domain>]
                 [--os-interface <interface>] [--timing] [--os-beta-command]
                 [--os-profile hmac-key]
                 [--os-compute-api-version <compute-api-version>]
                 [--os-network-api-version <network-api-version>]
                 [--os-image-api-version <image-api-version>]
                 [--os-volume-api-version <volume-api-version>]
                 [--os-identity-api-version <identity-api-version>]
                 [--os-object-api-version <object-api-version>]
                 [--os-queues-api-version <queues-api-version>]
                 [--os-clustering-api-version <clustering-api-version>]
                 [--os-search-api-version <search-api-version>]
                 .......


Cloud-Eye-Service Client contains commands list in table below, use -h option to get more useage

+----------------------+
| command              |
+======================+
| metric list          |
+----------------------+
| metric favorite list |
+----------------------+
| metric data list     |
+----------------------+
| metric data create   |
+----------------------+
| alarm list           |
+----------------------+
| alarm show           |
+----------------------+
| alarm enable         |
+----------------------+
| alarm disable        |
+----------------------+
| alarm delete         |
+----------------------+
| quota list           |
+----------------------+




.. code:: console

    # use help command 
    $ openstack metric list -h
    usage: openstack metric list [-h] [-f {csv,json,table,value,yaml}] [-c COLUMN]
                                [--max-width <integer>] [--print-empty]
                                [--noindent]
                                [--quote {all,minimal,none,nonnumeric}]
                                [--namespace {SYS.ECS,SYS.EVS,SYS.AS,SYS.ELB,SYS.VPC,SYS.RDS,SYS.WAF,SYS.HVD}]
                                [--metric-name <metric-name>]
                                [--dimensions <key=value>] [--start <key=value>]
                                [--limit <count>] [--order {desc,asc}]

    list metrics

    optional arguments:
    -h, --help            show this help message and exit
    --namespace {SYS.ECS,SYS.EVS,SYS.AS,SYS.ELB,SYS.VPC,SYS.RDS,SYS.WAF,SYS.HVD}
                            list metric with namespace
    --metric-name <metric-name>
                            list metric with name(example: cpu_utils)
    --dimensions <key=value>
                            Metric dimension (repeat to set multiple dimension,
                            max repeat time is 3)
    --start <key=value>   return result list start from (namespace.metric-
                            name.key:value)
    --limit <count>       return result limit, max size is 1000
    --order {desc,asc}    Sort by, default is desc

    output formatters:
    output formatter options

    -f {csv,json,table,value,yaml}, --format {csv,json,table,value,yaml}
                            the output format, defaults to table
    -c COLUMN, --column COLUMN
                            specify the column(s) to include, can be repeated

    table formatter:
    --max-width <integer>
                            Maximum display width, <1 to disable. You can also use
                            the CLIFF_MAX_TERM_WIDTH environment variable, but the
                            parameter takes precedence.
    --print-empty         Print empty table if there is no data to show.

    json formatter:
    --noindent            whether to disable indenting the JSON

    CSV Formatter:
    --quote {all,minimal,none,nonnumeric}
                            when to include quotes, defaults to nonnumeric



.. code:: console

    # list metric 
    $ openstack metric list --namespace=SYS.VPC --metric-name=up_bandwidth
        --start=SYS.VPC.up_bandwidth.bandwidth_id:a6e74b9d-e2c8-4bf8-85a2-cc78a04c6cb4
        --os-cloudeye-endpoint-override=https://ces.eu-de.otc.t-systems.com
    +-----------+--------------+---------------------------------------------------+--------+
    | Namespace | Metric Name  | Dimension                                         | Unit   |
    +-----------+--------------+---------------------------------------------------+--------+
    | SYS.VPC   | up_bandwidth | bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4 | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=74cf708f-9c1e-4f32-bd83-9b945dfe9434 | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=59ab20fd-53c8-44ce-ba03-19dc2f6f038f | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=38d50758-da39-4d3f-9ee0-9bd78050f682 | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=1d101781-c5ca-47f2-a848-dab03ad341f3 | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=1607470e-8542-40a6-a826-a3e3affff2fc | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=13b617cd-459c-4351-87a7-ed85e9e59f9d | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=0c2d5910-55ad-4406-8ee5-fed14a76d0c3 | Byte/s |
    | SYS.VPC   | up_bandwidth | bandwidth_id=0082ecc5-a7f4-47c2-9196-6fefb4394019 | Byte/s |
    +-----------+--------------+---------------------------------------------------+--------+

    $ openstack metric list --dimensions=bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4
    +-----------+----------------+---------------------------------------------------+--------+
    | Namespace | Metric Name    | Dimension                                         | Unit   |
    +-----------+----------------+---------------------------------------------------+--------+
    | SYS.VPC   | up_bandwidth   | bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4 | Byte/s |
    | SYS.VPC   | down_bandwidth | bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4 | Byte/s |
    +-----------+----------------+---------------------------------------------------+--------+



Python Library Usage
-------------------------------

The full api is documented in the `CloudEye Offical Document`_ site

Here's an example of listing antiddos status using Python library with keystone V3 authentication:

.. code:: python

    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from vbclient.v2 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Cloud Eye API
    >>> # Let's try list metric API
    >>> client.metric_mgr.list(namespace='SYS.VPC')
    [<Metric namespace=SYS.VPC ....>, ....]




    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from vbclient.v2 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Cloud Eye API
    >>> # Let's try list metric API
    >>> client.metric_mgr.list(namespace='SYS.VPC')
    [<Metric namespace=SYS.VPC ....>, ....]




    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from vbclient.v1 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Cloud Eye API
    >>> # Let's try list metric API
    >>> client.metric_mgr.list(namespace='SYS.VPC')
    [<Metric namespace=SYS.VPC ....>, ....]


.. note::

    The example above must be running and configured to use the Keystone Middleware.

    For more information on setting this up please visit: `KeyStone`_


* License: Apache License, Version 2.0
* `OpenStack Client`_
* `CloudEye Offical Document`_
* `KeyStone`_

.. _OpenStack Client: https://github.com/openstack/python-openstackclient
.. _CloudEye Offical Document: http://support.hwclouds.com/ces/
.. _KeyStone: http://docs.openstack.org/developer/keystoneauth/
