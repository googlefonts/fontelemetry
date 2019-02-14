### Fontelemetry Settings

The fontelemetry settings file is named `fntel.toml` (pronounced `/fintel/`) and can be stored on any file path local to the project that uses fontelemetry.  

The file must be formatted according to the [TOML specification](https://github.com/toml-lang/toml#user-content-spec).  This file is parsed to a Python dictionary with the Python [toml package](https://github.com/uiri/toml) for use in fontelemetry.  Most fontelemetry objects support manual construction of a Python dictionary that mimics the parsed format of the settings file.

The following text shows all supported settings.  *Please be aware that this project is at an early stage of development and the settings specification is not stable.  These definitions may change without advance notice.*  SemVer versioning will be introduced in the future.


```toml

# Glyph mark color definitions
[colordefinitions]

    [colordefinitions.glyphs]
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

    [colordefinitions.ufo]

```