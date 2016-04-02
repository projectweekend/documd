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
