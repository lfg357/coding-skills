# 🧠 Trae Coding Skills

> **一套高标准的 AI 辅助编码规范，让 AI 写出人类工程师愿意维护的代码。**

覆盖 **Python、C++、Java、Go、JavaScript/TypeScript、Rust** 等主流语言。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills.sh Compatible](https://img.shields.io/badge/Skills.sh-Compatible-blue)](https://skills.sh)
[![Trae Compatible](https://img.shields.io/badge/Trae-Compatible-green)](https://trae.ai)

---

## 📦 安装

### 方式一：通过 `npx skills` CLI（推荐，支持 50+ 种 AI Agent）

```bash
# 安装所有技能
npx skills add YOUR_USERNAME/trae-coding-skills --all

# 安装特定技能
npx skills add YOUR_USERNAME/trae-coding-skills --skill universal-karpathy-coding-guidelines

# 全局安装（所有项目可用）
npx skills add YOUR_USERNAME/trae-coding-skills --all --global

# 安装到特定 Agent
npx skills add YOUR_USERNAME/trae-coding-skills --all --agent trae
```

### 方式二：手动导入 Trae

1. 下载本仓库 ZIP 或克隆
2. 打开 **Trae → 设置 → 规则和技能 → 技能 → 创建**
3. 上传 `skills/xxx/SKILL.md` 或包含多个 SKILL.md 的 ZIP
4. Trae 自动解析并识别技能

### 方式三：手动复制到项目

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/trae-coding-skills.git

# 复制到 Trae 项目技能目录
cp -r trae-coding-skills/skills/* .trae/skills/

# 或复制到全局技能目录（macOS/Linux）
cp -r trae-coding-skills/skills/* ~/.trae/skills/
```

---

## 🎯 技能清单

| 技能 | 描述 | 触发条件 | 自动触发 |
|------|------|----------|----------|
| **[universal-karpathy-coding-guidelines](skills/universal-karpathy-coding-guidelines/SKILL.md)** | Karpathy 极简编码规范，整合 Bug-Fix、Code-Review、Security、Test-Driven | 代码编写/审查/重构/修复/优化 | ✅ |
| **[flask-web-dev](skills/flask-web-dev/SKILL.md)** | Flask 后端开发最佳实践，路由/模板/数据库/认证/错误处理 | Flask 项目、.py 文件 | ✅ |
| **[frontend-compatibility](skills/frontend-compatibility/SKILL.md)** | 前端兼容性检查，ES6+ 语法/DOM 事件/CSS/Fetch API | .html/.css/.js 文件 | ✅ |
| **[hybrid-python-web](skills/hybrid-python-web/SKILL.md)** | 前后端协同开发，API 设计/数据传递/认证同步/错误协调 | 全栈 Web 项目 | ✅ |

---

## 🏗️ 项目结构

```
trae-coding-skills/
├── skills/                          # 核心技能目录（每个技能一个文件夹）
│   ├── universal-karpathy-coding-guidelines/
│   │   └── SKILL.md                 # 通用编码规范
│   ├── flask-web-dev/
│   │   └── SKILL.md                 # Flask 开发规范
│   ├── frontend-compatibility/
│   │   └── SKILL.md                 # 前端兼容性
│   └── hybrid-python-web/
│       └── SKILL.md                 # 前后端协同
│
├── integrations/                    # IDE 集成配置
│   ├── trae/                        # Trae 导入指南
│   ├── cursor/                      # Cursor .cursorrules
│   ├── vscode/                      # VS Code 设置
│   └── claude/                      # Claude Code 配置
│
├── tools/                           # 辅助工具脚本
│   └── validate-skills.py           # 校验 SKILL.md 格式
│
├── .github/
│   └── workflows/
│       └── validate.yml             # CI 自动校验
│
├── README.md                        # 本文件
├── LICENSE                          # MIT 许可证
└── CONTRIBUTING.md                  # 贡献指南
```

---

## 🔧 技能详情

### universal-karpathy-coding-guidelines

基于 Andrej Karpathy 极简编码哲学，整合四大核心能力：

- **🐛 Bug Fix**：根因驱动最小化修复（复现→根因→修复→验证）
- **🔍 Code Review**：P0/P1/P2 分级审查（Critical/Warning/Suggestion）
- **🛡️ Security Hardening**：深度安全规范（输入验证/注入防御/密钥管理）
- **🧪 Test Driven**：测试驱动开发（覆盖率≥80%，回归测试必写）

**适配语言**：Python、C++、Java、Go、JavaScript/TypeScript、Rust

**设计原则**：
1. 绝不擅自假设 — 只基于已有代码和明确需求行动
2. 拒绝过度设计 — 不为"未来可能"添加抽象层
3. 每行代码必须有目的 — 禁止无目标编码
4. 修改前说明理由，修改后说明影响范围

### flask-web-dev

Flask 后端开发专项规范：

- **项目结构**：Blueprint 组织、配置分离、环境变量管理
- **路由设计**：RESTful 风格、API 版本控制、统一响应格式
- **数据库操作**：上下文管理器、参数化查询、连接池
- **认证安全**：密码哈希（SHA256+salt）、Session 安全配置、CSRF 防护
- **错误处理**：全局错误处理器、HTTP 状态码规范、日志记录

### frontend-compatibility

前端浏览器兼容性保障：

- **ES6+ 语法**：可选链/空值合并的降级方案、模板字符串兼容性
- **DOM 事件**：事件对象跨浏览器处理、事件委托模式
- **CSS 兼容**：Flexbox/Grid 前缀、CSS 变量回退、sticky 定位
- **Fetch API**：Polyfill 方案、XMLHttpRequest 降级

### hybrid-python-web

前后端协同开发协调：

- **架构决策**：前后端分离 vs 模板渲染 vs 混合方案
- **API 设计**：JSON 格式约定、CORS 配置、请求头规范
- **数据传递**：模板渲染传值、API 动态加载、类型一致性
- **认证同步**：Session 认证流程、状态检查、Token 管理
- **错误协调**：后端统一错误格式、前端统一错误处理、加载状态管理

---

## 🚀 快速开始

### 场景 1：新功能开发

```
用户：帮我实现一个用户认证模块

→ universal-karpathy-coding-guidelines 触发
  1. 需求确认清单（消除歧义）
  2. 方案选型对比（2-3 种方案）
  3. 执行计划（带验证步骤）
  4. 完整代码（Karpathy Style + Minimal Coding）
  5. 测试覆盖（Test Driven）
  6. 安全审查（Security Hardening）

→ flask-web-dev 协同（如果是 Flask 项目）
  - 路由设计规范
  - 数据库操作规范
  - Session 安全配置
```

### 场景 2：Bug 修复

```
用户：这段代码在并发下偶尔崩溃

→ universal-karpathy-coding-guidelines 触发
  1. MCVE 复现（最小复现案例）
  2. 根因分析（数据流/时序/状态/假设）
  3. 最小修复（针对根因，非掩盖症状）
  4. 回归测试（验证修复）
  5. 横向排查（相似代码检查）
```

### 场景 3：代码审查

```
用户：帮我 review 这段代码

→ universal-karpathy-coding-guidelines 触发
  1. 整体评估（质量/风险等级）
  2. P0 严重问题（必须修复）
  3. P1 警告问题（建议修复）
  4. P2 优化建议（可选）
  5. 修复代码示例
```

### 场景 4：纯概念问答（不触发）

```
用户：Python 的 GIL 是什么？

→ 不触发任何 Skill
→ 仅提供概念解释，不输出代码
```

---

## 🛠️ 工具脚本

### 校验技能格式

```bash
# 校验所有 SKILL.md 格式合规
python tools/validate-skills.py

# 输出示例
✅ universal-karpathy-coding-guidelines/SKILL.md 格式正确
✅ flask-web-dev/SKILL.md 格式正确
✅ frontend-compatibility/SKILL.md 格式正确
✅ hybrid-python-web/SKILL.md 格式正确
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR！新增技能必须：

1. 遵循 [Agent Skills 标准](https://agentskills.io) 格式（YAML frontmatter + Markdown body）
2. 包含清晰的 `description`（说明触发条件和用途）
3. 通过 `tools/validate-skills.py` 格式校验
4. 更新本 README 的技能清单

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📄 许可证

[MIT](LICENSE)

---

## 🙏 致谢

- 基于 [Andrej Karpathy](https://karpathy.ai) 的编码哲学
- 遵循 [Agent Skills 开放标准](https://agentskills.io)（Anthropic 发起）
- 兼容 [Trae](https://trae.ai)、[Cursor](https://cursor.com)、[Claude Code](https://claude.ai/code)、[VS Code Copilot](https://github.com/features/copilot) 等 50+ 种 AI 编程工具 [^53^]
- 通过 [skills.sh](https://skills.sh) 和 `npx skills` CLI 分发 [^62^]
