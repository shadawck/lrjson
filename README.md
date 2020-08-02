# LRJson

Convert Lightroom Template file (.ltemplate) into manipulable JSON file

### Install

You can install LRJson either via pip (PyPI) or from source. To install using pip:
```sh
python3 -m pip install lrjson
```

Or manually:
```sh
git clone https://github.com/remiflavien1/lrjson
cd lrjson
python3 setup.py install
```

### CLI

Realy simple CLI :   
Take a `Lightroom Template (.lrtemplate)` file and convert it into `JSON` file :
```sh
$ lrson myfilter.lrtemplate
File converted with Success
```

You can print output with `-p|--print` flag :
```
$ lrson myfilter.lrtemplate -p
{
    "id": "A76FFDE6-31E0-4FF6-AD4E-FF6F9EE930E9",
    "internalName": "mytemplate",
    "title": "myTemplate",
    "type": "Develop",
    "value": {
        "settings": {
            "Blacks2012": 40,
            "Clarity2012": 18,
            "ColorNoiseReduction": 5,
            "ColorNoiseReductionDetail": 50,
            "ColorNoiseReductionSmoothness": 50,
            "Contrast2012": 49,
            "HueAdjustmentRed": 9,
            "HueAdjustmentYellow": -89,
            "LuminanceAdjustmentAqua": -50,
            "LuminanceAdjustmentBlue": 34,
            "LuminanceAdjustmentGreen": 5,
            "LuminanceAdjustmentMagenta": 1,
            "LuminanceAdjustmentOrange": -1,
            "LuminanceAdjustmentPurple": 40,
            "LuminanceAdjustmentRed": 0,
            "LuminanceAdjustmentYellow": 37,
            "LuminanceNoiseReductionContrast": 0,
            "LuminanceNoiseReductionDetail": 50,
            "LuminanceSmoothing": 0,
            "ParametricDarks": 0,
            "ParametricHighlightSplit": 48,
            "ParametricHighlights": 0,
            "ParametricLights": 0,
            "Tint": 33,
            "ToneCurveName2012": "Custom",
            "ToneCurvePV2012": [
                14,
                25,
                94,
                112,
                198,
                170,
                255
            ],
            "ToneCurvePV2012Blue": [
                0,
                0,
                255
            ],
            "ToneCurvePV2012Green": [
                0,
                0,
                255
            ],
            "ToneCurvePV2012Red": [
                0,
                0,
                255
            ],
            "Vibrance": 1,
            "WhiteBalance": "Custom",
            "Whites2012": 55,
            "orientation": "AB"
        },
        "uuid": "28ACD78F-6C28-4A38-B09E-A62718A4C073"
    },
    "version": 0
}
```

## API
There is only one function.    
Just import it and use it.

```python
>>> from lrjson import convert_lr_to_json as cvj
>>> cvj.convert("myFilter.lrtemplate","output.json")
```