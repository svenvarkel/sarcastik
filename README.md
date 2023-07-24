# Random Case

This simple script takes string from stdin and randomizes it's case.
It can be used with command line tools to paste from clipboard and return converted string to clipboard.

## Use case

Main use case for this is expressing sarcasm on social media.

## Example usage

### In shell
    
```bash
python3 sarcastik/sarcastic.py
```

### On MacOS

```bash
pbpaste | python3 sarcastik/sarcastik.py | pbcopy
```

# Helper script

There is helper shell script that can be used to run this script from anywhere.

```bash
./sarcastik.sh
```