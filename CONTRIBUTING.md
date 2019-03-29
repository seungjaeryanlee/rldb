# How to Contribute

Thank you for your interest in helping us improve rldb!

## Testing

We use `pytest` to verify our package. Note that we separate our tests from our application code. Thus, you have two ways of running tests.

The first is installing rldb with the `--editable` flag. This enables you to use the `pytest` command.

```bash
pip install --editable .
pytest
```

The second is running pytest with the following command.

```bash
python -m pytest
```
