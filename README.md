![](resources/markovx_banner.png)

### Intro ###
[Markov Chains](https://en.wikipedia.org/wiki/Markov_chain) implementation <br>

### Installation ###
in your terminal:

    > pip install markovx
    
### Examples ###

Adding Chains
```python
from markovx.model import MarkovModel
    
mx = MarkovModel()
mx.add_one('123456')
mx.add_one('qwerty')
mx.add_many(['admin', 'root', 'user'])
```

Generating Chains
```python
mx.generate(10) # len of tokens in chain
```
```python
mx.generate(10, random_init=True)
# when True first token in chain would be assigned randomly
# when False first token would be assigned based on observed firs tokens
# default to False
```
```python
mx.generate(10, smart_ending=False)
# when False chain wouldn't be terminated before len(chain) == n even if model got to an end token
# when True if model got to an end token while len(chain) < n chain would terminate
# default to True
```

### Contact ###
[Tal Peretz](https://www.linkedin.com/in/tal-per/)





