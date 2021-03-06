{

    'variables' : {
        'stl_include_dir' : '<(ndk_root)/sources/cxx-stl/gnu-libstdc++/<(ndk_ver)/include',
    },

    # Include this file to enable C++11 support

    'target_defaults': {

        'cflags_cc': [
            '-std=c++11',
        ],

        'conditions': [

            ['OS=="android"', {
# TODO:
# Use GYP to enable c++11 stl support for android.
# Now, I just enable it in Android's Application.mk by APP_STL.
#                'include_dirs':[
#                    '<(stl_include_dir)',
#                ],
#                'libraries': [
#                    '-lgnustl_static',
#                    '-lstdc++',
#                ],
#                'link_settings': {
#                    'ldflags': [
#                        '-std=c++11',
#                    ],
#                },

                'link_settings': {
                    'ldflags': [
                        '-latomic',
                    ],
                },
            }], # OS=="android"

            ['OS=="linux" and platform=="darwin"', {
                'xcode_settings': {
                    'CLANG_CXX_LANGUAGE_STANDARD' : 'c++11',
                    'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'],
                    'OTHER_LDFLAGS': ['-stdlib=libc++'],
                },
            }], # OS=="linux" and platform=="darwin"

        ],   # conditions
    },

}
