graph TD
    A[Sprint开始前: 确定需求范围] --> B[第一周: 产品需求宣讲]
    B --> C[设计阶段: 研发写设计文档 / 测试写用例]
    C --> D[研发阶段: 编码并提交至 2.6-test 分支]
    D --> E[Showcase 给测试 & 编写自动化用例]
    E --> F[测试阶段: 研发修复 Bug / 测试人员执行测试]
    F --> G[发版阶段: 合并至 2.6-release 分支]
    G --> H[回归测试 & 产品准备 Release Notes]
    H --> I{回归完成且Bug修复?}
    I -- 是 --> J[正式发布]
    J --> K[1. 版本号+1 如 2.6.101]
    K --> L[2. 记录 ws/wt/datasource 仓库 Commit ID]
    L --> M[3. 发送全员版本通知邮件]
