# mutation-gate-poc

Testing the mutation-regression workflow in [DataDog/dd-license-attribution](https://github.com/DataDog/dd-license-attribution).


## Getting Started

See below for instructions on running the project locally.

## Running locally

```bash
pip install -e ".[dev]"
pytest tests/unit/ -v
mutmut run --max-children 4
mutmut results --all true
```

## License

This project is licensed under the Apache License 2.0 - see [LICENSE](LICENSE) for details.

The mutation-regression workflow is derived from [DataDog/dd-license-attribution](https://github.com/DataDog/dd-license-attribution), which is also licensed under the Apache License 2.0.
