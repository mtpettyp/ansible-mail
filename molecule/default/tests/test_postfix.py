

"""Role testing Postfix using testinfra."""


def test_services(host):
    """Validate that Postfix is configured correction """
    main_cf = host.file("/etc/postfix/main.cf")

    assert main_cf.contains("myhostname = example.com")
    assert main_cf.contains("virtual_alias_domains = example.com")

    virtual = host.file("/etc/postfix/virtual")
    assert virtual.exists
    assert virtual.contains("test1@example.com test1@fake.com")
    assert virtual.contains("test2@example.com test2@fake.com")

    virtual = host.file("/etc/postfix/virtual.db")
    assert virtual.exists
