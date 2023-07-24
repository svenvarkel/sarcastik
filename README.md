# Random Case

This simple script takes string from stdin and randomizes it's case.
It can be used with command line tools to paste from clipboard and return converted string to clipboard.

## Use case

Main use case for this is expressing sarcasm on social media.

## Example usage

Works on MacOS

```bash
pbpaste | python3 random_case.py | pbcopy
```