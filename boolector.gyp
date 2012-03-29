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
    'use_precosat': 1,
  },
  'target_defaults': {
    'cflags': [
      '-Wall',
    ],
  }, # target_defaults
  'targets': [
    {
      'target_name': 'libboolector',
      'type': 'static_library',
      'sources': [
        'boolector.c',
        'boolector.h',
        'btoraig.c',
        'btoraig.h',
        'btoraigvec.c',
        'btoraigvec.h',
        'btorbtor.c',
        'btorbtor.h',
        'btorconfig.h',
        'btorconst.c',
        'btorconst.h',
        'btorexit.h',
        'btorexp.c',
        'btorexp.h',
        'btorhash.c',
        'btorhash.h',
        'btorlogic.h',
        'btormain.c',
        'btormain.h',
        'btormem.c',
        'btormem.h',
        'btorparse.h',
        'btorpreco.cc',
        'btorpreco.h',
        'btorqueue.h',
        'btorrand.c',
        'btorrand.h',
        'btorrewrite.c',
        'btorrewrite.h',
        'btorsat.c',
        'btorsat.h',
        'btorsmt.c',
        'btorsmt.h',
        'btorstack.h',
        'btorutil.c',
        'btorutil.h',
      ], # sources
      'dependencies': [
        'picosat/picosat.gyp:libpicosat',
      ],
      'conditions': [
        ['use_precosat==1', {
          'dependencies': [
            'precosat/precosat.gyp:libprecosat',
          ],
          'defines': [
            'BTOR_USE_PRECOSAT',
          ],
        }],
      ], # conditions
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
      },
      'actions': [
        {
          'action_name': 'gen_config',
          'inputs': [
            'boolector.gyp',
            'gen_config.sh',
          ],
          'outputs': [
            'btorconfig.h',
          ],
          'action': [ './gen_config.sh', 'gyp', '>(_cflags)', ],
        },
      ], # actions
    }, # target libboolector
    {
      'target_name': 'boolector',
      'type': 'executable',
      'dependencies': [
        'libboolector',
      ],
      'sources': [
        'boolectormain.c',
      ],
    }, # target boolector
    {
      'target_name': 'synthebtor',
      'type': 'executable',
      'dependencies': [
        'libboolector',
      ],
      'sources': [
        'synthebtor.c',
      ],
    }, # target synthebtor
    {
      'target_name': 'deltabtor',
      'type': 'executable',
      'dependencies': [
        'libboolector',
      ],
      'sources': [
        'deltabtor.c',
      ],
    }, # target deltabtor
  ], # 'targets'
}
