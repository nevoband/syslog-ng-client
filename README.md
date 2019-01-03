Role Name
=========

Installs the syslog-ng in client mode on a client host with mutual authentication

Requirements
------------



Role Variables
--------------

Example:
````yml
#Centralized Logging settings
syslogng_cert_data: "{{ vault_syslogng_cert_data }}"
syslogng_key_data: "{{ vault_syslogng_key_data }}"
syslogng_cert_force_replace: true
syslogng_server_dn: "foo.example.uic.edu"
````

**Other Options:**

Path/permission for certificates:
````yml
syslogng_ca_path: '/etc/syslog-ng/ca.d'
syslogng_cert_path: '/etc/syslog-ng/cert.d'
syslogng_certs_path_owner: "root"
syslogng_certs_path_group: "root"
syslogng_cert_mode: "0700"
````

File names of certificates/key:
````yml
syslogng_ca_file: "cacert.pem"
syslogng_cert_file: "clientcert.pem"
syslogng_key_file: "clientkey.pem"
````

Certificate and Key, should be saved in Ansible vault and linked see example above
````yml
syslogng_ca_data: ""
syslogng_cert_data: ""
syslogng_key_data: ""
````
Server Domain Name, IP and Protocol:
````yml
syslogng_server_dn: ""
syslogng_server_port: "6514"
syslogng_server_protocol: "tcp"
````

Extra log files to monitor:
````yml
log_files:
  - path: "/var/log/httpd/access_log"
    program: "apache-access"
  - path: "/var/log/httpd/error_log"
    program: "apache-error"
  - path: "/var/log/httpd/ssl_access_log"
    program: "apache-ssl-access"
  - path: "/var/log/httpd/ssl_error_log"
    program: "apache-ssl-error"
````

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: syslog-ng-client }

License
-------

BSD
