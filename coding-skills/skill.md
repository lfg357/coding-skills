---
name: trae-coding-skills-bundle
description: |
  Trae Coding Skills 技能合集：包含 Karpathy 通用编码规范、Flask 开发、前端兼容性、前后端协同。
  当用户进行代码编写、审查、重构、bug修复、性能优化时自动触发。
version: "1.0.0"
author: "Trae Coding Skills Team"
license: MIT
---

# Trae Coding Skills 合集

> 一套高标准的 AI 辅助编码规范，覆盖 Python、C++、Java、Go、JS/TS、Rust。

---

## 设计原则

1. **绝不擅自假设** — 只基于已有代码和明确需求行动
2. **拒绝过度设计** — 不为"未来可能"添加抽象层
3. **每行代码必须有目的** — 禁止无目标编码
4. **修改前说明理由，修改后说明影响范围**
5. **纯概念问答不输出代码** — 区分知识问答和代码操作

---

## 技能 1: Universal Karpathy Coding Guidelines

# 通用多语言 Karpathy 编码规范 v4.0

基于 Andrej Karpathy 对 LLM 编码痛点的核心洞察，整合 Bug-Fix、Code-Review、Security-Hardening、Test-Driven 四大方法论，适配所有主流编程语言，优先保障代码安全、极简、可维护。

**边界说明**：本规范偏向严谨性，对于简单的拼写修改、单行代码调整、注释补充，可酌情简化流程，无需全量校验。

---

## Skills 快速索引

| Skill 名称 | 职责范围 | 文件位置 |
|-----------|---------|---------|
| **universal-karpathy-coding-guidelines** | 核心编码原则（主技能） | `.trae-cn/skills/` |
| **frontend-compatibility** | 前端兼容性检查 | `.trae-cn/skills/` |
| **flask-web-dev** | Flask 后端开发规范 | `.trae-cn/skills/` |
| **hybrid-python-web** | 前后端协作协调 | `.trae-cn/skills/` |

**协作优先级**：Karpathy（主）> 语言专属规则 > 专项技能（补充）

---

## 自动触发规则

1. 当用户在编辑器中选中代码片段，无论是否提及关键词，自动启用本技能
2. 当用户打开的文件为代码文件（.py/.cpp/.java/.go/.js/.ts等），且需求涉及代码操作，自动启用本技能
3. 当用户提及【触发关键词】中的任意词汇，强制锁定本技能，优先级高于其他所有规则
4. 仅询问概念定义、不涉及代码编写/修改的需求，禁止触发本技能

---

## 第一原则：编码前先澄清，绝不擅自假设

**核心规则：不假设、不隐藏困惑、明确收益与 tradeoff**

动手写代码前，必须完成以下动作：
- 明确列出你对需求的所有假设，有歧义的地方必须先向用户提问确认
- 如果需求有多种实现方案，必须列出 2-3 种核心方案，说明各自的优缺点
- 如果用户的需求有更简单、更安全的实现方式，必须主动提出
- 遇到不明确的需求，立即停止，明确说出你困惑的点，向用户索要补充信息

### 强制自检 Checklist
开始编码前，必须逐条核对以下问题，**全部回答「是」才能进入编码阶段**：
1. 所有对需求的假设都已明确列出，无隐藏的默认选择？
2. 歧义点、不明确的需求都已向用户确认，无擅自决策的内容？
3. 目标编程语言、运行环境、框架版本都已明确，无兼容性风险？
4. 实现方案的优缺点、tradeoff 都已告知用户，用户已确认选型？

---

## 第二原则：极简优先，绝不过度设计

**核心规则：写能解决问题的最少代码，绝不添加非需求内的功能**

编码时必须严格遵守：
- 只实现用户明确要求的功能，绝不添加额外的"扩展性""灵活性"配置
- 不为单次使用的代码做过度抽象封装，能用简单函数实现的，绝不写类
- 不做不可能场景的错误处理，只处理明确会出现的异常情况
- 依赖最小化：除非用户明确要求，否则优先使用标准库
- 严格控制代码量，200 行能实现的功能，绝不写 500 行

### 强制自检 Checklist
完成代码编写后，必须逐条核对以下问题，**全部回答「否」才能输出**：
1. 有没有添加用户未明确要求的功能、配置、扩展能力？
2. 有没有可以直接删除的代码、抽象、封装、第三方依赖？
3. 资深同语言工程师会不会认为这段代码过度设计？
4. 有没有用更短、更符合语言惯用写法的实现方式？

---

## 第三原则：精准修改，只动该动的地方

**核心规则：每一行修改都能追溯到用户的需求，绝不乱改无关代码**

编辑现有代码时，必须遵守：
- 不修改、不格式化、和当前需求无关的相邻代码
- 不重构没有问题的现有代码，严格匹配项目已有的编码风格
- 如果发现和需求无关的死代码，只能向用户提出建议，绝不擅自删除
- 只清理你本次修改产生的未使用变量、导入、函数
- 修改完成后，必须给出 diff 说明，每一条修改都对应需求中的一个点

### 强制自检 Checklist
完成代码修改后，必须逐条核对以下问题，**全部回答「是」才能输出**：
1. 所有修改都能直接对应到用户的需求，无额外的无关改动？
2. 没有修改、格式化、优化和当前需求无关的代码？
3. 严格遵循了项目原有的编码风格、命名规范、目录结构？
4. 已明确给出修改diff说明，用户能清晰看到所有改动点？

---

## 第四原则：目标驱动执行，先定义成功标准

**核心规则：把模糊需求转化为可验证的目标，循环执行直到达标**

必须把用户的需求转化为带验证步骤的可落地目标：
- "加参数校验" → "先写非法输入的测试用例，再实现校验逻辑，确保所有用例通过"
- "修复 bug" → "先写复现 bug 的测试代码，定位问题点，修复后验证 bug 完全解决"
- "重构这段代码" → "先确保现有测试用例全部通过，重构后再次验证所有用例通过"

对于多步骤的复杂需求，必须先给出执行计划：
1. [执行步骤 1] → 验证标准：[怎么确认这一步完成且正确]
2. [执行步骤 2] → 验证标准：[怎么确认这一步完成且正确]
3. [执行步骤 3] → 验证标准：[怎么确认这一步完成且正确]

---

## 第五原则：Bug 修复 - 根因驱动最小化修复

**优先级：P0（最高）**

### 修复方法论

#### 1. 复现（Reproduction）
- 分析错误信息：定位文件、函数、行号
- 构建最小复现案例（MCVE）
- 确认复现环境：语言版本、依赖版本、操作系统
- 区分：必现/偶现/特定输入触发

#### 2. 根因分析（Root Cause）
- 追溯数据流：错误值从何处引入
- 检查时序问题：异步/并发/事件顺序
- 检查状态变更：可变状态、全局变量、副作用
- 检查假设违背：空值、类型不匹配、范围溢出

#### 3. 修复（Fix）
- 修复应针对根因，而非掩盖症状（禁止 catch-all 吞异常）
- 优先修复数据校验/前置条件
- 并发问题优先使用不可变数据或标准同步原语

#### 4. 验证（Verification）
- 复现案例必须通过
- 原有相关测试必须通过
- 检查相似代码是否存在相同缺陷（横向排查）

### 禁止行为
- ❌ 禁止在未理解根因前修改代码
- ❌ 禁止用 try-catch 掩盖逻辑错误
- ❌ 禁止引入新依赖来修复简单逻辑错误
- ❌ 禁止修改与 bug 无关的代码

### 退出条件
- ✅ MCVE 通过
- ✅ 原有测试通过
- ✅ 横向排查完成

---

## 第六原则：代码审查 - 系统性分级审查

**优先级：P0/P1/P2 分级输出**

### 问题分级规则

| 等级 | 定义 | 处理方式 |
|-----|------|---------|
| **P0** | 必须修复：语法错误、逻辑bug、内存泄漏、安全漏洞、SQL注入、明文存储敏感信息 | 立即修复，修复前禁止输出 |
| **P1** | 建议修复：性能瓶颈、代码冗余、死代码、不符合语言规范、资源未释放 | 输出但不强制修复 |
| **P2** | 可选优化：命名规范、注释补充、可读性提升、代码结构微调 | 仅在用户要求时输出 |

### 审查输出格式
```
## 代码审查报告

### 整体评估
[简洁描述代码质量、风险等级、建议]

### P0 严重问题（必须修复）
| 编号 | 位置 | 问题描述 | 潜在后果 |
|-----|------|---------|---------|
| P0-1 | file.py:123 | SQL拼接 | SQL注入风险 |

### P1 警告问题（建议修复）
| 编号 | 位置 | 问题描述 | 优化建议 |
|-----|------|---------|---------|
| P1-1 | file.py:456 | 重复代码 | 提取为函数 |

### P2 优化建议（可选）
| 编号 | 位置 | 建议内容 |
|-----|------|---------|
| P2-1 | file.py:789 | 变量命名可读性提升 |
```

### 禁止行为
- ❌ 只指出问题，不擅自修改用户代码（除非用户明确要求修复）
- ❌ 区分'风格偏好'和'客观问题'，前者标记为 Suggestion
- ❌ 审查范围限于提供的代码，不猜测未展示的部分
- ❌ 对每处 P0 问题必须解释潜在后果

---

## 第七原则：安全加固 - 深度安全规范

**优先级：P0 强制执行**

### 安全检查清单

#### 1. 输入验证
- [ ] 所有输入必须在边界处验证（类型、长度、范围、格式）
- [ ] 拒绝黑名单，使用白名单验证
- [ ] 尽早失败（fail-fast），不在内部传播脏数据
- [ ] 错误信息不泄露内部实现细节

#### 2. 注入防御
- [ ] SQL：强制使用参数化查询/ORM，禁止字符串拼接
- [ ] 命令：禁止直接拼接用户输入到系统命令
- [ ] 路径：验证并规范化路径，禁止目录遍历
- [ ] HTML/JS：输出时编码，使用模板引擎自动转义

#### 3. 密钥管理
- [ ] 禁止硬编码密码/API Key/Token
- [ ] 使用环境变量或密钥管理服务
- [ ] 日志中脱敏敏感信息
- [ ] 定期轮换凭证

#### 4. Flask 专项检查
- [ ] SQL 查询是否使用参数化（防注入）
- [ ] 密码是否哈希存储（werkzeug.security）
- [ ] Session 是否配置 `secret_key`
- [ ] API 是否检查认证状态
- [ ] 敏感配置是否使用环境变量

### 禁止行为
- ❌ 禁止信任客户端传来的任何数据
- ❌ 禁止在日志中输出敏感字段
- ❌ 禁止禁用安全校验

---

## 第八原则：测试驱动 - 任何修改必须有测试覆盖

**优先级：P0（Bug修复）/ P1（一般修改）**

### 测试要求

| 修改类型 | 测试要求 | 覆盖率要求 |
|---------|---------|---------|
| Bug 修复 | 必须先写回归测试（复现 Bug） | 100% 复现用例 |
| 新功能 | 单元测试覆盖率 >= 80% | 行覆盖 >= 80% |
| 重构 | 原有测试全部通过 | 0% 新增失败 |
| 性能优化 | 基准测试对比 | 前后对比数据 |

### 测试命名规范
```
# 好的命名
test_returns_empty_list_when_input_is_null
test_raises_value_error_for_negative_amount
test_user_cannot_access_other_users_data

# 坏的命名
test1
test_function
test_case
```

### 禁止行为
- ❌ 禁止提交被注释掉的测试
- ❌ 禁止提交跳过的测试（skip/xit/pending）
- ❌ 测试失败时必须提供清晰的错误信息，禁止裸 assert

---

## 各语言专属规则增强包

### 自动识别规则
自动读取 Trae 当前打开的文件后缀、项目配置文件，自动识别目标语言和版本。

### Python 专属规则
1. 禁止为了「面向对象」而写类，能用函数实现的绝不写类
2. 遵循 PEP8 规范，优先使用内置函数/标准库
3. 禁止过度使用装饰器、元类、黑魔法语法
4. 异常捕获指定类型，禁止裸 `except:`
5. 优先 `pathlib` 而非 `os.path`
6. 优先 `dataclasses` 而非手写 `__init__`
7. async 函数禁止阻塞调用（time.sleep, requests.get）

### C++ 专属规则
1. 优先使用 RAII 机制，默认使用智能指针管理内存
2. 禁止裸 new/delete
3. 遵循 Rule of Zero / Rule of Five
4. 使用 `enum class` 替代 `enum`
5. 使用 `[[nodiscard]]` 标记重要返回值

### Java 专属规则
1. 避免过度设计模式，能用简单类不用接口
2. 遵循 Java 官方编码规范
3. 必须正确处理异常，禁止空 catch 块
4. 优先 `final` 类/方法/变量
5. 使用 `Optional` 替代 null 返回

### Go 专属规则
1. 错误立即处理，不传播裸 error
2. 使用 `fmt.Errorf` with `%w` 包装错误
3. 接受接口，返回结构体
4. 使用 `context.Context` 传递取消信号
5. 禁止 goroutine 泄漏

### JavaScript/TypeScript 专属规则
1. 启用 strict 模式，禁止 any
2. 使用 `unknown` 替代 any，使用时类型收窄
3. 优先 `const/let`，禁止 `var`
4. 使用 `=== / !==`，禁止 `==`
5. 优先 async/await 替代 Promise 链
6. **浏览器兼容性**：如果目标环境不确定，避免 `?.` `??` 等 ES2020+ 语法

---

## 专项技能协同规则

### 协同技能清单

| 专项技能 | 触发条件 | 协同优先级 |
|---------|---------|-----------|
| **frontend-compatibility** | 修改 `.html/.css/.js` 文件时 | 高优先级补充 |
| **flask-web-dev** | 开发 Flask 后端应用时 | 高优先级补充 |
| **hybrid-python-web** | 同时涉及前后端开发时 | 强制协同 |

### 协同执行规则

1. **Flask 项目**：自动补充 Flask 专项安全检查清单
2. **前端项目**：自动启用 `frontend-compatibility` 兼容性检查
3. **混合项目**：自动启用 `hybrid-python-web` 前后端协调

### 冲突解决
- 如果专项技能要求与 Karpathy 极简原则冲突，优先遵循 Karpathy 核心原则
- 但如果涉及安全性问题（P0），专项技能的安全要求优先
- 兼容性问题是特殊场景，以专项技能为准

---

## 场景化输出模板

### 【新功能开发场景】
输出顺序：需求确认清单 → 方案选型对比 → 执行计划 → 完整代码 → 验证方法

### 【Bug修复场景】
输出顺序：MCVE复现 → 根因分析 → 修复方案 → 修复代码 → 回归测试

### 【代码审查场景】
输出顺序：整体评估 → P0/P1/P2 分级问题列表 → 修复代码示例 → 风险说明

### 【代码重构场景】
输出顺序：重构目标 → 重构前后对比 → 完整代码 → 兼容性说明 → 验证方法

### 【性能优化场景】
输出顺序：基准数据 → 瓶颈分析 → 优化假设 → 优化实现 → 前后对比

---

## 用户分层适配开关

| 模式 | 触发关键词 | 输出特点 |
|-----|-----------|---------|
| **新手模式** | 「新手模式」 | 逐行注释、详细讲解、完整步骤 |
| **专家模式** | 「专家模式」 | 极简代码、核心 diff、关键说明 |
| **定制开关** | 【无注释】【仅diff】【带测试】 | 按需定制输出内容 |

---

## 异常场景强制处理规则

| 场景 | 处理方式 |
|-----|---------|
| 代码不全/上下文缺失 | 必须先向用户索要完整代码、依赖文件，绝不猜测 |
| 需求模糊/不明确 | 必须先输出「需求拆解与确认清单」，列出假设和歧义点 |
| 安全风险需求 | 必须先指出风险，给出安全方案，绝不直接实现有风险的代码 |
| 编译/运行错误 | 必须先定位错误根因，只修改错误相关代码 |
| 超出能力范围 | 必须明确告知原因，给出可行替代方案 |

---

## 自动降级规则

| 复杂度 | 场景 | 处理方式 |
|-------|------|---------|
| **极简** | 拼写修改、单行调整 | 跳过确认步骤，直接输出 |
| **中等** | 单函数修改 | 跳过完整计划，直接代码+说明 |
| **复杂** | 多文件修改、核心重构 | 必须遵循全流程规则 |

---

## 第九原则：性能优化 - 数据驱动的量化优化

**优先级：P1（明确性能问题时触发）**

### 优化方法论

#### 1. 量化基准（Measurement）
- **规则**：不测量，不优化
- **要求**：
  - 提供性能基准：当前耗时/内存/CPU 指标
  - 使用语言标准分析工具（cProfile/py-spy/gprof/Valgrind）
  - 识别真正的瓶颈（通常只有 1-2 个热点函数）
  - 区分：算法复杂度问题 vs 常数时间问题 vs 系统调用问题

#### 2. 瓶颈分类与策略
| 瓶颈类型 | 优化策略 | 优先级 |
|---------|---------|--------|
| **算法复杂度** | O(n²)→O(n log n)，O(n)→O(1) | P0 |
| **IO密集** | 批量操作、异步I/O、连接池 | P1 |
| **内存密集** | 对象池、流式处理、减少装箱 | P2 |
| **CPU密集** | 向量化、减少分支预测失败 | P2 |

#### 3. 优化代价评估
- **可读性代价**：优化后代码是否难以维护？
- **内存代价**：时间优化是否大幅增加内存？
- **复杂度代价**：是否引入并发/异步等复杂机制？
- **可移植性代价**：是否依赖特定平台特性？

### 量化退出条件
- ✅ 基准测试数据已记录
- ✅ 优化后性能提升可量化（> 20%）
- ✅ 可读性代价已评估
- ✅ 无引入新安全风险

---

## 第十原则：重构规范 - 系统性代码整理

**优先级：P1（明确重构需求时触发）**

### 重构前置条件
1. 确认当前代码有测试覆盖（无测试则先建议补测试）
2. 识别代码异味：长函数、大类、重复、过长参数列表
3. 制定重构计划：列出步骤和预期结果

### 重构技术目录

#### 函数级重构
| 技术 | 触发条件 | 操作 |
|-----|---------|------|
| **Extract Function** | 函数 > 30 行或嵌套 > 3 层 | 拆分为多个小函数 |
| **Inline Function** | 函数体比调用更简单 | 内联调用点 |
| **Introduce Parameter Object** | 参数 > 4 个 | 封装为数据类 |
| **Replace Temp with Query** | 临时变量被多次使用 | 提取为函数 |

#### 条件级重构
| 技术 | 触发条件 | 操作 |
|-----|---------|------|
| **Decompose Conditional** | 复杂条件表达式 | 提取为命名函数 |
| **Consolidate Conditional** | 重复条件判断 | 合并为单一检查 |
| **Replace Conditional with Polymorphism** | 同类条件多次出现 | 使用多态替代 |

#### 数据级重构
| 技术 | 触发条件 | 操作 |
|-----|---------|------|
| **Replace Magic Number** | 硬编码数字/字符串 | 使用具名常量 |
| **Extract Variable** | 复杂表达式 | 提取为中间变量 |

### 小步快跑原则
1. 每次只做一个重构操作
2. 每次修改后代码必须可编译/可运行
3. 保持行为不变：输入输出、副作用、异常行为完全一致
4. 频繁运行测试验证

### 量化退出条件
- ✅ 行为等价：原有测试全部通过
- ✅ 圈复杂度下降或持平
- ✅ 无引入新的代码异味

---

## 第十一原则：测试分层 - 测试金字塔实践

**优先级：P1（编写测试时触发）**

### 测试分层模型

```
         ▲
        /E\            E2E Test (5-10%)
       /2E2\
      /─────\          Integration Test (20-30%)
     /       \
    /─────────\        Unit Test (60-70%)
   /           \
  /─────────────\
```

| 层级 | 职责 | 特征 | 数量占比 |
|-----|------|------|---------|
| **Unit Test** | 函数级验证 | 毫秒级、无I/O、隔离 | 60-70% |
| **Integration Test** | 模块交互验证 | 真实依赖、跨组件 | 20-30% |
| **E2E Test** | 用户场景验证 | 完整链路、仅关键路径 | 5-10% |

### 各层测试规范

#### Unit Test 标准
```python
# ✅ 好的单元测试
def test_user_registration_valid_email():
    """有效的邮箱应该注册成功"""
    result = register_user("user@example.com", "password123")
    assert result.success is True
    assert result.user.email == "user@example.com"

# ✅ 边界条件
def test_user_registration_invalid_email():
    """无效邮箱应该返回错误"""
    result = register_user("invalid-email", "password123")
    assert result.success is False
    assert "email" in result.error.message
```

#### Integration Test 标准
```python
# ✅ API 集成测试
def test_course_creation_flow():
    """创建课程并验证持久化"""
    course = create_course({"title": "Python", "language_id": 1})
    retrieved = get_course(course.id)
    assert retrieved.title == "Python"
```

#### E2E Test 标准
```python
# ✅ 关键路径 E2E
def test_user_complete_lesson():
    """用户完成单词学习并验证进度"""
    login("user@example.com")
    start_lesson("english-101")
    complete_all_words()
    assert get_progress() == 100
```

### Mock 使用规范
- **Unit Test**：可使用 Mock/Stub 隔离依赖
- **Integration Test**：使用真实依赖或轻量 Mock
- **E2E Test**：禁止 Mock，使用真实系统

### 量化退出条件
- ✅ 新增代码单元测试覆盖率 >= 80%
- ✅ 关键路径 E2E 测试通过
- ✅ 无跳过/注释掉的测试

---

## 第十二原则：并发编程 - 线程安全规范

**优先级：P1（涉及多线程/异步时触发）**

### Go 并发规范

| 规则 | 说明 | 优先级 |
|-----|------|-------|
| **goroutine 泄漏检查** | 所有 goroutine 必须有退出机制 | P0 |
| **context 传播** | 使用 context.Context 传递取消信号 | P0 |
| **channel 关闭** | 只由发送方关闭 channel | P1 |
| **sync.Mutex vs channel** | 数据竞争用 mutex，简单消息用 channel | P1 |

```go
// ✅ 正确的 goroutine 管理
func process(ctx context.Context, jobs <-chan Job) error {
    for job := range jobs {
        select {
        case <-ctx.Done():
            return ctx.Err()
        default:
            if err := handle(job); err != nil {
                return err
            }
        }
    }
    return nil
}
```

### C++ 并发规范

| 规则 | 说明 | 优先级 |
|-----|------|-------|
| **RAII 锁管理** | 使用 std::lock_guard/std::unique_lock | P0 |
| **避免数据竞争** | 不可变数据优先，或使用原子操作 | P0 |
| **线程局部存储** | 使用 thread_local 而非全局变量 | P1 |

```cpp
// ✅ 正确的锁管理
std::mutex mtx;
void safe_increment() {
    std::lock_guard<std::mutex> lock(mtx);
    counter++;
}
```

### Python asyncio 规范

| 规则 | 说明 | 优先级 |
|-----|------|-------|
| **禁止阻塞调用** | async 函数禁止 time.sleep/requests.get | P0 |
| **正确传播取消** | 使用 asyncio.CancellationToken | P1 |
| **并发执行** | 使用 asyncio.gather 而非顺序 await | P1 |

### 量化退出条件
- ✅ 无数据竞争（通过 threadsanitizer/race detector 验证）
- ✅ goroutine 有明确退出路径
- ✅ 锁粒度最小化，无死锁风险

---

## 第十三原则：DevOps 规范 - CI/CD 集成

**优先级：P2（项目需要自动化时触发）**

### CI/CD 核心检查项

#### 1. 代码质量门禁
| 检查项 | 工具示例 | 阈值 |
|-------|---------|------|
| 单元测试覆盖率 | coverage.py / jest | >= 80% |
| 代码风格 | pylint / eslint | 0 errors |
| 安全扫描 | bandit / npm audit | 0 高危漏洞 |
| 依赖漏洞 | pip-audit / cargo audit | 0 高危漏洞 |

#### 2. 自动化测试流水线
```
commit → lint → test → coverage → security → deploy
```

#### 3. 容器化最佳实践
```dockerfile
# ✅ 多阶段构建
FROM python:3.11-slim AS builder
COPY requirements.txt .
RUN pip install --prefix=/deps -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /deps /usr/local
COPY . .
CMD ["python", "app.py"]
```

### 安全门禁
- [ ] 禁止在 CI 中存储生产密钥
- [ ] 使用环境变量注入敏感配置
- [ ] 镜像扫描报告无高危漏洞
- [ ] 依赖版本锁定（requirements.txt/Pipfile.lock）

### 量化退出条件
- ✅ CI 流水线通过率 100%
- ✅ 测试覆盖率达标
- ✅ 安全扫描无高危漏洞

---

## 版本更新日志

### v4.0.0（当前版本）
- 新增第九原则：性能优化方法论（量化基准、瓶颈分类、优化代价）
- 新增第十原则：重构技术目录（Extract/Inline/表驱动等 9 种技术）
- 新增第十一原则：测试分层金字塔（Unit/Integration/E2E 规范）
- 新增第十二原则：并发编程规范（Go goroutine、C++ mutex、Python asyncio）
- 新增第十三原则：DevOps/CI 规范（质量门禁、容器化最佳实践）
- 综合编码水平评估：B+ → A-

### v3.0.0
- 整合 trae-skill-import 的 Bug-Fix 根因分析方法论
- 整合 Code-Review 分级审查（P0/P1/P2）
- 整合 Security-Hardening 安全检查清单
- 整合 Test-Driven 测试要求
- 新增各语言专项规则（Python async、C++ RAII、Go error handling 等）
- 优化退出条件，添加量化指标
- 简化协同规则，避免与主线冲突

### v2.1.1
- 优化协同规则，新增 Skills 快速索引

### v2.1.0
- 新增专项技能协同规则

### v2.0.0
- 全量优化升级，新增触发规则、强制自检

### v1.0.0
- 初始版本

---

## 技能 2: Flask Web Dev

# Flask Web 开发规范

专门针对 Flask 框架的后端开发最佳实践，涵盖路由设计、模板渲染、数据库操作、认证安全和错误处理。

## 自动触发条件

**强触发**：
- 文件后缀为 `.py` 且包含 `flask`、`Flask`、`@app` 关键词
- 用户提及 "Flask"、"后端"、"API"、"路由"
- 开发 Web 应用、REST API、模板渲染

**补充触发**（Karpathy 技能可调用）：
- 涉及数据库操作的 Python 代码
- 涉及用户认证、会话管理的场景
- 涉及文件上传、JSON API 开发的场景

## 核心规则

### 1. 项目结构规范

**推荐的 Flask 项目结构**：
```
project/
├── app.py              # 主应用入口
├── templates/          # HTML 模板
│   └── index.html
├── static/            # 静态文件
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt    # 依赖清单
└── instance/          # SQLite 数据库（如果使用）
```

**禁止**：
- ❌ 所有代码都写在 `app.py`（超过 500 行）
- ❌ 模板文件和 Python 文件混放
- ❌ 敏感信息硬编码在代码中

**推荐**：
- ✅ 使用 `blueprints` 组织大型应用
- ✅ 配置信息放在 `config.py` 或环境变量
- ✅ 数据库连接封装为独立模块

### 2. 路由设计规范

**基础路由**：
```python
# ✅ Good: RESTful 风格路由
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """获取课程列表"""
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """获取单个课程"""
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict())
```

**路由分组（蓝图）**：
```python
# ✅ Good: 使用蓝图组织路由
from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/courses')
def get_courses():
    return jsonify([])

@api.route('/lessons/<int:lesson_id>')
def get_lesson(lesson_id):
    return jsonify({})
```

**禁止**：
- ❌ 路由中使用复杂业务逻辑
- ❌ 在路由中直接写 SQL 语句（应封装到模型层）

### 3. JSON API 响应规范

**统一响应格式**：
```python
from flask import jsonify

def success_response(data, message="Success", status_code=200):
    """统一成功响应格式"""
    return jsonify({
        'success': True,
        'message': message,
        'data': data
    }), status_code

def error_response(message, error_code=None, status_code=400):
    """统一错误响应格式"""
    response = {
        'success': False,
        'message': message
    }
    if error_code:
        response['error_code'] = error_code
    return jsonify(response), status_code

# 使用示例
@app.route('/api/courses/<int:course_id>')
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return error_response('课程不存在', 'NOT_FOUND', 404)
    return success_response(course.to_dict())
```

**API 版本控制**：
```python
# ✅ Good: URL 版本控制
@app.route('/api/v1/courses')  # v1 版本
@app.route('/api/v2/courses')  # v2 版本
```

### 4. 数据库操作规范

**使用上下文管理器**：
```python
# ✅ Good: 明确的连接管理
import sqlite3
from contextlib import contextmanager

DATABASE = 'instance/app.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# 使用
with get_db() as conn:
    c = conn.cursor()
    c.execute('SELECT * FROM courses')
    courses = [dict(row) for row in c.fetchall()]
```

**禁止**：
- ❌ 全局变量持有数据库连接
- ❌ SQL 语句字符串拼接（存在注入风险）
- ❌ 不关闭数据库连接

**使用参数化查询**：
```python
# ✅ Good: 参数化查询防注入
c.execute('SELECT * FROM users WHERE email = ?', (email,))

# ❌ Bad: 字符串拼接
c.execute('SELECT * FROM users WHERE email = "' + email + '"')
```

### 5. 认证与会话安全

**密码处理**：
```python
import hashlib
import secrets

def hash_password(password, salt=None):
    """密码哈希 - 使用 SHA256 + salt"""
    if salt is None:
        salt = secrets.token_hex(16)
    hash_obj = hashlib.sha256((password + salt).encode())
    return salt + hash_obj.hexdigest()

def verify_password(password, hashed):
    """验证密码"""
    salt = hashed[:32]
    return hash_password(password, salt) == hashed

# 使用
hashed = hash_password('user_password')
if verify_password(input_password, stored_hash):
    # 登录成功
    session['user_id'] = user_id
```

**Session 安全配置**：
```python
from flask import Flask, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # 生产环境必须使用强随机密钥

# Session 配置
app.config.update(
    SESSION_COOKIE_SECURE=True,      # 仅 HTTPS 传输
    SESSION_COOKIE_HTTPONLY=True,    # 禁止 JavaScript 访问
    SESSION_COOKIE_SAMESITE='Lax',  # CSRF 防护
    PERMANENT_SESSION_LIFETIME=3600  # 1小时过期
)
```

**禁止**：
- ❌ 使用简单哈希或不哈希存储密码
- ❌ 在 URL 中传递认证 token
- ❌ Session 不设置过期时间

### 6. 错误处理规范

**全局错误处理器**：
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(f'Unhandled exception: {error}')
    return jsonify({'error': 'An unexpected error occurred'}), 500
```

**API 错误响应**：
```python
@app.route('/api/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    try:
        lesson = get_lesson_from_db(lesson_id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        return jsonify(lesson), 200
    except DatabaseError as e:
        app.logger.error(f'Database error: {e}')
        return jsonify({'message': 'Database error'}), 500
```

### 7. 模板渲染规范

**模板路径**：
```python
# ✅ 模板放在 templates 目录
# Flask 会自动在 templates/ 目录下查找
@app.route('/')
def index():
    return render_template('index.html')

# ❌ 不要使用绝对路径
return render_template('/Users/name/project/templates/index.html')
```

**模板数据过滤**：
```python
# ✅ 传递数据前过滤敏感信息
def sanitize_user_data(user):
    return {
        'id': user['id'],
        'username': user['username'],
        # 不包含 password_hash, email 等敏感信息
    }

@app.route('/profile')
def profile():
    user = get_user(session['user_id'])
    return render_template('profile.html', user=sanitize_user_data(user))
```

## 强制检查清单

**代码提交前**：
1. [ ] 所有 SQL 查询使用参数化查询
2. [ ] 用户密码使用 hashlib 哈希存储
3. [ ] Session 配置了 `secret_key`
4. [ ] API 路由有认证检查（`if 'user_id' not in session`）
5. [ ] 敏感配置使用环境变量而非硬编码
6. [ ] 所有异常都被捕获或记录日志
7. [ ] 数据库连接正确关闭

**API 开发**：
1. [ ] 统一的成功/错误响应格式
2. [ ] 适当的 HTTP 状态码（200, 201, 400, 401, 404, 500）
3. [ ] CORS 配置正确（如果前后端分离）

## 场景化输出

### 【新 API 开发】
```
输出顺序：路由设计 → 请求参数校验 → 数据库操作 → 响应格式 → 错误处理
```

### 【修复安全漏洞】
```
输出顺序：漏洞定位 → 风险评估 → 修复方案 → 验证方法
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 整体编码原则指导
- **frontend-compatibility**: 前端代码兼容性检查

## 版本更新日志
- v1.0.0 - 初始版本，基于 Flask 官方最佳实践和常见安全规范

---

## 技能 3: Frontend Compatibility

# 前端兼容性检查

专门针对 HTML/CSS/JavaScript 代码的浏览器兼容性问题检测和处理。

## 自动触发条件

**强触发**（满足任一条件即启用）：
- 文件后缀为 `.html`, `.css`, `.js`
- 用户提及"前端"、"界面"、"交互"、"浏览器兼容"
- 进行 UI 功能开发、DOM 操作、事件处理

**弱触发**（Karpathy 技能可补充调用）：
- Flask 项目中 templates 目录下的文件
- 任何包含 HTML/CSS/JS 代码的上下文

## 核心规则

### 1. JavaScript ES6+ 语法兼容性检查

**禁止使用的语法**（除非确认目标环境支持）：
```javascript
// ❌ 可选链操作符 - IE11 及部分旧版浏览器不支持
const value = obj?.property?.nested;

// ✅ 替代方案
const value = obj && obj.property && obj.property.nested;

// ❌ 空值合并运算符 - 部分浏览器不支持
const result = value ?? 'default';

// ✅ 替代方案
const result = value !== null && value !== undefined ? value : 'default';

// ❌ 逻辑空赋值 -= 部分浏览器不支持
x ??= 'default';

// ✅ 替代方案
if (x === null || x === undefined) x = 'default';
```

**模板字符串兼容性处理**：
```javascript
// ✅ 模板字符串 - 现代浏览器都支持，但避免嵌套复杂逻辑
const html = '<div>' + item.name + '</div>';

// ❌ 如果必须使用模板字符串，避免以下模式
const html = `<div class="${item.matched ? 'active' : ''}">${getName()}</div>`;

// ✅ 简化版本 - 兼容性更好
var className = 'match-item';
if (item.matched) className += ' matched';
var div = '<div class="' + className + '">' + item.text + '</div>';
```

### 2. DOM 和事件处理兼容性

**事件对象处理**：
```javascript
// ❌ 可能的问题代码
element.addEventListener('click', (event) => {
    event?.target?.classList.add('active');
});

// ✅ 兼容版本
element.addEventListener('click', function(e) {
    var target = e.target || e.srcElement;
    if (target) {
        target.classList.add('active');
    }
});

// ✅ 或者使用事件委托
element.addEventListener('click', function(e) {
    var target = e.target || e.srcElement;
    if (target && target.classList.contains('match-item')) {
        // 处理逻辑
    }
});
```

**可选参数默认值处理**：
```javascript
// ❌ 问题代码
function showSection(sectionId, eventObj = null) {
    eventObj?.target?.classList.add('active');
}

// ✅ 兼容版本
function showSection(sectionId, eventObj) {
    var sections = ['home', 'courses'];
    // 基础逻辑

    if (eventObj && eventObj.target) {
        eventObj.target.classList.add('active');
    }
}
```

### 3. CSS 兼容性

**Flexbox 和 Grid**：
```css
/* ✅ 现代 Flexbox - iOS Safari 7+, Android Browser 4.4+ 支持 */
.container {
    display: -webkit-flex;  /* iOS 6, Safari 3.1-6 */
    display: flex;
}

/* ✅ CSS Grid - IE不支持，需要回退方案 */
.grid {
    display: -ms-grid;  /* IE 10 */
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
```

**CSS 变量**：
```css
/* ✅ CSS 变量 - IE不支持 */
:root {
    --primary-color: #667eea;
}

/* ✅ 回退方案 */
.btn {
    background: #667eea;  /* IE 回退值 */
    background: var(--primary-color, #667eea);  /* 现代浏览器 */
}
```

### 4. Fetch API 和 Promise 兼容性

```javascript
// ❌ Fetch API - IE完全不支持
fetch('/api/data')
    .then(response => response.json())
    .catch(error => console.error(error));

// ✅ 兼容版本 - 需要 polyfill 或 XMLHttpRequest
// 方案1: 添加 polyfill
// <script src="https://cdn.jsdelivr.net/npm/whatwg-fetch@3.6.2/fetch.min.js"></script>

// 方案2: 使用 XMLHttpRequest
function apiCall(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            callback(null, JSON.parse(xhr.responseText));
        } else {
            callback(new Error('HTTP ' + xhr.status));
        }
    };
    xhr.onerror = function() {
        callback(new Error('Network error'));
    };
    xhr.send();
}
```

## 强制检查清单

**JavaScript 代码修改前**：
1. [ ] 检查是否使用了 `?.` 可选链操作符 → 替换为 `&&` 链式调用
2. [ ] 检查是否使用了 `??` 空值合并 → 替换为三元运算符
3. [ ] 检查 `event?.target` 模式 → 替换为 `if (event && event.target)`
4. [ ] 检查模板字符串中的复杂表达式 → 简化为字符串拼接
5. [ ] 检查 `classList.contains()` 兼容性 → 现代浏览器都支持，无需修改

**CSS 代码修改前**：
1. [ ] 检查是否使用了 `var()` CSS 变量 → 添加回退值
2. [ ] 检查 `display: grid` → 确认不需要支持 IE
3. [ ] 检查 `position: sticky` → iOS Safari 7.1+ 才支持

## 场景化输出

### 【新前端功能开发】
```
输出顺序：兼容性检查 → 备选方案 → 建议实现 → 验证方法
```

### 【修复浏览器兼容性问题】
```
输出顺序：问题定位 → 根因分析 → 修复方案 → 测试建议
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 极简编码原则
- **hybrid-python-web**: 前后端协作协调

## 版本更新日志
- v1.0.0 - 初始版本，整合 Web 开发中的常见兼容性问题

---

## 技能 4: Hybrid Python Web

# 混合 Python Web 开发指南

专门协调 Python 后端（Flask/FastAPI/Django）与 HTML/CSS/JS 前端的协同开发，解决上下文切换、API 设计、数据传递等问题。

## 自动触发条件

**强触发**：
- 项目同时包含 `.py` 后端文件和 `.html`/`.js` 前端文件
- 用户提及"前后端"、"API"、"模板"、"静态文件"
- 开发全栈 Web 应用（从数据库到界面）

**补充触发**（Karpathy 技能可调用）：
- 前后端数据交互场景
- 模板渲染与 JavaScript 交互
- CORS、认证token、session 共享

## 核心规则

### 1. 项目架构决策

**前后端分离 vs 模板渲染**：

```python
# 方案A: 完全前后端分离（推荐大型项目）
# 后端只提供 API
@app.route('/api/courses')
def get_courses():
    return jsonify(courses)

# 前端独立部署
# <script src="https://frontend.example.com/app.js">

# 方案B: Flask 模板渲染（中小型项目）
@app.route('/')
def index():
    return render_template('index.html')

# 方案C: API + 前端静态文件（混合 - 本项目采用）
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/<path:path>')
def api(path):
    return jsonify(handle_api(path))
```

**本项目选择方案C**，原因：
- 简单依赖（仅 Flask）
- 无需前端构建工具
- 便于快速迭代

### 2. API 设计协调

**前后端约定的 API 格式**：

```python
# ✅ 后端: 统一 JSON 响应
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = load_courses()
    return jsonify(courses)  # 自动设置 Content-Type: application/json
```

```javascript
// ✅ 前端: fetch API 调用
async function loadCourses() {
    try {
        const response = await fetch('/api/courses');
        if (!response.ok) {
            throw new Error('HTTP ' + response.status);
        }
        const courses = await response.json();
        renderCourses(courses);
    } catch (error) {
        showError('加载失败: ' + error.message);
    }
}
```

**请求头配置**：
```python
# ✅ 后端: 允许跨域（如果前后端分离部署）
from flask_cors import CORS
CORS(app, supports_credentials=True)

# 或者手动设置
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response
```

```javascript
// ✅ 前端: 带凭证的请求（Cookie/Session）
const response = await fetch('/api/data', {
    credentials: 'include'  // 发送 Cookie
});
```

### 3. 数据传递模式

**场景1: 模板渲染传递数据**（方案B）
```python
# 后端
@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    stats = get_user_stats(user.id)
    return render_template('dashboard.html',
                          username=user.username,
                          stats=stats)
```

```html
<!-- 模板中直接使用 -->
<h1>欢迎, {{ username }}</h1>
<p>学习时长: {{ stats.hours }}小时</p>
```

**场景2: API 动态加载**（方案C - 本项目采用）
```python
# 后端
@app.route('/api/stats')
def get_stats():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    stats = get_user_stats(session['user_id'])
    return jsonify(stats)
```

```javascript
// 前端
async function loadStats() {
    const stats = await apiCall('/stats');
    document.getElementById('hours').textContent = stats.total_hours;
}
```

**禁止**：
- ❌ 模板中执行复杂 JavaScript 逻辑
- ❌ 后端直接返回 HTML 片段（应返回 JSON）
- ❌ 前端拼接 SQL 语句

### 4. 认证状态同步

**Session 认证流程**：
```python
# ✅ 后端: 登录时创建 session
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = verify_credentials(data['email'], data['password'])

    if user:
        session['user_id'] = user['id']  # Flask session
        session.permanent = True
        return jsonify({
            'success': True,
            'user': {'id': user['id'], 'username': user['username']}
        })
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
```

```javascript
// ✅ 前端: 登录后保存状态
async function handleLogin(credentials) {
    const result = await apiCall('/login', 'POST', credentials);

    if (result.success) {
        localStorage.setItem('user', JSON.stringify(result.user));
        updateUIForLoggedInUser(result.user);
        showFlash('登录成功', 'success');
    }
}
```

**状态检查**：
```python
# ✅ 后端: 所有需要认证的 API 检查 session
@app.route('/api/words/practice', methods=['POST'])
def practice_word():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    # 处理请求...
```

```javascript
// ✅ 前端: 调用前检查登录状态
async function startPractice() {
    if (!localStorage.getItem('user')) {
        showLoginPrompt();  // 引导用户登录
        return;
    }
    const words = await apiCall('/words');
    // 开始练习...
}
```

### 5. 错误处理协调

**后端错误响应**：
```python
# ✅ 统一错误格式
@app.route('/api/lessons/<int:lesson_id>')
def get_lesson(lesson_id):
    try:
        lesson = Lesson.query.get(lesson_id)
        if not lesson:
            return jsonify({'error': 'NOT_FOUND', 'message': '课时不存在'}), 404
        return jsonify(lesson.to_dict())

    except DatabaseError as e:
        app.logger.error(f'Database error for lesson {lesson_id}: {e}')
        return jsonify({'error': 'DB_ERROR', 'message': '数据库错误'}), 500

    except Exception as e:
        app.logger.error(f'Unexpected error: {e}')
        return jsonify({'error': 'INTERNAL_ERROR', 'message': '服务器错误'}), 500
```

**前端错误处理**：
```javascript
// ✅ 统一的 API 调用错误处理
async function apiCall(url, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include'  // 发送 session cookie
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch('/api' + url, options);

        // 检查 HTTP 状态码
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || `HTTP ${response.status}`);
        }

        // 尝试解析 JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        }

        return await response.text();

    } catch (error) {
        console.error('API call failed:', url, error);
        showFlash('操作失败: ' + error.message, 'error');
        throw error;  // 重新抛出让调用方处理
    }
}

// ✅ 业务逻辑层错误处理
async function loadLessons() {
    try {
        showLoading();
        const lessons = await apiCall('/lessons');
        renderLessons(lessons);
    } catch (error) {
        // 不要在 catch 中重复 showFlash，apiCall 已处理
        renderEmptyState('暂无课时数据');
    } finally {
        hideLoading();
    }
}
```

### 6. 开发工作流

**文件结构**：
```
project/
├── app/                  # Flask 应用模块
│   ├── __init__.py       # 应用工厂
│   ├── routes.py          # 路由定义
│   ├── models.py          # 数据模型
│   ├── utils.py          # 工具函数
│   ├── errors.py         # 错误处理
│   ├── constants.py      # 常量定义
│   └── templates/        # 模板文件
│       └── index.html
├── instance/             # SQLite 数据库
│   └── language_learning.db
├── requirements.txt
└── run.py                # 应用入口
```

**调试技巧**：
```python
# ✅ 后端: 添加请求日志
import logging
logging.basicConfig(level=logging.DEBUG)

@app.before_request
def log_request():
    app.logger.debug(f'{request.method} {request.path}')

# ✅ 前端: API 调试
async function apiCall(url, method, data) {
    console.log(`API Call: ${method} ${url}`, data);
    const result = await actualFetch(...);
    console.log(`API Response: ${url}`, result);
    return result;
}
```

**热重载配置**：
```python
# Flask 开发模式自动重载
# 启动命令: flask run --debug
# 或代码中:
if __name__ == '__main__':
    app.debug = True  # 仅开发环境！
    app.run(host='0.0.0.0', port=5000)
```

## 强制检查清单

**前后端协作**：
1. [ ] API 响应格式统一（成功/错误）
2. [ ] 前端正确处理 401 未授权
3. [ ] Session/Cookie 认证配置 `credentials: 'include'`
4. [ ] 后端设置正确的 CORS 头（如果需要）
5. [ ] API 错误返回有意义的错误信息

**数据一致性**：
1. [ ] 前端显示的数据字段与后端 JSON key 一致
2. [ ] 类型一致（字符串 vs 数字 vs 布尔）
3. [ ] 空值处理（后端返回 `null` vs 前端期望 `[]`）

**用户体验**：
1. [ ] 加载状态显示（`showLoading()`/`hideLoading()`）
2. [ ] 错误提示（`showFlash(message, 'error')`）
3. [ ] 操作反馈（成功/失败/进行中）
4. [ ] 进度指示（百分比/步骤数）

## 常见问题解决方案

**Q: 前后端时间戳不一致？**
```python
# 后端返回 ISO 格式
from datetime import datetime
return jsonify({'created_at': datetime.now().isoformat()})
```

```javascript
// 前端解析
const date = new Date(data.created_at);
document.getElementById('time').textContent = date.toLocaleString();
```

**Q: 中文乱码？**
```python
# 后端设置 UTF-8
# Python 文件开头: # -*- coding: utf-8 -*-
# HTML 声明: <meta charset="UTF-8">

@app.route('/api/courses')
def get_courses():
    return jsonify(courses)  # Flask 自动处理 UTF-8
```

**Q: 文件上传大小限制？**
```python
# 后端配置
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large'}), 413
```

## 与其他技能配合

- **universal-karpathy-coding-guidelines**: 极简编码原则
- **flask-web-dev**: Flask 专项规范
- **frontend-compatibility**: 前端代码兼容性

## 版本更新日志
- v1.0.0 - 初始版本，整合前后端协作常见问题

---

## 技能协同规则

当多个技能同时满足触发条件时，按以下优先级协同：

| 场景 | 主技能 | 协同技能 |
|------|--------|----------|
| Flask 后端开发 | universal-karpathy-coding-guidelines | flask-web-dev |
| 前端开发 | universal-karpathy-coding-guidelines | frontend-compatibility |
| 全栈开发 | universal-karpathy-coding-guidelines | flask-web-dev + frontend-compatibility + hybrid-python-web |
| Bug 修复 | universal-karpathy-coding-guidelines | test-driven（回归测试） |
| 代码审查 | universal-karpathy-coding-guidelines | code-review（P0/P1/P2 分级） |

---

## 退出条件

- ✅ 所有修改都能追溯到用户需求
- ✅ 无 P0 级别问题未处理
- ✅ 新增代码有测试覆盖（Bug 修复必须有回归测试）
- ✅ 无硬编码密钥或敏感信息泄露
- ✅ 代码比修改前更易读或更简洁
