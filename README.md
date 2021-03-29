[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-mail.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-mail)


Mail
====

Mail server role


Role Variables
--------------

`mail_domain` - Mail domain being configured
`mail_forwarding` - List of `source`/`target` pairs.  `source` emails are forwarded to `target`


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    mail_domain: example.com
    mail_forwarding:
      - source: test1@example.com
        target: test1@fake.com
      - source: test2@example.com
        target: test2@fake.com
  include_role:
    name: "ansible-mail"
```

License
-------

MIT

