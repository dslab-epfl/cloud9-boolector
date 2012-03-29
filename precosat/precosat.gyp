#
# Cloud9 Parallel Symbolic Execution Engine
# 
# Copyright (c) 2012, Dependable Systems Laboratory, EPFL
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Dependable Systems Laboratory, EPFL nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE DEPENDABLE SYSTEMS LABORATORY, EPFL BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# All contributors are listed in CLOUD9-AUTHORS file.
#

{
  'variables': {
    'check_with_picosat': 0,
    # TODO(bucur): Import the other options from the configure script
  },
  'target_defaults': {
    'cflags': [
      '-Wall',
      '-Wextra',
    ],
  },
  'targets': [
    {
      'target_name': 'libprecosat',
      'type': 'static_library',
      'sources': [
        'precobnr.cc',
        'precobnr.hh',
        'precosat.cc',
        'precosat.hh',
        'precocfg.hh',
      ],
      'conditions': [
        ['check_with_picosat==1', {
          'defines': {
            'CHECKWITHPICOSAT',
          },
          'dependencies': [
            '../picosat/picosat.gyp:libpicosat',
          ],
        }],
      ], # conditions
      'actions': [
        {
          'action_name': 'gen_config',
          'inputs': [
            'precosat.gyp',
            'gen_config.sh',
          ],
          'outputs': [
            'precocfg.hh',
          ],
          'action': [ './gen_config.sh', 'gyp', '>(_cflags)', ],
        },
      ], # actions
    }, # target libprecosat
    {
      "target_name": "precosat",
      "type": "executable",
      "dependencies": [
        "libprecosat",
      ],
      "sources": [
        'precomain.cc',
      ],
    }, # target precosat
  ], # targets
}
