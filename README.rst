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


Show Help for command

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


1. Show Help for `Create Volume Backup`

#. Create Volume Backup

    $ openstack volume backups create volume-4a59 --name bakup-qianbiao-1 --description=QianBiao-Test-purpose
        --os-vb-endpoint-override=https://vbs.eu-de.otc.t-systems.com

#. Show volume backup job

    # show volume backup job
    $ openstack volume backups job show 2c9eb2c159b48597015a0d4fe9e440a6 --os-vb-api-version=1
        --os-vb-endpoint-override=https://vbs.eu-de.otc.t-systems.com
    +------------+-----------------------------------------------------------------------------------------------------------------------+
    | Field      | Value                                                                                                                 |
    +------------+-----------------------------------------------------------------------------------------------------------------------+
    | Id         | 2c9eb2c159b48597015a0d4fe9e440a6                                                                                      |
    | Type       | bksCreateBackup                                                                                                       |
    | Begin Time | 2017-02-05T08:07:05.443Z                                                                                              |
    | End Time   | 2017-02-05T08:11:13.702Z                                                                                              |
    | entities   | backup_id='d86a3759-7f55-4d02-929b-045cdc17b505', bks_create_volume_name='autobk_volume_2017-02-05T08:07:18.787Z',    |
    |            | snapshot_id='97b86b2b-1928-4186-8864-24814dae5af0', volume_id='abd4b550-8857-4615-900a-cc25845d74d5'                  |
    | Status     | SUCCESS                                                                                                               |
    +------------+-----------------------------------------------------------------------------------------------------------------------



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
