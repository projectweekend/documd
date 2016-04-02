[![Build Status](https://build.exitcodezero.io/api/badges/projectweekend/documd/status.svg)](https://build.exitcodezero.io/projectweekend/documd)


# Usage
Write markdown documentation in your classes and decorate them with `documd.documentation.register`:
```python
from documd import documentation


@documentation.register(section='This Stuff')
class ThisApiRoute:
    """
    ### This route

    **POST:**
    ```
    /v1/this
    ```

    **Body:**
    ```json
    {
        "message": "this"
    }
    ```

    **Response:**
    ```json
    {
        "message": "this"
    }
    ```

    **Status Codes:**
    * `200` if successful
    * `400` if incorrect data provided
    """


@documentation.register(section='That Stuff')
class ThatApiRoute:
    """
    ### That route

    **POST:**
    ```
    /v1/that
    ```

    **Body:**
    ```json
    {
        "message": "that"
    }
    ```

    **Response:**
    ```json
    {
        "message": "that"
    }
    ```

    **Status Codes:**
    * `200` if successful
    * `400` if incorrect data provided
    """
```

Then use the `documd.documentation.generate` function in a script to output to a markdown file. Be sure to import the package that contains the decorated classes/functions in your script. For example, assuming that the two decorated classes above are in the `example.py`, a script ('example_script.py') might look like this:
```python
#!/usr/bin/env python
from documd import documentation
import example.py


def main():
    documentation.generate(output_file='SOME_DOCUMENTATION.md')


if __name__ == "__main__":
    main()
```

Then run your script to rebuild the markdown file:
```
./example_script.py
```

An example output file can be found in [test/output_example.md](test/output_example.md).


# Run tests
```
docker-compose run cli nosetests -v
```
