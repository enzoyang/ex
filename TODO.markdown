#2010-12-01
1. 注册表单自定义验证：判断email是否已经存在
2. 写一个装饰器，用于判断此IP是否处于禁止注册列表
3. 禁止列表规则：
    * 注册成功后5分钟内，该IP无法继续注册
    * 登录尝试错误3次后，该IP5分钟内无法尝试登录