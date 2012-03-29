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
    # TODO(bucur): The names here look generic.  Are these global vars?
    'log%': 0,
    'stats%': 0,
    'trace%': 0,
    'version': 936,
    # TODO(bucur): Import the other options from the configure script
  },
  'target_defaults': {
    'conditions': [
      ['log==1', {
        'defines': [
          'LOGGING',
        ],
      }],
      ['stats==1', {
        'defines': [
          'STATS',
        ],
      }],
      ['trace==1', {
        'defines': [
          'TRACE',
        ],
      }],
    ], # conditions
    'cflags': [
      '-Wall',
      '-Wextra',
    ],
  }, # target_defaults
  'targets': [
    {
      'target_name': 'libpicosat',
      'type': 'static_library',
      'sources': [
        'picosat.c',
        'picosat.h',
        'version.c',
        'config.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
      },
      'actions': [
        {
          'action_name': 'gen_config',
          'inputs': [
            'picosat.gyp',
            'gen_config.sh',
          ],
          'outputs': [
            'config.h',
          ],
          'action': [ './gen_config.sh', 'gyp', '>(_cflags)', '<(version)', ],
        },
      ],
    }, # target libpicosat
    {
      'target_name': 'picosat',
      'type': 'executable',
      'sources': [
        'app.c',
        'main.c',
      ],
      'dependencies': [
        'libpicosat',
      ],
    }, # target picosat
    {
      'target_name': 'picomus',
      'type': 'executable',
      'sources': [
        'picomus.c',
      ],
      'dependencies': [
        'libpicosat',
      ],
    }, # target picomus
  ], # targets
}
