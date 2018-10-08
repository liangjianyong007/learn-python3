from model.odjDefine import A
if __name__ == '__main__':
   # 获取A的所有子类
   sub_class_list = A.__subclasses__()
   for i in range(len(sub_class_list)):
        # 获取子类的类名
        class_name=sub_class_list[i].__name__
        print(class_name)
        # 导入model模块
        model_module = __import__('model')
        m_py = getattr(model_module, 'odjDefine')
        # 根据子类名称从m.py中获取该类
        obj_class_name = getattr(m_py, class_name)
        # 实例化对象
        obj = obj_class_name()
        # 调用print_name方法
        getattr(obj, 'print_name')()



