# **Logging**
----
### logger level recommendations
#### use debug only for detail debugging information, e.g. when the data is big or the frequency is high
```
def complex_algorithm(items):
    for i, item in enumerate(items):
        # do some complex algorithm computation
        logger.debug('%s iteration, item=%s', i, item)
```
#### use info levels for routines, e.g. when handling requests or server state changes
```
def handle_request(request):
    logger.info('Handling request %s', request)
    # handle request here
    result = 'result'
    logger.info('Return result: %s', result)
```
```
def start_service():
    logger.info('Starting service at port %s ...', port)
    service.start()
    logger.info('Service is started')
```
#### use warning when it's important, but not an error. E.g. for authentication or performance warnings
```
def authenticate(user_name, password, ip_address):
    if user_name != USER_NAME and password != PASSWORD:
        logger.warn('Login attempt to %s from IP %s', user_name, ip_address)
        return False
    # do authentication here
```
#### use error level when something is wrong, e.g. when throwing exceptions, IO failures, no connection
```
def get_user_by_id(user_id):
    user = db.read_user(user_id)
    if user is None:
        logger.error('Cannot find user with user_id=%s', user_id)
        return user
    return user

```
#### there is also the critical level, but this is seldomly used
----
### logger name recommendations
It's recommended to set the logger name to `__name__`, this way the configurations are shared when used in a module

### exceptions
It can be helpfull to record tracebacks to see where something went wrong, as logging itself won't be enough help for troubleshooting  
You should capture exceptions and record them with traceback  
You can call logger methods with the exc_info=True parameter to dump traceback
```
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception, e:
    logger.error('Failed to open file', exc_info=True)
```

