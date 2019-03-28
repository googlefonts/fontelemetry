### Fontelemetry Settings

The fontelemetry settings file is named `fontelemetry.toml` and can be stored on any file path local to the project that uses fontelemetry.  

The file must be formatted according to the [TOML specification](https://github.com/toml-lang/toml#user-content-spec).  This file is parsed to a Python dictionary with the Python [toml package](https://github.com/uiri/toml) for use in fontelemetry.  Most fontelemetry objects support manual construction of a Python dictionary that mimics the parsed format of the settings file.

The following text shows all supported settings.  *Please be aware that this project is at an early stage of development and the settings specification is not stable.  These definitions may change without advance notice.*  SemVer versioning will be introduced in the future.


```toml

# Color definitions
[color]

    # [ glyphs source mark color definitions ]
    # glyphs source files have a fixed mark color range that includes the following color options.
    # fontelemetry supports one or more color definitions in this field and the color name keys
    # must use the names as specified below.
    [color.mark.glyphs]
    red = "Status 1"
    orange =  "Status 2"
    brown = "Status 3"
    yellow = "Status 4"
    ltgreen = "Status 5"
    dkgreen = "Status 6"
    ltblue = "Status 7"
    dkblue = "Status 8"
    purple = "Status 9"
    pink = "Status 10"
    ltgrey = "Status 11"
    dkgrey = "Status 12"
    white = "Done"

    # [ UFO source mark color definitions ]
    # UFO source files support use of the entire RGBA spectrum for glyph mark colors.
    # Use an informative key name for the color mapping here.
    [color.mark.ufo]
    red = ["0.85,0.26,0.06,1", "Status 1"]
    orange = ["0.99,0.62,0.11,1", "Status 2"]
    yellow = ["0.97,0.9,0,1", "Status 3"]
    green = ["0.04,0.57,0.04,1", "Status 4"]
    white = ["1.0,1.0,1.0,1", "Done"]

```