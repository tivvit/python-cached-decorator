# Python Cached Decorator 
### Provides caching for functions
* Suitable for time consuming computations
* How does it work:
    * First run = run
    * Second run = load result
* Stores result in pickle
* Checks if function args matches
* Always use newest result

### Example

```python
from Cached import Cached

@Cached()
# possible params: Cached(force_run=False, output_path="cached_data", name="")
def func(arg):
    return arg

print fun(5)
```
### Options
All options are optional
* **force_run** [True/**False**] Do not use cached result
* **output_path** [String] *default=cached_data* in script path, /tmp is a good idea
* **name** [String] *default=function name*, force function name - used for store and load

### Development

Feel free to contribute.

### Copyright and License 

&copy; 2015 [Vít Listík](http://tivvit.cz), [Michal Bukovský](https://github.com/burlog)

Released under [MIT licence](https://github.com/tivvit/python-cached-decorator/blob/master/LICENSE)