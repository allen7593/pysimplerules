#Python Rule Engine
## How to setup?
1. Create an empty python file and have a list with following structure
    ```
    aganda_dict = [
        {
            "agenda_name": "agenda_one",
            "items_provided": [
                <classes that need to provided for this agenda>
            ]
        }
    ]
    ```
2. Initialize rule config using Initializer
    ```
    from initializer.initializer import Initializer
    
    init = Initializer(agenda_config)
    init.initialize()
    ```
3.