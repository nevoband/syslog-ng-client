import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
  ("/etc/syslog-ng/ca.d/cacert.pem", "Certificate Authority"),
  ("/etc/syslog-ng/cert.d/clientcert.pem", "Domain Name Certificate"),
  ("/etc/syslog-ng/cert.d/clientkey.pem", "Private Key"),
  ("/etc/syslog-ng/syslog-ng.conf", "Managed by Ansible"),

])
def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
