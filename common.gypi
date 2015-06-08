{

    'variables' : {
        'ndk_root': '<!(echo $NDK_ROOT)',
        'ndk_ver': '4.6',
    },

    'target_defaults': {
        # Things get confused if multiple targets in the same .gyp file don't have the same configuration
        # names, so define them all here.  (this problem doesn't appear to exist across .gyp files,
        # and it doesn't work to define configurations in globals.gypi).
        'default_configuration': 'Debug',
        # enable andoird short names (not full path) for linking libraries
        "android_unmangled_name": 1,
        'configurations': {
            'Debug': {
            },
            'Release': {
            },
        },

        'cflags': [
            '-Wall', '-Wno-unused-parameter',
        ],

        'cflags_cc': [
            '-frtti',
            '-fexceptions',
        ],

        'conditions': [
            ['OS=="android"', {
                'defines': [
                    'ANDROID',
                    '__ANDROID__',
                ],

                'cflags': [
                    '-fno-exceptions',
                ],
            }],
            ['OS=="ios"', {
                'defines': [
                    'IOS',
                ],
                'xcode_settings': {
                    'SDKROOT': 'iphoneos',
                    'TARGETED_DEVICE_FAMILY': '1,2',
                    'CODE_SIGN_IDENTITY': 'iPhone Developer',
                    'IPHONEOS_DEPLOYMENT_TARGET': '7.1',
                    'OTHER_CPLUSPLUSFLAGS' : ['-fno-exceptions'],
                    'OTHER_LDFLAGS': [
                        '-ObjC',
                    ],
                },
            }], # OS=="ios"
        ],   # conditions
    },

}