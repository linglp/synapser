# synRestPut

Sends an HTTP PUT request to the Synapse server.

## Usage

``` r
synRestPut(uri, body=NULL, endpoint=NULL, headers=NULL, retry_policy=list(), requests_session_async_synapse=NULL, kwargs=NULL)
```

## Arguments

- uri:

  (str) URI on which the request is performed

- body:

  (Any) The payload to be delivered, as a JSON-encoded string (e.g. via
  [`rjson::toJSON()`](https://rdrr.io/pkg/rjson/man/toJSON.html)). This
  is passed straight through to the underlying HTTP client's `content`
  argument, which only accepts a string or raw bytes – passing a named
  list/dict directly will fail with
  `TypeError: Unexpected type for 'content'`.

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

This wraps synapseclient's `rest_put_async()`, which is a Python `async`
coroutine method. Calling `synRestPut()` does not run that coroutine –
it returns an unresolved Python coroutine object, since reticulate does
not automatically await coroutines. To get the actual response, resolve
the returned coroutine yourself with Python's `asyncio.run()` via
reticulate, as shown in the example below.

## Examples

``` r
if (FALSE) { # \dontrun{
## Using this function
    # For ordinary entity updates, prefer the higher-level synSetProperties()
    # / synStore() functions instead -- they handle this fetch-modify-store
    # cycle for you. Reach for synRestPut() only for REST endpoints that
    # don't have a higher-level model wrapper.
    library(synapser)
    synLogin()

    asyncio = reticulate::import("asyncio")

    # Fetch the entity's current properties first
    get_coro = synRestGet(uri = "/entity/syn123456")
    entity_properties = asyncio$run(get_coro)

    # Modify the field(s) you want to change
    entity_properties$name = "New Name"

    # The body must be a JSON-encoded string, not a named list -- it is passed
    # straight through to the underlying HTTP client's `content` argument,
    # which only accepts a string or raw bytes.
    put_coro = synRestPut(uri = "/entity/syn123456", body = rjson::toJSON(entity_properties))
    response = asyncio$run(put_coro)
    response
} # }
```
