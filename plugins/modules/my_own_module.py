#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: This is the path of file.
        required: true
        type: str
    content:
        description:
            - Content of the file.
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@belas80)
'''

EXAMPLES = r'''
# Cteate file with default content
- name: Test with a message
  belas80.my_own_collection.my_own_module:
    path: ./sample_file.txt

# pass contents to file
- name: Test with contents
  belas80.my_own_collection.my_own_module:
    path: ./sample_file.txt
    content: "some one content"

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'File created'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File created'
'''
from os import stat
from ansible.module_utils.basic import AnsibleModule

def file_exist(path):
    try:
        stat(path)
        return False
    except FileNotFoundError:
        return True

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='some content')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        result['changed'] = file_exist(module.params['path'])
        module.exit_json(**result)

    if file_exist(module.params['path']):
        with open(module.params['path'], 'w') as new_file:
            new_file.write(module.params['content'])
        result['changed'] = True
        result['original_message'] = 'File {path} succesfully created'.format(path=module.params['path'])
        result['message'] = 'File created'
    else:
        result['original_message'] = 'File {path} already exist'.format(path=module.params['path'])
        result['message'] = 'File already exist'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()