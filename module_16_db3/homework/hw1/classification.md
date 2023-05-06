## Типы связей между таблицами в схеме

![](../img/cinema_schema_diagram.png)

| Тип связи | Таблица 1 | Таблица 2     |
|:---------:|-----------|---------------|
|    m2m    | actors    | movie         |
|    o2m    | movie     | oscar_awarded |
|    m2m    | movie     | director      |