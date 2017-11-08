#!/usr/bin/env python
from ansible.module_utils.basic import *

class Linux(object):
	platform = 'Generic'
	distribution = None
 
	def __new__(cls, *args, **kwargs):
		return load_platform_subclass(Linux, args, kwargs)
 
	def name(self):
		return self.distribution if self.distribution else self.platform

class Debian(Linux):
	platform = 'Linux'
	distribution = 'Debian'

class OSX(Linux):
	platform = 'Darwin'
	distribution = None

module = AnsibleModule(
	argument_spec = dict(
		command = dict(required=True)
	)
)
module.log("start")
linux = Linux()

command = module.params['command']
rc, stdout, stderr = module.run_command(command)
module.exit_json(
	changed=True,
	rc=rc,
	stdout=stdout,
	stderr=stderr, msg=linux.name()
)
module.log("end")
