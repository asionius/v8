# Copyright 2016 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'v8_code': 1,
  },
  'includes': ['../../build/toolchain.gypi', '../../build/features.gypi'],
  'targets': [
    {
      'target_name': 'parser_fuzzer',
      'type': 'executable',
      'dependencies': [
        'parser_fuzzer_lib',
      ],
      'include_dirs': [
        '../..',
      ],
      'sources': [
        'fuzzer.cc',
      ],
    },
    {
      'target_name': 'parser_fuzzer_lib',
      'type': 'static_library',
      'dependencies': [
        'fuzzer_support',
      ],
      'include_dirs': [
        '../..',
      ],
      'sources': [  ### gcmole(all) ###
        'parser.cc',
      ],
    },
    {
      'target_name': 'fuzzer_support',
      'type': 'static_library',
      'dependencies': [
        '../../tools/gyp/v8.gyp:v8_libplatform',
      ],
      'include_dirs': [
        '../..',
      ],
      'sources': [  ### gcmole(all) ###
        'fuzzer-support.cc',
        'fuzzer-support.h',
      ],
      'conditions': [
        ['component=="shared_library"', {
          # fuzzers can't be built against a shared library, so we need to
          # depend on the underlying static target in that case.
          'dependencies': ['../../tools/gyp/v8.gyp:v8_maybe_snapshot'],
        }, {
          'dependencies': ['../../tools/gyp/v8.gyp:v8'],
        }],
      ],
    },
  ],
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'fuzzer_run',
          'type': 'none',
          'dependencies': [
            'parser_fuzzer',
          ],
          'includes': [
            '../../build/isolate.gypi',
          ],
          'sources': [
            'fuzzer.isolate',
          ],
        },
      ],
    }],
  ],
}
