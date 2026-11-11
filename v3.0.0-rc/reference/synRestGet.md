# synRestGet

Sends an HTTP GET request to the Synapse server.

## Usage

``` r
synRestGet(uri, endpoint=NULL, headers=NULL, retry_policy=list(), requests_session_async_synapse=NULL, kwargs=NULL)
```

## Arguments

- uri:

  (str) URI on which get is performed

- endpoint:

  (str) Server endpoint, defaults to the client's configured repository
  endpoint (see
  [`synSetEndpoints()`](https://r-docs.synapse.org/v3.0.0-rc/reference/synSetEndpoints.md)).

- headers:

  (Headers) Named list of headers to use.

- retry_policy:

  (dict\[str, Any\]) A retry policy (named list) whose keys should match
  the parameters of
  [with_retry_time_based_async](https://python-docs.synapse.org/reference/core/),
  the underlying Python client's retry mechanism.

- requests_session_async_synapse:

  (AsyncClient) The async client to use when making this specific call.

- kwargs:

  optional named parameter: Any other arguments taken by a
  [request](https://www.python-httpx.org/api/) method

## Value

JSON encoding of response

## Note

This wraps synapseclient's `rest_get_async()`, which is a Python `async`
coroutine method. Calling `synRestGet()` does not run that coroutine –
it returns an unresolved Python coroutine object, since reticulate does
not automatically await coroutines. To get the actual response, resolve
the returned coroutine yourself with Python's `asyncio.run()` via
reticulate, as shown in the example below.

## Examples

``` r
if (FALSE) { # \dontrun{
## Using this function
    library(synapser)
    synLogin()

    asyncio = reticulate::import("asyncio")

    # Low-level REST access to an entity's raw JSON, bypassing the synGet() model wrapper
    coro = synRestGet(uri = "/entity/syn123456")
    response = asyncio$run(coro)
    response
} # }
```
