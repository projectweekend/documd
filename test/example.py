from documd import documentation


@documentation.register(doc_name='test.md', section='This Stuff', title='This route')
class ThisApiRoute:
    """
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


@documentation.register(doc_name='test.md', section='That Stuff', title='That route')
class ThatApiRoute:
    """
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
