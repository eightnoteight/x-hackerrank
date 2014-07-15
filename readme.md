# x-hackerrank
x-hackerrank checks code and speculates it based on the test cases provided by the user.
x-hackerrank uses [hackrank.com](http://www.hackerrank.com) [API](http://www.hackerrank.com/api) to get those results. it is more useful for competitve programmers to speculate their programs before submission right through their terminals or it can used as a cloud compiler.

### usage in *nix systems
- get your free api key from [here](http://www.hackerrank.com/api)
- `git clone https://github.com/eightnoteight/x-hackerrank.git`
- `cd x-hackerrank`
- `python x-hackerrank.py -h`
- To use it efficiently one can create an alias to their .bashrc file.

### features
- error handling for HTTP requests.
- Once api key is entered it is stored as cache to save from entering everytime
- Once a language is chosen it is made the default for the future requests, and it can be changed at any time
- can take multiple input files.

### caution
- may not support a proxy.
- depends on some basic python libraries such as requests and json
- works good on python 2.7.5, but the behavior in python 3 is unknown.

### API KEY from hackerrank
you can get your api key from https://www.hackerrank.com/api