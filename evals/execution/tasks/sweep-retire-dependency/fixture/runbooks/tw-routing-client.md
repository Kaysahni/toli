# tw-routing-client (Python library)

Maintainers: Routing Core. Repo: `git.tesselwick.internal/routing/tw-routing-client`

Most Python services do not call RouteCalc over raw HTTP. They use this
library, which handles auth, retries, and response parsing. The library can
talk to either RouteCalc API generation, and which one it talks to is decided
at runtime.

## Choosing the backend

The backend is chosen by the `RC_API_MODE` environment variable:

| RC_API_MODE | Backend used |
|---|---|
| `classic` | RouteCalc v1 (`routecalc-v1.core.tesselwick.internal`) |
| `current` | RouteCalc v2 (`routecalc.core.tesselwick.internal/v2`) |

If `RC_API_MODE` is not set at all, the default depends on the library
release: versions before 3.0.0 fall back to `classic`, and 3.0.0 or later
default to `current`.

We did it this way so teams could flip back quickly during the 2025 migration.
In hindsight the silent default in 2.x was a mistake.

## Other settings

- `RC_TIMEOUT_SECONDS` (default 5)
- `RC_MAX_RETRIES` (default 3, exponential backoff starting at 200 ms)
- `RC_CLIENT_ID` (defaults to the service name from the pod labels)

## Upgrading from 2.x to 3.x

1. Bump the pin.
2. Replace `client.quote(origin, dest, metres=True)` calls: v2 returns kilometres.
3. Run your integration tests against staging.
4. Remove any `RC_API_MODE` override unless you have a reason to keep it.

## Changelog highlights

- 3.4.0: async client
- 3.0.0: default backend changed to v2, distance units changed
- 2.9.0: added `RC_API_MODE=current` so 2.x users could opt into v2 early
- 2.5.0: bulk quote helper
