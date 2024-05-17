Облачное машинное обучение предоставляет высокую вычислительную мощность без необходимости закупки собственного оборудования, но при этом включает в себя передачу данных на сторонний сервер, в связи с чем возникает проблема обеспечения безопасности данных, так как, например, уязвимости в самом облаке или неправильная настройка доступа к облаку могут привести к угрозам информационной безопасности, в том числе, утечке данных, что приведёт к репутационным потерям и штрафам за нарушение правил информационной безопасности.

Решением данной проблемы выступает предварительное шифрование данных перед их загрузкой на сервер, то есть обучение модели на зашифрованных данных. Такую возможность предоставляет технология полностью гомоморфного шифрования, позволяющего выполнять вычисления с зашифрованными данными без их расшифровки, что обеспечивает наивысший уровень безопасности, так как содержание данных никогда не раскрывается.

В данной работе демонстрируется применение полностью гомоморфного шифрования для машинного обучения на примере решения задачи кредитного скоринга с предварительным шифрованием данных на стороне клиента (этап 1) и обучением и оценкой модели на зашифрованных данных на стороне сервера (этап 2). 

В качестве библиотеки полностью гомоморфного шифрования выбрана TenSEAL, основанная на Microsoft SEAL, которая в настоящее время является наиболее используемой библиотекой полностью гомоморфного шифрования. С помощью API она обеспечивает простоту использования языка Python, при этом сохраняя эффективность за счет реализации большинства операций с использованием C++.