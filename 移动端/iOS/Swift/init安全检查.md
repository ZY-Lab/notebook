## init安全检查
错误: `self` used before super.init call

在 init 中 有四个阶段的安全检查, 这里违背了第四个检查

    // 初始化 编译的过程的四个安全检查
    // 1. 在调用父类初始化之前 必须给子类特有的属性设置初始值, 只有在类的所有存储属性状态都明确后, 这个对象才能被初始化
    // 2. 先调用父类的初始化方法,  再 给从父类那继承来的属性初始化值, 不然这些属性值 会被父类的初始化方法覆盖
    // 3. convenience 必须先调用 designated 初始化方法, 再 给属性初始值. 不然设置的属性初始值会被 designated 初始化方法覆盖
    // 4. 在第一阶段完成之前, 不能调用实类方法, 不能读取属性值, 不能引用self

错误: Property not initialized at super.init call违反了安全检查第1条.

实际用例如下:

    class KeyerTableViewCell:UITableViewCell{
        let keyer:Keyer
        let normalMargin = 8
        let labelWidth = 60
    
        init(keyer:Keyer){
            self.keyer = keyer
            super.init(style: .default, reuseIdentifier: "SettingKeyerTableViewCell")
            self.setupUI()
        }
    }