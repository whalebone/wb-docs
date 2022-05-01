Resolver agent
===================

Command line interface
-----------------------
Agent's actions can be invoked using a proxy bash script present at path **/var/whalebone/cli/cli.sh**. This script calls a python script which handles the execution of the following agent actions: 

* **sysinfo** - returns the system status data in JSON format.
	* Parameters: None
	* Output: tested categories on tested key can have two values 'ok' and 'fail'

.. sourcecode:: js

	{
	   "hostname":"hostname",
	   "system":"Linux",
	   "platform":"CentOS Linux 7 (Core)",
	   "cpu":{
	      "count":4,
	      "usage":28.6
	   },
	   "memory":{
	      "total":7.6,
	      "available":3.9,
	      "usage":49.2
	   },
	   "hdd":{
	      "total":50.0,
	      "free":14.4,
	      "usage":71.1
	   },
	   "swap":{
	      "total":0.0,
	      "free":0.0,
	      "usage":0
	   },
	   "resolver":{
	      "answer.nxdomain":3284,
	      "answer.tc":35,
	      "answer.ad":849,
	      "answer.100ms":3983,
	      "answer.cd":6,
	      "answer.1500ms":74,
	      "answer.slow":215,
	      "answer.rd":224337,
	      "answer.1ms":104683,
	      "answer.servfail":215,
	      "predict.epoch":24,
	      "query.dnssec":6,
	      "answer.250ms":14941,
	      "query.edns":35498,
	      "answer.cached":86713,
	      "answer.nodata":3622,
	      "answer.aa":2362,
	      "answer.do":6,
	      "answer.edns0":35498,
	      "answer.ra":224337,
	      "predict.queue":0,
	      "answer.total":224337,
	      "answer.10ms":35351,
	      "answer.noerror":217216,
	      "answer.50ms":59766,
	      "answer.500ms":4642,
	      "answer.1000ms":653,
	      "predict.learned":80
	   },
	   "docker":{
	      "Platform":{
	         "Name":""
	      },
	      "Components":[
	         {
	            "Name":"Engine",
	            "Version":"17.12.1-ce",
	            "Details":{
	               "ApiVersion":"1.35",
	               "Arch":"amd64",
	               "BuildTime":"2022-02-27T22:17:54.000000000+00:00",
	               "Experimental":"false",
	               "GitCommit":"88888fc6",
	               "GoVersion":"go1.999.999",
	               "KernelVersion":"3.22.66-693.21.1.el7.x86_64",
	               "MinAPIVersion":"1.99",
	               "Os":"linux"
	            }
	         }
	      ],
	      "Version":"19.32.1-ce",
	      "ApiVersion":"1.98",
	      "MinAPIVersion":"1.12",
	      "GitCommit":"7390fc6",
	      "GoVersion":"go1.9.4",
	      "Os":"linux",
	      "Arch":"amd64",
	      "KernelVersion":"3.10.0-693.21.1.el7.x86_64",
	      "BuildTime":"2018-02-27T22:17:54.000000000+00:00"
	   },
	   "check":{
	      "resolve":"ok",
	      "port":"ok"
	   },
	   "containers":{
	      "lr-agent":"running",
	      "passivedns":"running",
	      "resolver":"running",
	      "kresman":"running",
	      "pcpy":"running",
	      "logrotate":"running",
	      "logstream":"running"
	   },
	   "images":{
	      "lr-agent":"whalebone/agent:1.1.1",
	      "passivedns":"whalebone/passivedns:1.1.1",
	      "resolver":"whalebone/kres:1.1.1",
	      "kresman":"whalebone/kresman:1.1.1",
	      "logrotate":"whalebone/logrotate:1.1.1",
	      "logstream":"whalebone/logstream:1.1.1"
	   },
	   "error_messages":{
	   },
	   "interfaces":[
	      {
	         "name":"lo",
	         "addresses":[
	            "127.0.0.1",
	            "::1",
	            "00:00:00:00:00:00"
	         ]
	      },
	      {
	         "name":"eth0",
	         "addresses":[
	            "1.1.1.1",
	            "::c8",
	            "fe80::",
	            "00:00:00:00:00:00"
	         ]
	      },
	      {
	         "name":"docker0",
	         "addresses":[
	            "198.1.1.1",
	            "00:00:00:00:00:00"
	         ]
	      }
	   ]
	}


* **stop** - stops up to three containers 
	* Parameters: containers to stop (up to 3), Example: ./cli.sh stop resolver lr-agent kresman
	* Output: 

.. sourcecode:: js

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **remove** - removes up to three containers
	* Parameters: containers to remove (up to 3), Example: ./cli.sh remove resolver lr-agent kresman
	* Output: 

.. sourcecode:: js

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **upgrade** - upgrades up to three containers, the container's configuration is specified by a docker-compose in agent container (can also be found in a volume **/etc/whalebone/agent**)
	* Parameters: containers to upgrade (up to 3), Example: ./cli.sh upgrade resolver lr-agent kresman
	* Output: 

.. sourcecode:: js 

	{
		'resolver': {'status': 'success'}, 
		'lr-agent': {'status': 'success'}, 
		'kresman': {'status': 'success'}
	}
	
* **create** - creates containers, the containers are specified by a docker-compose in agent container (can also be found in **/etc/whalebone/agent**)
	* Parameters: None, Example: ./cli.sh create
	* Output: 

.. sourcecode:: js

	{'resolver': {'status': 'success'}
	

	Pending configuration request deleted.
	
* **updatecache** - forces the update of resolver's IoC cache (which is used for blocking), this action should be done to manually force the update and refresh of the domains present in the malicous domain cache
	* Parameters: None
	* Output: 

.. sourcecode:: js

	{'status': 'success', 'message': 'Cache update successful'}
	
* **containers** - lists the containers and their information which include: labels, image, name and status. 
	* Parameters: None
	* Output: 

.. sourcecode:: js

	[
	   {
	      "id":"b8f4489379",
	      "image":{
	         "id":"c893b4df5ca3",
	         "tags":[
	            "whalebone/agent:1.1.1"
	         ]
	      },
	      "labels":{
	         "lr-agent":"1.1.1"
	      },
	      "name":"lr-agent",
	      "status":"running"
	   },
	   {
	      "id":"e433d58f13",
	      "image":{
	         "id":"2c4b84a7daee",
	         "tags":[
	            "whalebone/passivedns:1.1.1"
	         ]
	      },
	      "labels":{
	         "passivedns":"1.1.1"
	      },
	      "name":"passivedns",
	      "status":"running"
	   },
	   {
	      "id":"2aeec00121",
	      "image":{
	         "id":"fc442e625539",
	         "tags":[
	            "whalebone/kres:1.1.1"
	         ]
	      },
	      "labels":{
	         "resolver":"1.1.1"
	      },
	      "name":"resolver",
	      "status":"running"
	   },
	   {
	      "id":"662dac2e6c",
	      "image":{
	         "id":"b37d0d1bd10b",
	         "tags":[
	            "whalebone/kresman:1.1.1"
	         ]
	      },
	      "labels":{
	         "kresman":"1.1.1"
	      },
	      "name":"kresman",
	      "status":"running"
	   },
	   {
	      "id":"05188ac1df",
	      "image":{
	         "id":"5b50cdc924fc",
	         "tags":[
	            "whalebone/logrotate:1.1.1"
	         ]
	      },
	      "labels":{
	         "logrotate":"1.1.1"
	      },
	      "name":"logrotate",
	      "status":"running"
	   },
	   {
	      "id":"01e64dd697",
	      "image":{
	         "id":"fffb52c2dadd",
	         "tags":[
	            "whalebone/logstream:1.1.1"
	         ]
	      },
	      "labels":{
	         "logstream":"1.1.1"
	      },
	      "name":"logstream",
	      "status":"running"
	   }
	]


Each of those actions execute similarly named actions and the status of that action, or output of that action, is printed. The **list** and **run** actions are intended for the scenario when a confirmation of a certain action is required. The action list shows the action that should be executed and the changes that would be done by that action for containers specified in that action. This serves as an example of what would happen if the awaiting action would have been executed. The run action then executes the awaiting action and cleans up afterwards. 

The actions of upgrade and create use the docker-compose template present in the agent container to create/upgrade the desired container. This template is mounted in the volume **/etc/whalebone/agent** if the user decides to change it. However this change needs to be done also to the template present at **portal.whalebone.io**, if not than the local changes will be overwritten from the cloud during next upgrade. 

The bash script should be invoked like this: ``./cli.sh action param1 param2 param3``. Action is the action name and parameters are the action parameters. Only actions for container stop, remove and upgrade use these and specify what containers should be affected by the respective action.

Strict mode
------------------
The agent's default option is to execute actions from the cloud management immediately. It is however possible to enable manual confirmation of requests. This gives the administrator control over when and what gets executed. To enable the resolver Strict mode, please create a ticket to Whalebone support.

To list changes the request introduces the cli option **list** option should be used. To execute the request use cli option **run**. There can only be one  request pending in the queue. New request from the cloud will ovewrite the previous one, but the new one holds the full desired state anyway. To delete waiting request use cli option **delete_request**. The actions that can be persisted are: **upgrade**, **create** and **suicide**. Please see examples of the CLI command usage.

* **list** - lists the awaiting command and the changes that would be made to the containers specified in the awaiting action, this action is intended for human check hence it's format 
	* Parameters: None, Example: ./cli.sh list
	* Output: 

.. code-block:: lua

	-------------------------------
	Changes for resolver
	New value for label: resolver-1.1.1
	
	  	Old value for label: resolver-1.0.0
	-------------------------------
	
* **run** - executes the awaiting command
	* Parameters: none, Example: ./cli.sh run

.. sourcecode:: js

	{'resolver': {'status': 'success'}

* **delete_request** - deletes the awaiting request
	* Parameters: none, Example: ./cli.sh delete_request

.. code-block:: lua

	Pending configuration request deleted.

