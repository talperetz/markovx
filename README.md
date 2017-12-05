![](resources/markovx_banner.png)

### Intro ###
[Markov Chains](https://en.wikipedia.org/wiki/Markov_chain) implementation <br>

### Installation ###
in your terminal:

    > pip install markovx
    
### Examples ###

Adding Chains
```python
from markovx.models import MarkovModel
    
mx = MarkovModel()
mx.add_one('123456')
mx.add_one('qwerty')
mx.add_many(['admin', 'root', 'user'])
```

Generating Chains
```python
mx.generate(6) # len of tokens in chain
```
```python
mx.generate(6, random_init=True)
# when True first token in chain would be assigned randomly
# when False first token would be assigned based on observed firs tokens
# default to False
```
```python
mx.generate(6, smart_ending=True)
# when False chain wouldn't be terminated before len(chain) == n even if model got to an end token
# when True if model got to an end token while len(chain) < n chain would terminate
# default to False
```
Ordinal Markov Chains (position dependent chains)
```python
from markovx.models import OrdinalMarkovModel
    
mx = OrdinalMarkovModel()
mx.add_one('123456')
mx.add_one('123qwe')
mx.add_many(['qwerty', 'qwe123', 'qwe123456'])
mx.generate(6)
```

### Contact ###
[Tal Peretz](https://www.linkedin.com/in/tal-per/)





