# Project Name

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python ./mock_services/mock_stream_server.py
```

The server will start on `http://localhost:8082`

## Running Tests

```bash
pytest
```

For verbose output:
```bash
pytest -v
```

## Project Structure

- `.\mock_services\mock_stream_server.py` - Mock stream server
- `.\infra\` - Project infrastracture (streaming_validator, schemas, mobile_session)
- `requirements.txt` - Python dependencies
- `tests/` - Test suite

## Configuration

- `infra\config\config.json` - Project configuration
- `pytest.ini` - Pytest configuration
