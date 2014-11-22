{

    'target_defaults': {
        # Things get confused if multiple targets in the same .gyp file don't have the same configuration
        # names, so define them all here.  (this problem doesn't appear to exist across .gyp files,
        # and it doesn't work to define configurations in globals.gypi).
        'default_configuration': 'Debug',
        'configurations': {
            'Debug': {
            },
            'Release': {
            },
        },

        'conditions': [
            ['OS=="android"', {
                'defines': [
                    'ANDROID',
                    '__ANDROID__',
                ],
            }],
            ['OS=="ios"', {
                'xcode_settings': {
                    'SDKROOT': 'iphoneos',
                    'TARGETED_DEVICE_FAMILY': '1,2',
                    'CODE_SIGN_IDENTITY': 'iPhone Developer',
                    'IPHONEOS_DEPLOYMENT_TARGET': '7.1',
                    'OTHER_LDFLAGS': [
                        '-ObjC',
                    ],
                },
            }], # OS=="ios"
        ],   # conditions
    },

}