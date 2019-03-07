import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rkhunter_is_installed(host):
    package = host.package("rkhunter")
    assert package.is_installed
    assert package.version.startswith("1.4")


def test_rkhunter_is_check_successful(host):
    assert host.run_test("rkhunter --check --sk --rwo")
