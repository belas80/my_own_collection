# Ansible Collection - belas80.my_own_collection

В этой collection содержится модуль `my_own_module` , который создает текстовый файл по пути, определенном в параметре `my_own_path`,
с содержимым, определённым в параметре `my_own_content`.  
  
Так же в collection содержится роль `create_file`, с default значениями параметров:  

| Key             | Value          |
|-----------------|----------------|
| my_own_path:    | ./new_file.txt |
| my_own_content: | "some content" |
  
Минимальный плейбук для запуска модуля с использованием роли:  
```yaml
---
  - name: Create file
    hosts: localhost
    roles:
      - belas80.my_own_collection.create_file
```
