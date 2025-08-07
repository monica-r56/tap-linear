# tap-linear Fixes Applied

## Issues Fixed

### 1. Variable Reference Error (Line 53 in client.py)
**Problem**: The code was trying to log `body` before it was defined, causing a NameError.
**Fix**: Moved the logging statement after the `body` variable is defined.

### 2. Incorrect Authorization Header Format
**Problem**: Linear API requires Bearer token format, but the tap was sending just the token.
**Fix**: Modified the authenticator to use `Bearer {token}` format instead of just the token.

### 3. Excessive Debug Logging
**Problem**: Error-level logging was cluttering the output with full API responses.
**Fix**: Removed unnecessary debug logging statements that were using `logger.error()`.

## Files Modified

1. `tap_linear/client.py` - Fixed variable reference, authentication format, and removed debug logging
2. `test_config.json` - Created template configuration file

## How to Test the Fixed Tap

### Step 1: Install Dependencies
```bash
# In your tap-linear directory
pip install -e .
```

### Step 2: Configure Authentication
1. Get your Linear API token from https://linear.app/settings/api
2. Update `test_config.json` with your actual token:
```json
{
  "auth_token": "your_actual_linear_api_token",
  "start_date": "2024-01-01T00:00:00Z",
  "api_url": "https://api.linear.app/graphql"
}
```

### Step 3: Test Discovery Mode
```bash
tap-linear --config test_config.json --discover
```

### Step 4: Test Data Extraction
```bash
tap-linear --config test_config.json --discover > catalog.json
# Edit catalog.json to select the Issues stream
tap-linear --config test_config.json --catalog catalog.json
```

### Step 5: Use with Meltano
In your Meltano project, ensure your `meltano.yml` has the correct configuration:

```yaml
extractors:
  - name: tap-linear
    pip_url: /path/to/your/tap-linear/directory
    config:
      auth_token: ${LINEAR_API_TOKEN}
      start_date: "2024-01-01T00:00:00Z"
```

Then set your environment variable:
```bash
export LINEAR_API_TOKEN="your_actual_linear_api_token"
```

And run:
```bash
meltano invoke tap-linear
```

## Key Configuration Requirements

- `auth_token`: Your Linear API token (required)
- `start_date`: ISO 8601 datetime string for incremental sync start point
- `api_url`: Linear GraphQL endpoint (defaults to https://api.linear.app/graphql)

## Common Issues to Watch For

1. **Invalid Token**: Ensure your Linear API token is valid and has the necessary permissions
2. **Network Issues**: Verify you can reach api.linear.app from your environment
3. **Rate Limiting**: Linear API has rate limits, so large data extractions may need throttling
4. **Permissions**: Ensure your token has access to read issues from your Linear workspace