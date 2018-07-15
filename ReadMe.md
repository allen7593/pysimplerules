# Python Rule Engine
## How to use?
1. Create an empty python file and have a list with following structure
    ```
    aganda_config = [
        {
            "agenda_name": "agenda_one",
            "items_provided": [
                TestClass,
                <classes that need to provided for this agenda,
                Note: Premitive types are not supported:
                    - int
                    - float
                    - str
                    - list
                    - dict
                    - set
                    - bytes
                    - tuple
                >
            ]
        }
    ]
    ```
    ```
    class TestClass: 
        a: int
        
        def __init__(self):
            self.a = 1
    ```
2. Initialize rule config using Initializer, you only need to initialize once when application start
    ```
    from initializer.initializer import Initializer
    
    init = Initializer(agenda_config)
    init.initialize()
    ```
3. Decorate the method you wants to execute for each agenda group using @rule decorator
    ```
    from decorator.dec import rule

    @rule("test_agenda", conditions="ai.get_TestClass().a == 1")
    def foobar(agenda_item):
        some actions...
    ```    
    Parameters for @rule decorator
    
    | Name          | Description     | Type  |
    | ------------- |:---------------:| -----:|
    | agenda        | agenda group    |   str |
    | exec_order    | execution order, the bigger the number, the higher the priority, default to 0|   int |
    | conditions    | conditions, default to True, if you did not specify the conditions, it will always executed|    str |
 4. Prepare a list of rules that you wants to import
    ```
    import_list = [
        "agendprepare.test.test_rules"
    ]
    ```
 5. Use RuleReloader to import/reload/re-import all rules
    ```
    reloader = RuleReloader(self.import_list)
    reloader.reload()
    ```
 6. Prepare your own class instances that you provided in agenda_config for each agenda group
    ```
    preparer = AgendaPreparer()
    test_ins = TestClass()
    test_ins.a = 1
    ai = preparer.prepare_agenda("test_agenda", test_ins)
    ```
 7. Execute rules for certain agenda group using RuleExecutor
    ```
    executor = RuleExecutor()
    executor.execute_all(ai)
    ```
 8. An agenda_item will be provided to the method and all class instances your just provided are in agenda_item,
you can access them via using ai.get_{ClassTypeName} or ai.{ClassTypeName}, {ClassTypeName} will as same as the name of your class type, 
and also its case sensitive.
